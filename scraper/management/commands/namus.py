from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import re
import requests
from requests.exceptions import HTTPError
from django.core.management.base import BaseCommand, CommandError
from scraper.models import MissingPerson


class Command(BaseCommand, webdriver.Chrome, ChromeDriverManager):
    help = 'fetches the missing person data from namus'

    def __init__(self):
        super().__init__()
        # Set Driver and options
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def handle(self, *args, **options):
        self.nav_to_home_page()
        id_nums = self.collect_ids()
        self.get_individual_json(id_nums)
        self.quit()
        return

    def nav_to_home_page(self):
        '''
        Navigate to search result page and expand results to 100 per page.
        '''
        self.driver.get('https://www.namus.gov/MissingPersons/Search#/results')
        self.driver.implicitly_wait(10)
        more_results = self.driver.find_element_by_xpath(
            '/ html/body/div[1]/div[4]/form/div[2]/section[2]/div/div/div/div/div[3]/div[3]/search-results-pager/ng-include/div/div/div/label/select/option[4]')
        more_results.click()
        self.driver.implicitly_wait(20)

    def collect_ids(self):
        '''
        Sets a while loop that will go through x amount of pages.
        for each page, search out ID numbers. Strip MP from front of ID 
        number, then append number to array for later use.
        '''
        next_btn = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[4]/form/div[2]/section[2]/div/div/div/div/div[3]/div[3]/search-results-pager/ng-include/div/div/div/nav/button[2]')
        id_numbers = []
        n = 0
        # ! Set # of pages to go through here
        while n < 1:
            cells = self.driver.find_elements_by_class_name(
                'ui-grid-cell-contents')
            pattern = '^MP[0-9]'
            for cell in cells:
                cell = cell.text
                if re.match(pattern, cell):
                    cell = cell[2:]
                    id_numbers.append(cell)
            # Click pagination button to advance to next set of results.
            next_btn.click()
            self.driver.implicitly_wait(10)
            n = n + 1
        print('found {} id numbers'.format(len(id_numbers)))
        return id_numbers

    def handle_json(self,data):
        '''
        Recieve raw json data. Parse data and store pertinent parts in the DB
        '''
        agency_primary = data['investigatingAgencies'][0]
        if data['hrefDefaultImageThumbnail']:
            thumbnail_url = 'https://www.namus.gov/{}'.format(
                data['hrefDefaultImageThumbnail'])
        else:
            # todo: insert a generic photo URL here. Or do it on the front end?
            # todo: Either make a static image or pick it up from the frontend.
            pass
        try:
            date_reported = agency_primary['dateReported']
        except KeyError:
            date_reported = ''
        try:
            agency_website = agency_primary['selection']['agency']['websiteUrl']
        except KeyError:
            agency_website = ''
        data_to_save = {
            'id_number': data['id'],
            'first_name': data['subjectIdentification']['firstName'],
            'last_name': data['subjectIdentification']['lastName'],
            'current_age': data['subjectIdentification']['currentMinAge'],
            'age_when_missing': data['subjectIdentification']['computedMissingMinAge'],
            'gender': data['subjectDescription']['sex']['name'],
            'height': '{} inches'.format(data['subjectDescription']['heightFrom']),
            'weight': '{} pounds'.format(data['subjectDescription']['weightFrom']),
            'ethnicity': data['subjectDescription']['ethnicities'][0]['name'],
            'hair_color': data['physicalDescription']['hairColor']['name'],
            'eye_color': data['physicalDescription']['leftEyeColor']['name'],
            'circumstances': data['circumstances']['circumstancesOfDisappearance'],
            'agency_name': agency_primary['name'],
            'agency_city': agency_primary['city'],
            'agency_state': agency_primary['state']['name'],
            'agency_address': agency_primary['selection']['agency']['street1'],
            'agency_zip': agency_primary['selection']['agency']['zipCode'],
            'thumbnail_url': thumbnail_url,
            'case_qr_code': 'https: // www.namus.gov/{}'.format(data['hrefQRCode']),
            'date_reported': date_reported,
            'agency_website': agency_website
        }
        already_exists = MissingPerson.objects.filter(id_number=data_to_save['id_number'])
        if already_exists:
            print('Record already exists, skipping')
            return False
        else:
            MP = MissingPerson(**data_to_save)
            MP.save()
            print('Record Saved')
            return True

    def get_individual_json(self, id_nums):
        '''
        visit each individual case page and retrieve JSON response with 
        all information pertaining to that case. For each page, call handle_json
        to parse and store data.
        '''
        total_saved = 0
        for num in id_nums:
            try:
                response = requests.get(
                    'https://www.namus.gov/api/CaseSets/NamUs/MissingPersons/Cases/{}/'.format(num))
                data = response.json()
                saved = self.handle_json(data)
                if saved is True:
                    total_saved += 1
            except HTTPError as http_error:
                print('error occurred----{}'.format(http_error))
        print('Action Complete. Saved {} records'.format(total_saved))

    def quit(self):
        self.driver.quit()

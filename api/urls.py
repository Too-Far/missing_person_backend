from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'missingperson', views.MissingPersonViewSet)
urlpatterns = router.urls
# urlpatterns = [
#     path('', include('router.urls')),
#     path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
# ]

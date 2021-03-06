"""tracker_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from mentor_tracker import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'personnel', views.PersonnelViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'expertisecategories', views.ExpertiseCategoryViewSet)
router.register(
    r'personnelexpertisecategories', views.PersonnelExpertiseCategoryViewSet)
router.register('locations', views.LocationViewSet)
router.register('organizations', views.OrganizationViewSet)
router.register('devices', views.DeviceViewSet)
router.register('personnelorganizations', views.PersonnelOrganizationViewSet)
router.register('personneldevices', views.PersonnelDeviceViewSet)
router.register(
    'personnellocationentries', views.PersonnelLocationEntryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

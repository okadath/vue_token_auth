from django.urls import include, path
from rest_framework.routers import SimpleRouter
from user_account.views import *
# remove rest?

router=SimpleRouter()
router.register('profile',ProfileData)

urlpatterns=router.urls
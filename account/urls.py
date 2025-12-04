from rest_framework.routers import DefaultRouter
from account.views import StaffViewSet

router = DefaultRouter()
router.register(r'staff', StaffViewSet, basename='staff')

urlpatterns = router.urls
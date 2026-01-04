from rest_framework.routers import DefaultRouter
from .views import JobViewSet, JobApplicationViewSet, MessageViewSet, CategoryViewSet

router = DefaultRouter()
router.register("jobs", JobViewSet)
router.register("applications", JobApplicationViewSet)
router.register("messages", MessageViewSet)
router.register("categories", CategoryViewSet)


urlpatterns = router.urls

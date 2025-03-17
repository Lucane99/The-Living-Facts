from django.urls import path, include
from rest_framework import routers
from .views import DataCategoryViewSet, DataSourceViewSet, DataFormatViewSet, DataViewSet, DataFileViewSet, DataReportViewSet

router = routers.DefaultRouter()
router.register(r'data_categories', DataCategoryViewSet)
router.register(r'data_sources', DataSourceViewSet)
router.register(r'data_formats', DataFormatViewSet)
router.register(r'data_files', DataFileViewSet)
router.register(r'data_reports', DataReportViewSet)
router.register(r'data', DataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from rest_framework import viewsets
from .models import DataCategory, DataSource, DataFormat, Data, DataFile, DataReport
from .serializers import DataCategorySerializer, DataSourceSerializer, DataFormatSerializer, DataSerializer, DataFileSerializer, DataReportSerializer

class DataCategoryViewSet(viewsets.ModelViewSet):
    queryset = DataCategory.objects.all()
    serializer_class = DataCategorySerializer

class DataSourceViewSet(viewsets.ModelViewSet):
    queryset = DataSource.objects.all()
    serializer_class = DataSourceSerializer

class DataFormatViewSet(viewsets.ModelViewSet):
    queryset = DataFormat.objects.all()
    serializer_class = DataFormatSerializer

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

class DataFileViewSet(viewsets.ModelViewSet):
    queryset = DataFile.objects.all()
    serializer_class = DataFileSerializer
    

class DataReportViewSet(viewsets.ModelViewSet):
    queryset = DataReport.objects.all()
    serializer_class = DataReportSerializer

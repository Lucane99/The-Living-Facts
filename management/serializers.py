from rest_framework import serializers
from .models import DataCategory, DataSource, DataFormat, Data, DataFile, DataReport

class DataCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DataCategory
        fields = '__all__'

class DataSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSource
        fields = '__all__'

class DataFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataFormat
        fields = '__all__'

class DataFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataFile
        fields = '__all__'

class DataSerializer(serializers.ModelSerializer):
    category = DataCategorySerializer()
    source = DataSourceSerializer()
    format = DataFormatSerializer()
    files = DataFileSerializer(many=True)

    class Meta:
        model = Data
        fields = '__all__'

class DataReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataReport
        fields = '__all__'

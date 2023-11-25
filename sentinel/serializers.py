from rest_framework import serializers
from .models import GeometryBorderModel, GeometryDistrictModel, GeometryImmobileModel, NDVIStatisticsModel

"""
Retornam dados referentes as coordenadas dos imóveis, distritos e fronteira.
"""    
class GeometryImmobileWithoutPropertiesSerializer(serializers.ModelSerializer):
    pass

class GeometryDistrictWithoutPropertiesSerializer(serializers.ModelSerializer):
    pass

class GeometryBorderWithoutPropertiesSerializer(serializers.ModelSerializer):
    pass


"""
Retornam dados referentes aos dados estatísticos.
"""
class NDVIStatisticsSerializer(serializers.ModelSerializer):
    pass

"""
Retornam dados referentes aos dados estatísticos mais atual e aninhado as propriedades dos imóveis.
""" 
class PropertieImmobileSerializer(serializers.ModelSerializer):
    pass
from django.contrib import admin
from .models import GeometryCoordinatesUTM, GeometryBorder, GeometryDistrict, GeometryImmobile, DistrictImagesNDVISub, ImmobileImagesNDVISub, DistrictImageRGB, ImmobileImageRGB, NDVIStatistics


@admin.register(GeometryCoordinatesUTM)
class GeometryCoordinatesUTMAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GeometryCoordinatesUTM._meta.fields]

@admin.register(GeometryBorder)
class GeometryBorderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GeometryBorder._meta.fields]

@admin.register(GeometryDistrict)
class GeometryDistrictAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GeometryDistrict._meta.fields]

@admin.register(GeometryImmobile)
class GeometryImmobileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GeometryImmobile._meta.fields]

@admin.register(DistrictImagesNDVISub)
class DistrictImagesNDVISubAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DistrictImagesNDVISub._meta.fields]

@admin.register(ImmobileImagesNDVISub)
class ImmobileImagesNDVISubAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ImmobileImagesNDVISub._meta.fields]

@admin.register(DistrictImageRGB)
class DistrictImageRGBAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DistrictImageRGB._meta.fields]

@admin.register(ImmobileImageRGB)
class ImmobileImageRGBAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ImmobileImageRGB._meta.fields]

@admin.register(NDVIStatistics)
class ImmobileImageRGBAdmin(admin.ModelAdmin):
    list_display = [field.name for field in NDVIStatistics._meta.fields]
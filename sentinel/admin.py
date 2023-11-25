from django.contrib import admin
from .models import (
    GeometryCoordinatesUTMModel,
    GeometryBorderModel,
    GeometryDistrictModel,
    GeometryImmobileModel,
    DistrictImagesNDVISubModel,
    ImmobileImagesNDVISubModel,
    NDVIStatisticsModel,
    DistrictImageRGBModel,
    ImmobileImageRGBModel
)

@admin.register(GeometryCoordinatesUTModel)
class GeometryCoordinatesUTMAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GeometryCoordinatesUTMModel._meta.fields]

@admin.register(GeometryBorderModel)
class GeometryBorderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GeometryBorderModel._meta.fields]

@admin.register(GeometryDistrictModel)
class GeometryDistrictAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GeometryDistrictModel._meta.fields]

@admin.register(GeometryImmobileModel)
class GeometryImmobileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GeometryImmobileModel._meta.fields]

@admin.register(DistrictImagesNDVISubModel)
class DistrictImagesNDVISubAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DistrictImagesNDVISubModel._meta.fields]

@admin.register(ImmobileImagesNDVISubModel)
class ImmobileImagesNDVISubAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ImmobileImagesNDVISubModel._meta.fields]

@admin.register(DistrictImageRGBModel)
class DistrictImageRGBAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DistrictImageRGBModel._meta.fields]

@admin.register(ImmobileImageRGBModel)
class ImmobileImageRGBAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ImmobileImageRGBModel._meta.fields]

@admin.register(NDVIStatisticsModel)
class ImmobileImageRGBAdmin(admin.ModelAdmin):
    list_display = [field.name for field in NDVIStatisticsModel._meta.fields]
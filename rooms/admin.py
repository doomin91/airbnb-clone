from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedroom",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
    )

    list_filter = ("city", "country")

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    pass
    

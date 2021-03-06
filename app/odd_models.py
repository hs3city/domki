from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

"""
PUTTING EVERYTHING IN COMMENT CAUSE THE CODE BELOW WAS THROWING 30+ ERRORS:
    app.Bathroom.home: (fields.E304) Reverse accessor for 'Bathroom.home' clashes with reverse accessor for 'Bedroom.home'.
        HINT: Add or change a related_name argument to the definition for 'Bathroom.home' or 'Bedroom.home'.
WHEN TRYING TO MAKEMIGRATIONS
"""
# Create your models here.
# class Home(models.Model):
#     APARTMENT_TYPES = (
#         (1, _("Studio")),
#         (2, _("Apartment")),
#         (3, _("House")),
#         (4, _("Twin house")),
#         (5, _("Shared room")),
#         (6, _("Shared apartment")),
#     )
#
#     author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="homes")
#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)
#     # TODO: do some magic update after on new Review
#     rating = models.DecimalField(decimal_places=2, max_digits=2)
#
#     # PRICES AND AVAILABILITY
#     is_available_now = models.BooleanField(default=False)
#     price_per_night = models.CharField(max_length=10, blank=False)
#     price_per_week = models.CharField(max_length=10, blank=False)
#     price_per_month = models.CharField(max_length=10, blank=False)
#     price_per_year = models.CharField(max_length=10, blank=True)
#
#     # ADDRESS
#     city = models.CharField(max_length=100, blank=False)
#     street = models.CharField(max_length=100, blank=False)
#     postal_code = models.CharField(max_length=10, blank=False)
#     building_number = models.CharField(max_length=10, blank=True)
#     apartment_number = models.CharField(max_length=10, blank=True)
#     # baza django-teryt
#
#
#     # APARTMENT INFO
#     type_of_rent = models.CharField(choices=APARTMENT_TYPES, blank=False, max_length=20)
#     floor = models.PositiveIntegerField(blank=False)
#     floors_in_building = models.PositiveIntegerField(blank=False)
#
#     # TODO: do some auto counting magic https://www.stavros.io/posts/how-replace-django-model-field-property/
#     # ROOM COUNTS
#     living_rooms = models.PositiveIntegerField(blank=False)
#     bedrooms = models.PositiveIntegerField(blank=False)
#     bathrooms = models.PositiveIntegerField(blank=False)
#     toilets = models.PositiveIntegerField(blank=False)
#     kitchens = models.PositiveIntegerField(blank=False)
#     garages = models.PositiveIntegerField(blank=False)
#
#     # RULES
#     PET_POLICY = (
#         (0, _("No pets allowed")),
#         (1, _("Dogs only")),
#         (2, _("Cats only")),
#         (3, _("Cats and dogs")),
#     )
#     pet_policy = models.CharField(choices=PET_POLICY, blank=False, max_length=15)
#     smoking_allowed = models.BooleanField(default=False)
#     guests_overnight = models.BooleanField(default=False)
#
#
# class Room(models.Model):
#     SHAPES = (
#         (0, _("Square")),
#         (1, _("Rectangle")),
#         (2, _("Other"))
#     )
#     home = models.ForeignKey(Home, related_name="homes")
#     area_in_sq_m = models.PositiveIntegerField(blank=False)
#     shape = models.CharField(choices=SHAPES, blank=False, max_length=15)
#     angled_ceiling = models.BooleanField(default=False)
#     windowless = models.BooleanField(default=False)
#
#     class Meta:
#         abstract = True
#
#
# class Bedroom(Room):
#     szfaka = models.BooleanField(default=False)
#     bed = models.BooleanField(default=False)
#
#
# class LivingRoom(Room):
#     fireplace = models.BooleanField(default=False)
#
#
# class Bathroom(Room):
#     shower = models.BooleanField(default=False)
#     bath = models.BooleanField(default=False)
#     washing_machine = models.BooleanField(default=False)  # TODO: w sumie to dlaczego by nie w kuchni/garażu...
#     dryer = models.BooleanField(default=False)
#
#
# class Toilet(Room):
#     pass
#
#
# class Kitchen(Room):
#     stove = models.BooleanField(default=False)
#     oven = models.BooleanField(default=False)
#     fridge = models.BooleanField(default=False)
#     freezer = models.BooleanField(default=False)
#
#
# class Garage(Room):
#     BAYS = (
#         (1, "1"),
#         (2, "2"),
#         (3, "3+")
#     )
#     width_in_m = models.CharField(max_length=10, blank=False)
#     depth_in_m = models.CharField(max_length=10, blank=False)
#     bays = models.CharField(choices=BAYS, blank=False, max_length=10)
#
#
# class User(AbstractBaseUser):
#     city = models.CharField(max_length=100, blank=False)
#     street = models.CharField(max_length=100, blank=False)
#     postal_code = models.CharField(max_length=10, blank=False)
#     building_number = models.CharField(max_length=10, blank=True)
#     apartment_number = models.CharField(max_length=10, blank=True)
#     agency_employee = models.BooleanField(default=False)
#
#
# class Agency(models.Model):
#     city = models.CharField(max_length=100, blank=False)
#     street = models.CharField(max_length=100, blank=False)
#     postal_code = models.CharField(max_length=10, blank=False)
#     building_number = models.DecimalField(max_digits=10, decimal_places=10, blank=True)
#     apartment_number = models.DecimalField(decimal_places=10, max_digits=10, blank=True)
#
#
# class Review(models.Model):
#     user = models.ForeignKey(User)
#     rating = models.PositiveIntegerField()
#     review_text = models.TextField()
#
#
# class Image(models.Model):
#     room = models.ForeignKey(Room)
#     title = models.ImageField()  # TODO: add arguments
#
# class StandardParams(models.Model):

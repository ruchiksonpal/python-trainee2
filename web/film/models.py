from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

from web.film.constant import Active, ActiveBool, Type


class Category(models.Model):  # table Category
    name = models.TextField(null=False, max_length=200, error_messages={"unique": "This mail is already exist."})
    last_update = models.DateTimeField(_("Last updated date"), auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"
        verbose_name_plural = "category"


class Language(models.Model):  # table Language
    name = models.TextField(null=False, blank=False, unique=True)
    last_update = models.DateTimeField(_("Last updated date"), auto_now=True, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Language"
        verbose_name_plural = "Language"


class Film(models.Model):  # table Film
    title = models.TextField(max_length=200, null=False, unique=True)
    description = models.TextField(max_length=200, null=False)
    release_year = models.IntegerField(null=False)
    language = models.ForeignKey(Language, default=1, verbose_name="Language", on_delete=models.CASCADE,
                                 related_name="language_film")
    rental_duration = models.IntegerField(null=False)
    rental_rate = models.FloatField(null=False)
    length = models.IntegerField(null=False)
    replacement_cost = models.FloatField(null=False)
    rating = models.TextField(null=False, max_length=200)
    last_update = models.DateTimeField(_("Last updated date"), auto_now=True)
    special_features = models.TextField(max_length=200, null=False)
    fulltext = models.TextField(max_length=200, null=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Film"
        verbose_name_plural = "Film"


class FilmCategory(models.Model):  # table FilmCategory
    film = models.ForeignKey(Film, default=1, verbose_name="Film", on_delete=models.CASCADE, related_name="film")
    category = models.ForeignKey(Category, default=1, verbose_name="Category", on_delete=models.CASCADE,
                                 related_name="category_film")
    last_update = models.DateTimeField(_("last updated date"), auto_now=True)

    def __str__(self):
        return '{}'.format(self.category)

    class Meta:
        db_table = "FilmCategory"
        verbose_name_plural = "FilmCategory"


class Actor(models.Model):  # table Actor
    first_name = models.TextField(max_length=200, null=False, blank=False)
    last_name = models.TextField(max_length=200, null=False, blank=False)
    last_update = models.DateTimeField(_("Last update date"), auto_now=True, null=False)

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = "Actor"
        verbose_name_plural = "Actor"


class FilmActor(models.Model):  # table FilmActor
    actor = models.ForeignKey(to=Actor, default=1, verbose_name="Actor", on_delete=models.CASCADE,
                              related_name="actor_film")
    film = models.ForeignKey(to=Film, default=1, verbose_name="Film", on_delete=models.CASCADE,
                             related_name="film_film")
    last_update = models.DateTimeField(_("Last updated date"), auto_now=True)

    def __str__(self):
        return str(self.last_update)

    class Meta:
        db_table = "FilmActor"
        verbose_name_plural = "FilmActor"


class Country(models.Model):  # table Country
    country = models.TextField(max_length=200, null=False)
    last_update = models.DateTimeField(_("Last updated date country"), auto_now=True)

    def __str__(self):
        return self.country

    class Meta:
        db_table = "Country"
        verbose_name_plural = "Country"


class City(models.Model):  # table City
    city = models.TextField(max_length=200, null=False)
    country = models.ForeignKey(to=Country, default=1, verbose_name="Country", on_delete=models.CASCADE,
                                related_name="country_city")
    last_update = models.DateTimeField(_("Last updated date city "), auto_now=True)

    def __str__(self):
        return self.city

    class Meta:
        db_table = "City"
        verbose_name_plural = "City"


class Address(models.Model):  # table Address
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='user_address_u', null=True)
    address = models.TextField(max_length=500, null=False)
    address2 = models.TextField(max_length=500, null=True)
    district = models.TextField(max_length=100, null=False)
    city_id = models.ForeignKey(to=City, default=1, verbose_name="City", on_delete=models.CASCADE,
                                related_name="city_address")
    postal_code = models.IntegerField(null=False)
    phone = models.IntegerField(null=False)
    last_update = models.DateTimeField(_("last updated address"), auto_now=True)

    def __str__(self):
        return self.address

    class Meta:
        db_table = "Address"
        verbose_name_plural = "Address"


class Store(models.Model):  # table Store
    address = models.ForeignKey(to=Address, default=1, verbose_name="Address", on_delete=models.CASCADE,
                                related_name="address_store")
    last_update = models.DateTimeField(_("Last updated store date"), auto_now=True)

    def __str__(self):
        return str(self.last_update)

    class Meta:
        db_table = "Store"
        verbose_name_plural = "Store"


class UserProfile(models.Model):  # table UserProfile
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='user_profile_u', null=False)
    role = models.IntegerField(choices=Type.FieldStr.items(), default=Type.customer, null=False)
    created_ts = models.DateTimeField(_("Created Date"), auto_now_add=True)
    updated_ts = models.DateTimeField(_("Last Updated Date"), auto_now=True)

    def __str__(self):
        return self.user

    class Meta:
        db_table = "user_profile"
        verbose_name_plural = "User Profile"


class Inventory(models.Model):  # table Inventory
    film = models.ForeignKey(to=Film, default=1, verbose_name="Film", on_delete=models.CASCADE, related_name="film_inv")
    store = models.ForeignKey(to=Store, default=1, verbose_name="Store", on_delete=models.CASCADE,
                              related_name="store_inv")
    last_update = models.DateTimeField(_("LAst updated date"), auto_now=True)

    def __str__(self):
        return str(self.last_update)

    class Meta:
        db_table = "Inventory"
        verbose_name_plural = "Inventory"


class Rental(models.Model):  # table Rental
    rental_date = models.DateField(null=False)
    inventory = models.ForeignKey(to=Inventory, default=1, verbose_name="Inventory", on_delete=models.CASCADE,
                                  related_name="inv_rental")
    customer = models.ForeignKey(to=User, default=1, verbose_name="Customer", on_delete=models.CASCADE,
                                 related_name="customer_rental")
    return_date = models.DateField(null=False)
    staff = models.ForeignKey(to=User, default=1, verbose_name="StaffProfile", on_delete=models.CASCADE,
                              related_name="staff_rental")
    last_update = models.DateTimeField(_("Last updated date"), auto_now=True)

    def __str__(self):
        return str(self.rental_date)

    class Meta:
        db_table = "Rental"
        verbose_name_plural = "Rental"


class Payment(models.Model):  # table Payment
    customer = models.ForeignKey(to=User, default=1, verbose_name="Customer", on_delete=models.CASCADE,
                                 related_name="customer_payment")
    staff = models.ForeignKey(to=User, default=1, verbose_name="StaffProfile", on_delete=models.CASCADE,
                              related_name="staff_payment")
    rental = models.ForeignKey(to=Rental, default=1, verbose_name="Rental", on_delete=models.CASCADE,
                               related_name="rental_payment")
    amount = models.FloatField(null=False, max_length=20)
    payment_date = models.DateTimeField(_("Last payment date"), auto_now=True)

    def __str__(self):
        return str(self.amount)

    class Meta:
        db_table = "Payment"
        verbose_name_plural = "Payment"

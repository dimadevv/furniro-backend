import random
import string

from django.db import models

from apps.common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class HomeImage(BaseModel):
    home = models.ForeignKey("Home", on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='homes/images/', help_text="Upload an image for the home item")

    def __str__(self):
        return f"Image of {self.home.name}"


class Home(BaseModel):
    class ReviewChoice(models.IntegerChoices):
        ONE = 1, '1'
        TWO = 2, '2'
        THREE = 3, '3'
        FOUR = 4, '4'
        FIVE = 5, '5'

    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="categories")
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    discount = models.IntegerField(default=0)
    review = models.IntegerField(choices=ReviewChoice.choices)
    scu = models.CharField(max_length=255, unique=True, editable=False)
    description = models.CharField(max_length=255)
    size = models.ManyToManyField(Size, related_name="sizes", null=True, blank=True)
    color = models.ManyToManyField(Color, related_name="colors", null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.scu:
            self.scu = self.generate_unique_scu()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_unique_scu():
        from .models import Home

        while True:
            letters = ''.join(random.choices(string.ascii_uppercase, k=3))
            numbers = ''.join(random.choices(string.digits, k=6))
            scu = f"{letters}{numbers}"
            if not Home.objects.filter(scu=scu).exists():
                return scu

    def __str__(self):
        return self.name

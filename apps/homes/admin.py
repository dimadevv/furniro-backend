from django.contrib import admin

from apps.homes.models import Category, Size, HomeImage, Home


@admin.register(Category)
class CategoryAdminModel(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    list_display_links = ("id", "name", "created_at")


@admin.register(Size)
class SizeAdminModel(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


@admin.register(HomeImage)
class HomeImage(admin.ModelAdmin):
    list_display = ("id", "home", "image")
    list_display_links = ("id", "home", "image")


@admin.register(Home)
class HomesAdminModel(admin.ModelAdmin):
    list_display = ("id", "name", "price", "review", "size", "color")
    list_display_links = ("id", "name", "price", "review", "size", "color")
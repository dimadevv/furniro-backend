from django.contrib import admin

from apps.homes.models import Category, Size, HomeImage, Home, Color


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
    list_display = ("id", "name", "price", "review", "get_sizes", "get_colors")
    list_display_links = ("id", "name", "price", "review")

    def get_sizes(self, obj):
        return ", ".join([s.name for s in obj.size.all()])

    def get_colors(self, obj):
        return ", ".join([c.name for c in obj.colors.all()])
    get_colors.short_description = "Colors"


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")




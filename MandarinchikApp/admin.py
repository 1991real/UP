from django.contrib import admin
from .models import *


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(CountryProduction)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("id", "country")


@admin.register(Mandarin)
class MandarinAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "type",
        "country",
        "color",
        "price",
        "review_count",
    )

    def review_count(self, obj):
        return obj.reviews.count()

    review_count.short_description = "Количество отзывов"


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "mandarin",
        "rating",
        "short_comment",
    )

    def short_comment(self, obj):
        return obj.comment[:30]

    short_comment.short_description = "Краткий комментарий"
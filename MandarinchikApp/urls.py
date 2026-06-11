from django.urls import path
from . import views

urlpatterns = [

    # Мандарины
    path("", views.mandarin_list, name="mandarin_list"),
    path("create/", views.mandarin_create, name="mandarin_create"),
    path("<int:pk>/", views.mandarin_detail, name="mandarin_detail"),
    path("<int:pk>/update/", views.mandarin_update, name="mandarin_update"),
    path("<int:pk>/delete/", views.mandarin_delete, name="mandarin_delete"),

    # Отзывы
    path("reviews/", views.review_list, name="review_list"),

    path(
        "reviews/create/",
        views.review_create,
        name="review_create"
    ),

    path(
        "reviews/<int:pk>/",
        views.review_detail,
        name="review_detail"
    ),

    path(
        "reviews/<int:pk>/update/",
        views.review_update,
        name="review_update"
    ),

    path(
        "reviews/<int:pk>/delete/",
        views.review_delete,
        name="review_delete"
    ),
    # Types

    path(
        "types/",
        views.type_list,
        name="type_list"
    ),

    path(
        "types/create/",
        views.type_create,
        name="type_create"
    ),

    path(
        "types/<int:pk>/",
        views.type_detail,
        name="type_detail"
    ),

    path(
        "types/<int:pk>/update/",
        views.type_update,
        name="type_update"
    ),

    path(
        "types/<int:pk>/delete/",
        views.type_delete,
        name="type_delete"
    ),  
    # Countries
# Colors

path(
    "colors/",
    views.color_list,
    name="color_list"
),

path(
    "colors/create/",
    views.color_create,
    name="color_create"
),

path(
    "colors/<int:pk>/",
    views.color_detail,
    name="color_detail"
),

path(
    "colors/<int:pk>/update/",
    views.color_update,
    name="color_update"
),

path(
    "colors/<int:pk>/delete/",
    views.color_delete,
    name="color_delete"
),

path(
    "countries/",
    views.country_list,
    name="country_list"
),

path(
    "countries/create/",
    views.country_create,
    name="country_create"
),

path(
    "countries/<int:pk>/",
    views.country_detail,
    name="country_detail"
),

path(
    "countries/<int:pk>/update/",
    views.country_update,
    name="country_update"
),

path(
    "countries/<int:pk>/delete/",
    views.country_delete,
    name="country_delete"
),

]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
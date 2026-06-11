from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from .forms import *


def mandarin_list(request):
    mandarins = Mandarin.objects.all()

    return render(
        request,
        "mandarin/list.html",
        {"mandarins": mandarins}
    )


def mandarin_create(request):
    form = MandarinForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect("mandarin_list")

    return render(
        request,
        "mandarin/form.html",
        {"form": form}
    )


def mandarin_update(request, pk):
    mandarin = get_object_or_404(Mandarin, pk=pk)

    form = MandarinForm(
        request.POST or None,
        request.FILES or None,
        instance=mandarin
    )

    if form.is_valid():
        form.save()
        return redirect("mandarin_list")

    return render(
        request,
        "mandarin/form.html",
        {"form": form}
    )


def mandarin_delete(request, pk):
    mandarin = get_object_or_404(Mandarin, pk=pk)

    if request.method == "POST":
        mandarin.delete()
        return redirect("mandarin_list")

    return render(
        request,
        "mandarin/delete.html",
        {"object": mandarin}
    )


def mandarin_detail(request, pk):
    mandarin = get_object_or_404(Mandarin, pk=pk)

    return render(
        request,
        "mandarin/detail.html",
        {"mandarin": mandarin}
    )

def review_list(request):
    reviews = Review.objects.all()

    return render(
        request,
        "review/list.html",
        {"reviews": reviews}
    )


def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)

    return render(
        request,
        "review/detail.html",
        {"review": review}
    )


def review_create(request):
    form = ReviewForm(
        request.POST or None
    )

    if form.is_valid():
        form.save()
        return redirect("review_list")

    return render(
        request,
        "review/form.html",
        {"form": form}
    )


def review_update(request, pk):
    review = get_object_or_404(Review, pk=pk)

    form = ReviewForm(
        request.POST or None,
        instance=review
    )

    if form.is_valid():
        form.save()
        return redirect("review_list")

    return render(
        request,
        "review/form.html",
        {"form": form}
    )


def review_delete(request, pk):
    review = get_object_or_404(
        Review,
        pk=pk
    )

    if request.method == "POST":
        review.delete()
        return redirect("review_list")

    return render(
        request,
        "review/delete.html",
        {"review": review}
    )
def type_list(request):
    types = Type.objects.all()

    return render(
        request,
        "type/list.html",
        {"types": types}
    )


def type_detail(request, pk):
    type_obj = get_object_or_404(Type, pk=pk)

    return render(
        request,
        "type/detail.html",
        {"type_obj": type_obj}
    )


def type_create(request):
    form = TypeForm(
        request.POST or None
    )

    if form.is_valid():
        form.save()
        return redirect("type_list")

    return render(
        request,
        "type/form.html",
        {"form": form}
    )


def type_update(request, pk):
    type_obj = get_object_or_404(
        Type,
        pk=pk
    )

    form = TypeForm(
        request.POST or None,
        instance=type_obj
    )

    if form.is_valid():
        form.save()
        return redirect("type_list")

    return render(
        request,
        "type/form.html",
        {"form": form}
    )


def type_delete(request, pk):
    type_obj = get_object_or_404(
        Type,
        pk=pk
    )

    if request.method == "POST":
        type_obj.delete()
        return redirect("type_list")

    return render(
        request,
        "type/delete.html",
        {"type_obj": type_obj}
    )
def color_list(request):
    colors = Color.objects.all()

    return render(
        request,
        "color/list.html",
        {"colors": colors}
    )


def color_detail(request, pk):
    color = get_object_or_404(
        Color,
        pk=pk
    )

    return render(
        request,
        "color/detail.html",
        {"color": color}
    )


def color_create(request):
    form = ColorForm(
        request.POST or None
    )

    if form.is_valid():
        form.save()
        return redirect("color_list")

    return render(
        request,
        "color/form.html",
        {"form": form}
    )


def color_update(request, pk):
    color = get_object_or_404(
        Color,
        pk=pk
    )

    form = ColorForm(
        request.POST or None,
        instance=color
    )

    if form.is_valid():
        form.save()
        return redirect("color_list")

    return render(
        request,
        "color/form.html",
        {"form": form}
    )


def color_delete(request, pk):
    color = get_object_or_404(
        Color,
        pk=pk
    )

    if request.method == "POST":
        color.delete()
        return redirect("color_list")

    return render(
        request,
        "color/delete.html",
        {"color": color}
    )
def country_list(request):
    countries = CountryProduction.objects.all()

    return render(
        request,
        "country/list.html",
        {"countries": countries}
    )


def country_detail(request, pk):
    country = get_object_or_404(
        CountryProduction,
        pk=pk
    )

    return render(
        request,
        "country/detail.html",
        {"country": country}
    )


def country_create(request):
    form = CountryForm(
        request.POST or None
    )

    if form.is_valid():
        form.save()
        return redirect("country_list")

    return render(
        request,
        "country/form.html",
        {"form": form}
    )


def country_update(request, pk):
    country = get_object_or_404(
        CountryProduction,
        pk=pk
    )

    form = CountryForm(
        request.POST or None,
        instance=country
    )

    if form.is_valid():
        form.save()
        return redirect("country_list")

    return render(
        request,
        "country/form.html",
        {"form": form}
    )


def country_delete(request, pk):
    country = get_object_or_404(
        CountryProduction,
        pk=pk
    )

    if request.method == "POST":
        country.delete()
        return redirect("country_list")

    return render(
        request,
        "country/delete.html",
        {"country": country}
    )
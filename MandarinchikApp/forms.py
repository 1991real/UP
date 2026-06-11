from django.forms import ModelForm
from .models import *


class MandarinForm(ModelForm):
    class Meta:
        model = Mandarin
        fields = "__all__"


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"


class TypeForm(ModelForm):
    class Meta:
        model = Type
        fields = "__all__"


class ColorForm(ModelForm):
    class Meta:
        model = Color
        fields = "__all__"


class CountryForm(ModelForm):
    class Meta:
        model = CountryProduction
        fields = "__all__"
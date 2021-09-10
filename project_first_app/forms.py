from django import forms
from .models import Owner, Car


# creating a form
class AddOwnerForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Owner

        # specify fields to be used
        fields = [
            "first_name",
            "second_name",
            "birth_date",
            "home_address",
            "nation",
            "passport_number"
        ]


class AddCarForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Car

        # specify fields to be used
        fields = [
            "brand",
            "model",
            "color",
            "number"
        ]



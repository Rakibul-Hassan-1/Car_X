from django import forms

from .models import Brand


class BrandForm(froms.ModelForm):
    class Meta:
        model=Brand
        fields='__all__'
        labels={
            "name":"Brand Name",
        }


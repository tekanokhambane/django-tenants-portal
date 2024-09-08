from django import forms
from multitenancy.apps.models import Tenant


class TenantForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Name",
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    slug = forms.SlugField(
        max_length=100,
        label="Slug",
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    description = forms.CharField(
        max_length=100,
        label="Description",
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Tenant
        fields = ["name", "slug", "description"]

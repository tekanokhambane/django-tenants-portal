from django.conf import settings
from django.http import request
from ..users.models import TenantUser
from django import forms
from django.utils.translation import templatize, ugettext_lazy as _
from ..customers.models import Client
from .models import Staff, Customers
#from phonenumber_field.formfields import PhoneNumberField
#from phonenumber_field.widgets import PhoneNumber, PhoneNumberInternationalFallbackWidget
from django.utils.text import slugify 


class AddCustomerForm(forms.Form):
    email= forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    address_line = forms.CharField(label="Address", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    suburb = forms.CharField(label="Surbub", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    city = forms.CharField(label="City", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    province = forms.CharField(label="Province", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    postcode = forms.CharField(label="Postal Code", widget=forms.TextInput(attrs={"class":"form-control"}))
    phone_number = forms.RegexField(label="Cellphone",regex=r'^(\+27|0)[6-8][0-9]{8}$', error_messages= {'required':"Cellphone must be 10 or 14 digits"}, widget=forms.TextInput(attrs={"class":"form-control"}))
    #country = forms.CharField(label="Country", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    organisation = forms.CharField(label="Organisation", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))

class AddStaffForm(forms.Form):
    email= forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    job_description = forms.CharField(label="Job Description", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    department = forms.CharField(label="Department", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    skills = forms.CharField(label="Skills", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    educational_qualification = forms.CharField(label="Educational Qualifications", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    address_line = forms.CharField(label="Street", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    suburb = forms.CharField(label="Address line 2", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    city = forms.CharField(label="City", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    province = forms.CharField(label="City", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    postcode = forms.CharField(label="Country", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    #phone = PhoneNumberField(label="Phone", )


class EditstaffForm(forms.Form):
    email= forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    job_description = forms.CharField(label="Job Description", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    department = forms.CharField(label="Department", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    skills = forms.CharField(label="Skills", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    educational_qualification = forms.CharField(label="Educational Qualifications", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    address_line = forms.CharField(label="Street", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    suburb = forms.CharField(label="Address line 2", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    city = forms.CharField(label="City", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    province = forms.CharField(label="City", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    postcode = forms.CharField(label="Country", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    #phone = PhoneNumberField(label="Phone")



class EditCustomerForm(forms.Form):
    email= forms.EmailField(label="Email", max_length=50, show_hidden_initial=True, initial="customer.admin.email", widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    organisation = forms.CharField(label="Organisation", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    address_line = forms.CharField(label="Street", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    suburb = forms.CharField(label="Address line 2", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    city = forms.CharField(label="City", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    province = forms.CharField(label="City", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    postcode = forms.CharField(label="Country", max_length=250, widget=forms.TextInput(attrs={"class":"form-control"}))
    #phone = PhoneNumberField(label="Phone", max_length=250, widget=PhoneNumberInternationalFallbackWidget)


class AddTenantForm(forms.Form):
    name=forms.CharField(label="Name", max_length=300, widget=forms.TextInput(attrs={"class":"form-control"}))
    slug = forms.SlugField(label="Slug", max_length=300, widget=forms.TextInput(attrs={"class":"form-control"}))
    user_list = []
    if settings.DEBUG == True:
        template_list = (
            ('tenant1', 'template1'),
            ('t2_1608114756', 'template2'),
            ('t3_1607982529', 'template3'),
            ('t4_1605533761', 'template4'),
        )
    else:
        template_list = (
            ('snowball', 'snowball'),
        )
    try:
        users = TenantUser.objects.filter(user_type=3)
        for user in users:
            one_user=(user.id, user.email)
            user_list.append(one_user)
    except:
        user_list=[]
    
    templates = forms.ChoiceField(label="Template", choices=template_list, widget=forms.Select(attrs={"class":"form-control"}))
    owner = forms.ChoiceField(label="Email",choices=user_list, widget=forms.Select(attrs={"class":"form-control"}))
    
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class EditTenantForm(forms.Form):
    name=forms.CharField(label="Name", max_length=300, widget=forms.TextInput(attrs={"class":"form-control"}))
    description=forms.CharField(label="Description", max_length=500, widget=forms.TextInput(attrs={"class":"form-control"}))
    slug = forms.CharField(label="Slug", max_length=300, widget=forms.TextInput(attrs={"class":"form-control"}))
    #user_list = []
    #try:
    #    users = TenantUser.objects.filter(user_type=3)
    #    #user = TenantUser.objects.all()
    #    for user in users:
    #        one_user=(user.id, user.id)
    #        user_list.append(one_user)
    #except:
    #    user_list=[]
    #owner_id = forms.ChoiceField(label="User Id",choices=user_list, widget=forms.Select(attrs={"class":"form-control"}))
    
class CustomerAddTenantForm(forms.Form):
    name=forms.CharField(label="Name", max_length=300, widget=forms.TextInput(attrs={"class":"form-control"}))
    slug = forms.CharField(label="Slug", max_length=300, widget=forms.TextInput(attrs={"class":"form-control"}))
    user_list = []
    if settings.DEBUG == True:
        template_list = (
            ('t1_1605528147', 'template1'),
            ('t2_1605530124', 'template2'),
            ('t3_1605532812', 'template3'),
            ('t4_1605533761', 'template4'),
        )
    else:
        template_list = (
            ('snowball_1604918204', 'snowball'),
        )
    try:
        users = TenantUser.objects.filter(user_type=3)
        for user in users:
            one_user=(user.id, user.email)
            user_list.append(one_user)
    except:
        user_list=[]
    
    templates = forms.ChoiceField(label="Template", choices=template_list, widget=forms.Select(attrs={"class":"form-control"}))
    owner = forms.ChoiceField(initial="user.email", label="Email",choices=user_list, widget=forms.Select(attrs={"class":"form-control"}))
    
class EditTenantForm(forms.Form):
    name=forms.CharField(label="Name", max_length=300, widget=forms.TextInput(attrs={"class":"form-control"}))
    description=forms.CharField(label="Description", max_length=500, widget=forms.TextInput(attrs={"class":"form-control"}))
    slug = forms.CharField(label="Slug", max_length=300, widget=forms.TextInput(attrs={"class":"form-control"}))
    #user_list = []
    #try:
    #    users = TenantUser.objects.filter(user_type=3)
    #    #user = TenantUser.objects.all()
    #    for user in users:
    #        one_user=(user.id, user.id)
    #        user_list.append(one_user)
    #except:
    #    user_list=[]
    #owner_id = forms.ChoiceField(label="User Id",choices=user_list, widget=forms.Select(attrs={"class":"form-control"}))
  
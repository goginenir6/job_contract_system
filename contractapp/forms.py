from django.forms import ModelForm
from django import forms
from contractapp.models import Tenant, Employee
from django.contrib.auth.models import User


class TenantForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TenantForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
            self.fields[field].widget.attrs["placeholder"] = field.capitalize()
            self.fields[field].label = 'Pleae enter Tenant Name:'

    class Meta:
        model = Tenant
        fields = ["tenant_Name"]

def increment_emp_number(table):
    try:
        last_primary = table.objects.all().order_by('employee_id').last()
    except:
        return '0001'
    primary_no = last_primary.employee_id
    new_primary_no = str(int(primary_no) + 1)
    new_primary_no = primary_no[0:-(1)] + new_primary_no
    return new_primary_no

class EmployeeForm(ModelForm):
    # password = forms.PasswordInput()
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['employee_id'].initial = increment_emp_number(Employee)
        self.fields['tenantid'].initial = Tenant.objects.first()
    #     self.fields["employee_id"].widget.value = empno
    #     self.fields["email"].widget = forms.EmailInput()
    #     self.fields["ismanager"].widget = forms.CheckboxInput()
    #     self.fields["status"].widget = forms.CheckboxInput()
    #     self.fields["is_staff"].widget = forms.CheckboxInput()
    #     self.fields["is_admin"].widget = forms.CheckboxInput()
    #     self.fields["is_active"].widget = forms.CheckboxInput()
    #     for field in self.fields:
    #         self.fields[field].widget.attrs["class"] = "form-control"
            # self.fields[field].widget.attrs["placeholder"] = field.capitalize()

    class Meta:
        model = Employee
        # fields = '__all__'
        fields = ('tenantid', 'employee_id','first_name', 'last_name',
                  'email', 'password', 'remarks',
                  'profilepic', 'mobile_no','status', 
                  'is_admin', 'is_staff')#'tenantid', 'employee_id', 
        widgets = {
            "employee_id": forms.TextInput(attrs={ 'class': 'form-control', 'ReadOnly': 'True'}),
            # "employee_id": forms.la (attrs={ 'type':'hidden', 'class': 'form-control', 'ReadOnly': 'True'}),
            "tenantid": forms.TextInput(attrs={ 'type':'hidden', 'class': 'form-control'}),
            "first_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            "email": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            "password": forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}),
            "remarks": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Remarks'}),
            "mobile_no": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number'}),
            # "profilepic": forms.FileField(widget=forms.FileInput(attrs={'name':'applicant_resume'}),label='Resume'),
            # "profilepic": forms.ImageField(),
            
            # "ismanager": forms.CheckboxInput(attrs={'class': 'checkbox'}),
            "status": forms.Select(attrs={'class': 'form-control'}),
            "is_admin": forms.CheckboxInput(attrs={'class': 'checkbox'}),
            "is_staff": forms.CheckboxInput(attrs={'class': 'checkbox'})
        }




# def add_prefix(self, field_name):
# field_name = ATTR_FIELD_NAME_MAPPING.get(field_name, field_name)
# return super(AttributeForm, self).add_prefix(field_name)
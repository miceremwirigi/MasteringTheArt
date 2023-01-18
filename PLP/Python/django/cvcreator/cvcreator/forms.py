from django.forms import ModelForm
from .models import PersonalInfo

class PersonalInfoForm(ModelForm):
    class Meta:
        model = PersonalInfo
        fields = [
            "name",
            "idNumber",
            "dob",
            "gender",
            "email",
            "telephone",
            "religion",
        ]
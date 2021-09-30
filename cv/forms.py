from django.forms import ModelForm
from django.contrib.auth.models import User
from cv.models import Employee


# Create your forms here

class ApplyForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
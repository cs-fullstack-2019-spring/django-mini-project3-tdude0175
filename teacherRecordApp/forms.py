from django import forms
from .models import ClassRecordModel


class TeacherRecordForm(forms.ModelForm):
    class Meta():
        model = ClassRecordModel
        fields= 'teacherName','school','subject','hours','workDate'

# used form to hide the entry date so only admin can see it

# Need to practice with foreign keys
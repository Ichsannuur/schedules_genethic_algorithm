from django import forms
from penjadwalan_genetika.apps.classrooms.models import Classroom


class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

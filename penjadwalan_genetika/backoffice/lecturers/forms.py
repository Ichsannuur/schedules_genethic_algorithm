from django import forms
from penjadwalan_genetika.apps.lecturers.models import Lecture


class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ('name', 'study_programs',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

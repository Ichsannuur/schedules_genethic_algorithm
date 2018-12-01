from django import forms
from penjadwalan_genetika.apps.study_programs.models import StudyPrograms


class StudyProgramForm(forms.ModelForm):
    class Meta:
        model = StudyPrograms
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

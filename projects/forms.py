import wtforms.widgets
from django.forms import ModelForm
from .models import Project
from django import forms


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['vote_total', 'vote_ratio', 'owner']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }


    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'input'})


        # self.fields['title'].widget.attrs.update({'class': 'input'})


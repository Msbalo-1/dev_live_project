from django.forms import ModelForm
from .models import Project, Review
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




class reviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'Place your vote ',
            'body': 'Add a comment with your vote'
        }

    def __init__(self, *args, **kwargs):
        super(reviewForm, self).__init__(*args, **kwargs)

        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'input'})

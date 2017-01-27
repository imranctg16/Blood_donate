from django import forms
from .models import Division,Blood_group,data


class dataForm(forms.ModelForm):
      class Meta:
        # Provide an association between the ModelForm and a model
        model = data
        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        #exclude = ('category',)
        #or specify the fields to include (i.e. not include the category field)
        fields = ('division','blood_group','phone_number','image')
        help_texts = {
            'division': 'Select a Division',
            'blood_group': 'Select Blood Group',
            'phone_number': 'Provide Your number',
            'image':'Provide your pic'
        }
class searchForm(forms.ModelForm):
    class Meta:
        model=data
        fields = ('division','blood_group')
        help_texts = {
            'division': 'Select a Division',
            'blood_group': 'Select Blood Group',
        }

from django import forms
from django.core.exceptions import ValidationError
from djng.forms.fields import FloatField
from djng.styling.bootstrap3.forms import Bootstrap3Form
from djng.forms import NgFormValidationMixin, NgModelFormMixin


class BaseForm(Bootstrap3Form):
    first_name = forms.CharField(
        label='First name',
        min_length=3,
        max_length=20,
        )
    last_name = forms.RegexField(
        r'^[A-Z][a-z -]?',
        label='Last name',
        error_messages={'invalid': 'Last names shall start in upper case'},
        )
    sex = forms.ChoiceField(
        choices=(('m', 'Male'), ('f', 'Female')),
        widget=forms.RadioSelect, error_messages={'invalid_choice': 'Please select your sex'},
        )
    email = forms.EmailField(
        label='E-Mail',
        required=True,
        help_text='Please enter a valid email address',
        )
    
class SubscribeForm(NgFormValidationMixin, BaseForm):
    pass
    
class ModelScopeSubscribeForm(NgModelFormMixin, BaseForm):
    scope_prefix = 'subscribe_data'
    form_name = 'my_form'

    def clean(self):
        if self.cleaned_data.get('first_name') == 'John' and self.cleaned_data.get('last_name') == 'Doe':
            raise ValidationError('The full name "John Doe" is rejected by the server.')
        return super(ModelScopeSubscribeForm, self).clean()

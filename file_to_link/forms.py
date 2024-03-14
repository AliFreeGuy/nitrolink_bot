
from django import forms





class VolumeUsageForm(forms.Form):
    operation_choices = [('increase', 'increase'), ('decrease', 'decrease')]
    bot_choices = [('file_to_link', 'file_to_link'), ('link_to_file', 'link_to_file')]
    user = forms.IntegerField(required=True)
    operation_type = forms.ChoiceField(choices=operation_choices , required=True)
    bot_status = forms.ChoiceField(choices=bot_choices , required=True)
    volume = forms.FloatField(required=True)
    
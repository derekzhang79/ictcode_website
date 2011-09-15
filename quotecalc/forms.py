from django import forms

from models import Task, Quote


class QuoteForm(forms.ModelForm):
    tasks = forms.ModelMultipleChoiceField(
             widget=forms.CheckboxSelectMultiple(),
             queryset=Task.objects.all())

    class Meta:
        model = Quote
        fields = ('tasks',)

    def __init__(self, *args, **kwargs):
        try:
            tasks = kwargs.pop('tasks')
        except:
            tasks = None

        super(QuoteForm, self).__init__(*args, **kwargs)

        if tasks:
            self.fields['tasks'].queryset = tasks

    def clean(self):
        super(QuoteForm, self).clean()

        tasks = self.cleaned_data.get('tasks')

        if not tasks:
            raise forms.ValidationError('No tasks selected.')

        return self.cleaned_data

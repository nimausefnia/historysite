from .models import Entry
from django.forms import ModelForm, fields



class EntryForm(ModelForm):
    class Meta:
        model=Entry 
        fields=( 'text', )


    def __init__(self, *args,**kwargs):
      super().__init__(*args,**kwargs)
      self.fields['text'].widget.attrs.update({ 'class': 'textarea','placeholder':'What\'s on Your Mind?'})
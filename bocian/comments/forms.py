from django import forms

from comments.models import Komentarz


class FormKomentarz(forms.Form):
    nick = forms.CharField()
    email = forms.EmailField()
    tytul = forms.CharField()
    tresc = forms.CharField(widget=forms.Textarea())


class FormKomentarz2(forms.ModelForm):
    class Meta:
        model = Komentarz
        fields = ('nick', 'email', 'tytul', 'tresc')



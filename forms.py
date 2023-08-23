from django import forms

class AdvertisementForm (forms.Form):
    title = forms.CharField(max_length=64)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField()
    auction = forms.BooleanField(required=False)
    image = forms.ImageField()


class AdForm(forms.ModelForm):
    class Meta:
        fields = ['title', 'description', 'price', 'auction', 'image']

    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.startswith('?'):
            raise forms.ValidationError("Заголовок не может начинаться с вопросительного знака")
        return title
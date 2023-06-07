from django import forms

class UserForm(forms.Form):
    name = forms.CharField(
        label="Имя клиента", 
        required=True, #необходимость заполнить поле,
        widget=forms.TextInput #по умолчанию
        )
    age = forms.IntegerField(
        label="Возраст клиента", 
        required=True,
        widget=forms.TextInput #по умолчанию
        )
    comment = forms.CharField(
        label="Комментарий", 
        widget=forms.Textarea #вручную измененный, расширяемый!
        )
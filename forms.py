#ОБЫЧНАЯ ФОРМА


from django import forms


class BirthdayForm(forms.Form):
    first_name = forms.CharField(
        max_length=20,
        label='Имя'
    )
    last_name = forms.CharField(
        required=False,
        label='Фамилия',
        help_text='Необязательное поле'
    )
    birthday = forms.DateField(
        label='Дата рождения',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        label='Описание:',
        required=False
    )
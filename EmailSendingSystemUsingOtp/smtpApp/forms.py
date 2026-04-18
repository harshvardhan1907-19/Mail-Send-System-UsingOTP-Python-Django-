from django import forms

class Smtp(forms.Form):
    to = forms.EmailField(
        label="To",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'to-mail',
        }),
        max_length=50,
        required=True,
    )

    subject = forms.CharField(
        label='Subject',
        widget=forms.TextInput(attrs= {
            'class': 'form-control',
            'id': 'subject',
        }),
        max_length=100,
        required=True,
    )

    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={
            'rows': 10,
            'class': 'form-control',
            'id': 'msg',
        }),
        max_length=500,
        required=True,
    )

    otp = forms.CharField(
        label="Enter OTP..",
        max_length=6,
        required=False
    )

# class MailForm(forms.Form):
#     name
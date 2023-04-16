from django import forms
from .models import Contact


class MyForm(forms.ModelForm):
    
    EMAILS = [  
        ('alan.naji@yahoo.com', 'alan.naji@yahoo.com'),
        ('berguss22@hotmail.com', 'berguss22@hotmail.com'),
        ('alan.naji@genpact.com', 'alan.naji@genpact.com')
    ]
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.ChoiceField(label='Your Email', choices=EMAILS)
    age = forms.IntegerField(label='Your Age')
    msg = forms.CharField(label='Your Message', widget=forms.Textarea)

    class Meta:
        model = Contact
        fields = ['name', 'email','age','msg']

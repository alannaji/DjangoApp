from django.shortcuts import render,redirect
from .forms import MyForm

def home(request):

    if request.method == 'POST':
        form = MyForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']           
            msg = form.cleaned_data['msg']

            instance = form.save()
            return redirect('success', name=name,email=email)
    else:
        form = MyForm()
    return render(request, 'home.html',{'form' : form})

def success(request,name,email):

    print('Thank you '+ name + 'Will send you email @ '+ email)
    
    return render(request, 'success.html',{'name':name,'email':email })

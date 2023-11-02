from django.shortcuts import render,redirect
from .forms import RegistrationForm

# Create your views here.
def handle_request(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    else:
        form=RegistrationForm()  #Sending the new form to the user.
        return render(request,'Templates/hello.html',{'form':form})
    







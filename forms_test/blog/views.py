from django.shortcuts import render
from django import forms
#from .forms import NameForm
from django.http import HttpResponseRedirect
# Create your views here.


from django import forms

class NameForm( forms.Form):
    your_name = forms.CharField(label='Your name',max_length=100)

def index(req):
	if req.method == 'POST':
		form = NameForm( req.POST )
		if form.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		form = NameForm()
	return render( req ,'name.html', {'form':form })
	#return render( req ,'index.html', {'form':form })

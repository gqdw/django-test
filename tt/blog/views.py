from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

from django import forms
# Create your views here.

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	email = forms.EmailField(required=False)
	message = forms.CharField()

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			print cd['subject'],cd['message']
#			send_mail(
#            	cd['subject'],
#                cd['message'],
#				cd.get('email', 'noreply@example.com'),
#				['aca_jingru@qq.com'],
#			)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm()
	return render(request,'contact_form.html', {'form': form})

def thanks(request):
	return render( request,'thanks.html',{})

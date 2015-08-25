from django.shortcuts import render

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
			send_mail(
            	cd['subject'],
                cd['message'],
				cd.get('email', 'noreply@example.com'),
				['siteowner@example.com'],
			)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm()
	return render(request,'contact_form.html', {'form': form})

from django.shortcuts import render
from django import forms
from django.http import HttpResponse
# Create your views here.


class Userform(forms.Form):
	username = forms.CharField()
	headImg = forms.FileField()

def register(req):
	if req.method == 'POST':
		form = Userform(req.POST,req.FILES)
		if form.is_valid():
			cd = form.cleaned_data
			print cd['username']
			print req.FILES
			print cd['headImg'].name
			print cd['headImg'].size
			fp = file( cd['headImg'].name ,'wb' )
			s = cd['headImg'].read()
			fp.write(s)
			fp.close()
			return HttpResponse('ok')
	else:
		form = Userform()
	return render( req,'test.html',{'form':form })

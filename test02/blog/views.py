from django.shortcuts import render

from django.template import loader,Context
from django.http import HttpResponse
# Create your views here.
def index(req):
	t = loader.get_template('index.html')
	c = Context({'user':'aca'})
	html = t.render(c)
	return HttpResponse(html)
	
def index2(req):
	return 	render(req,'index.html', {'user':'gqdw'} )

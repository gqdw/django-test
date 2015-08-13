from django.shortcuts import render_to_response
from blog.models import Person
# Create your views here.

def index(req):
	ps = Person.objects.all()
	return render_to_response('index.html',{'persons':ps})

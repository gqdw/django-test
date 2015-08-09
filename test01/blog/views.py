from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context
from django.shortcuts import render_to_response
# Create your views here.
'''
def index(req):
	t = loader.get_template('index.html')
	c = Context({})
	return HttpResponse( t.render(c))	
'''

class Person():
#class Person(object):
	def __init__(self,name,age,sex):
		self.name = name
		self.sex = sex
		self.age = age
	def say(self):
		return "I'm " + self.name

def index(req):
#	user = {'name':'aca','age':29,'sex':'male'}
	user = Person('aca',30,'male')
	book_list = ['python','php','java','c']
	return render_to_response('index.html',{'title':'fuck', 'user':user,'book_list':book_list})
#	return HttpResponse('<h1>hello baby!</h1>')

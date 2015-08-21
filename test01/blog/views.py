from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context
from django.shortcuts import render_to_response
import datetime
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

def time(req):
	now = datetime.datetime.now()
	html = "<html><body>it is %s.</body></html>" % now
	return HttpResponse(html)	

def time2(req,offset):
	print offset
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta( hours=offset )
#	assert False
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)



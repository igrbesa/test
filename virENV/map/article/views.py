from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson

from django.templatetags.static import static

from article.models import Article
from article import forms

from sendfile import sendfile
from django.core.servers.basehttp import FileWrapper
import os
import mimetypes

from map.settings import RESOURCES_DIR

# Create your views here. how to display information of weppages 

def poc(request):
	name = 'Igor'
	html = "<html><body> Hi %s good luck</body></html>" % name
	return HttpResponse(html)

def extemplate(request):
	# name = 'Igor'
	# html = "<html><body> Hi %s good luck dsjks</body></html>" % name
	# return HttpResponse(html)
	return render_to_response('hello.html', {'name':'Igor'})

def listdb(request):
	return render_to_response('hello.html', {'name':'Lista db', 'articles':Article.objects.all()})

def adduser(request):
	# return render_to_response('adduser.html')

	if request.method == 'POST':
		data = {'name': '', 'ready': False, 'error': '', 'form_errors': ''}
		form = forms.ArticleForm(data = request.POST)

		if form.is_valid():
			print '---------- valid form--------'
			data['name'] = form.cleaned_data['Name']
			data['ready'] = True;
			#add to database
			# fname = form.cleaned_data['Name']
			# fsurname = form.cleaned_data['Surname']
			# fmail = form.cleaned_data['Email']
			# fcomment = form.cleaned_data['Comment']
			# a = Article(name=fname, surname = fsurname, mail=fmail, comment=fcomment)
			# a.save()

			# url = static('RadarChart.png')
			# return HttpResponse(simplejson.dumps(url))

			filepath = RESOURCES_DIR + '/mapPlakat.pdf'
			filepath = '/static/mapPlakat.pdf'
			filepath = '/static/clipit-1.4.2.tar.gz'
			return HttpResponse(simplejson.dumps(filepath))
			#return sendfile(request, RESOURCES_DIR + '/mapPlakat.pdf')
			# response = HttpResponse(simplejson.dumps(data), mimetype='application/pdf')
			#response = HttpResponse(FileWrapper(mapPlakat.getvalue()), content_type='application/pdf')
			#response['Content-Disposition'] = 'attachment; filename="mapPlakat.pdf"'
			#return response

			# wrapper = FileWrapper(open(filepath,'r'))
			# filename = 'mapPlakat.pdf'
			# content_type = mimetypes.guess_type(filename)[0] 
			# response = HttpResponse(wrapper, content_type = content_type) 
			# from django.utils.encoding import smart_str
			# response['X-Sendfile'] = smart_str(filepath)
			# response['Content-Length'] = os.path.getsize(filepath)
			# response['Content-Disposition'] = 'attachment; filename=%s/' % smart_str(filename)      
			# return response

	else:
		form = forms.ArticleForm()
		print 'adduser else'

	return render(request, 'adduser.html', {"form":form})
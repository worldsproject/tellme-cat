from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login

def add(request):
    url = request.POST['url']
    domain = url_parse(url)[1]

    s = Story(link=url, domain=domain)
    s.save()
    return HttpResponseRedirect('add_url.html', context_instance=RequestContext(request))

def add_url(request):
    return render_to_response('add_url.html',  context_instance=RequestContext(request))

def respond(request):
    return HttpResponse('Respond Page')

def process_login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return render_to_response('links.html', context_instance=RequestContext(request))
    else:
        print('Login Failed')
        #return invalid login
        
def login(request): 
return render_to_response('login.html', context_instance=RequestContext(request)) 



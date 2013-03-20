from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from urlparse import urlparse
from models import Story
import urllib
import BeautifulSoup


@login_required
def add(request):
    url = request.POST['url']
    parsed = urlparse(url)

    if parsed.scheme =='':
        url = 'http://' + url

    domain = urlparse(url)[1]

    soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(url))
    title = soup.title.string

    s = Story(link=url, domain=domain, title=title, user=request.user)
    s.save()
    return redirect('/list.html')

@login_required
def add_url(request):
    return render_to_response('add_url.html',  context_instance=RequestContext(request))

@login_required
def respond(request):
    return HttpResponse('Respond Page')

def process_login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        auth_login(request, user)
        return redirect('/list.html')
    else:
        print('Login Failed')
        #return invalid login
        
def process_logout(request):
    logout(request)
    return redirect('/')

@login_required
def list_page(request):
    stories = request.user.story_set.all()
    followups = []

    for story in stories:
        followups.push(story.followup_set.all())

    return render_to_response('list.html', {'stories':stories, 'followups':followups}, context_instance=RequestContext(request))

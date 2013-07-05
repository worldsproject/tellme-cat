from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from urlparse import urlparse
from models import Story, FollowUp
import urllib
import BeautifulSoup
from achievements.utils import get_user_score
from django.views.generic import TemplateView

class ListView(TemplateView):
    def get(self, request, *args, **kwargs):
        stories = request.user.story_set.all()
        data = []
        data.append('>')

        for story in stories:
            data.append(story)
            fu = story.followup_set.all()

            data.append('>')

            if not fu:
                data.append('x')
                data.append('<')
            else:
                for f in fu:
                    data.append(f)
                data.append('<')
        data.append('<')

        karma = get_user_score(request.user)
        karma = "Moo"
        println*("Hi")

        return render_to_response('list.html', {'data':data, 'karma':karma,}, context_instance=RequestContext(request))
        
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
def delete(request):
    url = request.POST['url']
    story = Story.objects.filter(link=url[:-1])

    story.delete()

    return redirect('/list.html')

@login_required
def respond(request):
    old = request.POST['old']
    new = request.POST['new']

    old_parsed = urlparse(old)

    if old_parsed.scheme == '':
        old_parsed = urlparse('http://' + old)

    new_parsed = urlparse(new)

    if new_parsed.scheme == '':
        new_parsed = urlparse('http://' + new)

    soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(new_parsed.geturl()))
    title = soup.title.string

    story = Story.objects.filter(link=old_parsed.geturl())

    # if nothing is returned, we need to return an error.

    r = FollowUp(link=new_parsed.geturl(), domain=new_parsed[1], story=story[0])
    r.save() 
    return redirect('/list.html')

def process_login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        auth_login(request, user)
        return redirect('/list.html')
    else:
        return redirect('/register.html')
        
def process_logout(request):
    logout(request)
    return redirect('/')

@login_required
def list_page(request):
    stories = request.user.story_set.all()
    data = []
    data.append('>')
    for story in stories:
        data.append(story)
        fu = story.followup_set.all()

        data.append('>')

        if not fu:
            data.append('x')
            data.append('<')
        else:
            for f in fu:
                data.append(f)
            data.append('<')
    data.append('<')

    return render_to_response('list.html', {'data':data,}, context_instance=RequestContext(request))

def register_user(request):
    email = request.POST['email']
    password = request.POST['password']

    User.objects.create_user(email, email, password)
    user = authenticate(username=email, password=password)
    auth_login(request, user)

    return redirect('/list')

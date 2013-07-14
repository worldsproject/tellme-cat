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
from badges import *

def home(request):
    karma = "None Yet."
    if request.user.is_authenticated():
        karma = get_user_score(request.user)

    return render_to_response('index.html', {'karma':karma}, context_instance=RequestContext(request))

@login_required
def add_page(request):
    return render_to_response('add_url.html', {'karma':get_user_score(request.user)}, context_instance=RequestContext(request))

def check_achievement(achievement, user):
    if achievement.evaluate(user):
        return achievement.name
    else:
        return False

@login_required
def view_profile(request):
    cow = check_achievement(CreateStoryAchievement(), request.user)
    dog = check_achievement(TenStoryAchievement(), request.user)
    dragon = check_achievement(FiftyStoryAchievement(), request.user)
    frog = check_achievement(HundredStoryAchievement(), request.user)
    horse = check_achievement(FiveHundredStoryAchievement(), request.user)
    moose = check_achievement(FollowUpAchievement(), request.user)
    ostrich = check_achievement(TenFollowUpAchievement(), request.user)
    rabbit = check_achievement(FiftyFollowUpAchievement(), request.user)
    seahorse = check_achievement(HundredFollowUpAchievement(), request.user)
    skunk = check_achievement(FiveHundredFollowUpAchievement(), request.user)

    data = {'cow':cow, "frog":frog, 'ostrich':ostrich, 'skunk':skunk, 'dog':dog, 'horse':horse, 'rabbit':rabbit, 'dragon':dragon, 'seahorse':seahorse, 'moose':moose}
    return render_to_response('profile.html', data, context_instance=RequestContext(request))

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
def respond_page(request):
    return render_to_response('add_url.html', {'karma':get_user_score(request.user)}, context_instance=RequestContext(request))

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

    r = FollowUp(user=request.user, link=new_parsed.geturl(), domain=new_parsed[1], story=story[0])
    r.save() 
    return redirect('/list.html')

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

    return render_to_response('list.html', {'data':data, 'karma':get_user_score(request.user)}, context_instance=RequestContext(request))

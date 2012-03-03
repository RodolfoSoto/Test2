from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from exam.models import *
from exam.forms import *


def home(request):
    zombie = Zombie.objects.all()
    return render_to_response('home.html', {
        'Zombie': zombie,
    })


def add_zombie(request):
    form = ZombieForm()
    if request.method == 'POST':
        form = ZombieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render_to_response('add_zombie.html', {
        'form': form,
    }, RequestContext(request))


def add_tweet(request):
    form = TweetForm()
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render_to_response('add_tweet.html', {
        'form': form,
    }, RequestContext(request))


def edit_zombie(request,pk):
    zombie = get_object_or_404(Zombie, pk=pk)
    form = ZombieForm(instance=zombie)
    if request.method == 'POST':
	form = ZombieForm(request.POST, instance=zombie)
	if form.is_valid():
		form.save()
		return redirect('home')
    return render_to_response('add_zombie.html', {
	'form': form,
    }, RequestContext(request))

#una vista no requiere de una template para mostrarse, solo se requiere lo que se quiera mostrar como edit_comment o edit_article

 
def edit_tweet(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    form = TweetForm(instance=tweet)
    if request.method == 'POST':
	form = TweetForm(request.POST, instance=tweet)
	if form.is_valid():
		form.save()
		return redirect('home')
    return render_to_response('add_tweet.html', {
	'form':form,
    }, RequestContext(request))


def delete_zombie(request, pk):
    Zombie.objects.filter(pk=pk).delete()
    return redirect('home')


def delete_tweet(request, pk):
    Tweet.objects.filter(pk=pk).delete()
    return redirect('home')




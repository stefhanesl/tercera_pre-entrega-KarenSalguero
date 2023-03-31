from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room, Message

@login_required
def rooms(request):
    context = {'rooms': Room.objects.all()}
    return render(request, 'rooms/rooms.html', context)

@login_required
def room(request, slug):
    context = {'room': Room.objects.get(slug=slug),
               'messages': Message.objects.all()[:25][::-1]}
    return render(request, 'rooms/room.html', context)
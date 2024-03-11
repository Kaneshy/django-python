from django.shortcuts import render
from .models import Room

# Create your views here.<ctrl63> # models.py



rooms = [
    {
        'id': 1,
        'name': 'Living Room',
        'description': 'This is the living room. It has a TV, a couch, and a few chairs.'
    },
    {
        'id': 2,
        'name': 'Bedroom',
        'description': 'This is the bedroom. It has a bed, a dresser, and a nightstand.'
    },
    {
        'id': 3,
        'name': 'Kitchen',
        'description': 'This is the kitchen. It has a stovetop, a sink, and a refrigerator.'
    }
]

def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request, pk):
    room = Room.objects.get(id=pk)
    return render(request, 'base/room.html', {'room': room})
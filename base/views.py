from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm
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

"""def create_room(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        room = Room(name=name, description=description)
        room.save()
        return redirect('home')"""

def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render (request, 'base/room_form.html', {'form': form})

def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})
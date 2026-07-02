from django.shortcuts import render, redirect, get_object_or_404
from .models import Plant, Pot
from .forms import PlantForm, PotForm
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PlantSerializer, PotSerializer

def home(request):
    return HttpResponse("Welcome to Nursery Management System")

def dashboard(request):
    return render(request, 'dashboard.html')


def plant_list(request):
    plants = Plant.objects.all()
    return render(request, 'plant_list.html', {'plants': plants})


def add_plant(request):
    form = PlantForm()

    if request.method == "POST":
        form = PlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plant_list')

    return render(request, 'add_plant.html', {'form': form})

def edit_plant(request, id):
    plant = get_object_or_404(Plant, id=id)
    form = PlantForm(instance=plant)

    if request.method == "POST":
        form = PlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plant_list')

    return render(request, 'edit_plant.html', {'form': form})

def delete_plant(request, id):
    plant = get_object_or_404(Plant, id=id)
    plant.delete()
    return redirect('plant_list')

@api_view(['GET'])
def get_plants(request):

    plants = Plant.objects.all()

    serializer = PlantSerializer(plants, many=True)

    return Response({
    "status": "success",
    "code": 200,
    "message": "All plants fetched",
    "data": serializer.data
})

@api_view(['POST'])
def add_plant_api(request):

    serializer = PlantSerializer(data=request.data)

    if serializer.is_valid():

        serializer.save()

        return Response({
    "status": "success",
    "code": 200,
    "message": "Plant added successfully",
    "data": serializer.data
})

    return Response({
    "status": "failed",
    "code": 400,
    "message": "Validation error",
    "errors": serializer.errors
})

@api_view(['PUT'])
def update_plant_api(request, id):

    plant = Plant.objects.get(id=id)

    serializer = PlantSerializer(
        plant,
        data=request.data
    )

    if serializer.is_valid():

        serializer.save()

        return Response({
    "status": "success",
    "code": 200,
    "message": "Plant updated successfully",
    "data": serializer.data
})

    return Response({
        "status": "failed",
        "code": 400,
        "message": "Update failed",
        "errors": serializer.errors
    })

@api_view(['DELETE'])
def delete_plant_api(request, id):

    plant = Plant.objects.get(id=id)

    plant.delete()

    return Response({
    "status": "success",
    "code": 200,
    "message": "Plant deleted successfully"
})

def pot_list(request):
    pots = Pot.objects.all()
    return render(request, 'pot_list.html', {'pots': pots})

def add_pot(request):
    form = PotForm()

    if request.method == "POST":
        form = PotForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('pot_list')

    return render(request, 'add_pot.html', {'form': form})

def edit_pot(request, id):
    pot = get_object_or_404(Pot, id=id)
    form = PotForm(instance=pot)

    if request.method == "POST":
        form = PotForm(request.POST, request.FILES, instance=pot)

        if form.is_valid():
            form.save()
            return redirect('pot_list')

    return render(request, 'edit_pot.html', {'form': form})

def delete_pot(request, id):
    pot = get_object_or_404(Pot, id=id)
    pot.delete()
    return redirect('pot_list')

@api_view(['GET'])
def get_pots(request):

    pots = Pot.objects.all()

    serializer = PotSerializer(pots, many=True)

    return Response({
        "status": "success",
        "code": 200,
        "message": "All pots fetched",
        "data": serializer.data
    })

@api_view(['POST'])
def add_pot_api(request):

    serializer = PotSerializer(
        data=request.data
    )

    if serializer.is_valid():

        serializer.save()

        return Response({
            "status": "success",
            "code": 200,
            "message": "Pot added successfully",
            "data": serializer.data
        })

    return Response({
        "status": "failed",
        "code": 400,
        "errors": serializer.errors
    })

@api_view(['PUT'])
def update_pot_api(request, id):

    pot = Pot.objects.get(id=id)

    serializer = PotSerializer(
        pot,
        data=request.data,
        partial=True
    )

    if serializer.is_valid():

        serializer.save()

        return Response({
            "status": "success",
            "code": 200,
            "message": "Pot updated successfully",
            "data": serializer.data
        })

    return Response({
        "status": "failed",
        "code": 400,
        "errors": serializer.errors
    })

@api_view(['DELETE'])
def delete_pot_api(request, id):

    pot = Pot.objects.get(id=id)

    pot.delete()

    return Response({
        "status": "success",
        "code": 200,
        "message": "Pot deleted successfully"
    })



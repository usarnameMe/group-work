import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehicle
from .forms import VehicleForm

def vehicle_list(request):
    brand_query = request.GET.get('brand')
    model_query = request.GET.get('model')
    year_query = request.GET.get('year')

    vehicles = Vehicle.objects.all()

    if brand_query:
        vehicles = vehicles.filter(brand__icontains=brand_query)
    if model_query:
        vehicles = vehicles.filter(model__icontains=model_query)
    if year_query:
        try:
            year = int(year_query)
            if 1950 <= year <= datetime.datetime.now().year:
                vehicles = vehicles.filter(year=year)
        except ValueError:
            pass

    current_year = datetime.datetime.now().year
    return render(request, 'vehicle_list.html', {'vehicles': vehicles, 'current_year': current_year})

def vehicle_detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    return render(request, 'vehicle_detail.html', {'vehicle': vehicle})

def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'add_vehicle.html', {'form': form})

def edit_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_detail', pk=vehicle.pk)
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'edit_vehicle.html', {'form': form, 'vehicle': vehicle})

def delete_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicle_list')
    return render(request, 'delete_vehicle.html', {'vehicle': vehicle})

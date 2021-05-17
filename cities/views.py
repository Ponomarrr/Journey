from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from cities.forms import CityForm
from cities.models import City


def home(request, pk=None):
    if request.method == 'POST':
        form = CityForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    if pk:
        # city = City.objects.filter(id=pk).first()
        # city = City.objects.get(id=pk)
        city = get_object_or_404(City, id=pk)
        context = {'object': city}
        return render(request, 'cities/details.html', context)
    form = CityForm()
    cities = City.objects.all()
    context = {'objects_list': cities, 'form': form}
    return render(request, 'cities/home.html', context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    context_object_name = 'object'
    template_name = 'cities/details.html'

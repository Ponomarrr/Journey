from django.shortcuts import render
from django.contrib import messages
from routes.forms import RouteForm
from routes.utils import get_routes


def home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {'form': form})


def find_routes(request):
    if request.method == "POST":
        form = RouteForm(request.POST or None)
        context = {'form': form}
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                context = get_routes(request, form)
            except ValueError as e:
                messages.error(request, e)
            # return render(request, 'routes/home.html', {'form': form})
        return render(request, 'routes/home.html', context)
    else:
        messages.error(request, 'Создайте маршрут')
        form = RouteForm()
        return render(request, 'routes/home.html', {'form': form})

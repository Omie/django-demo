from django.shortcuts import render

from .models import Fruit

def show_all(request):
    all_fruits = Fruit.objects.all()

    context = {"all_fruits": all_fruits}

    return render(request, "show_all.html", context=context)



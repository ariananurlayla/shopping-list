from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from django.shortcuts import render

# Create your views here.
def show_main(request):
    products = Product.objects.all()

    context = {
        'name': 'Ariana Nurlayla Syabandini',
        'class': 'PBP C',
        'products': products
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
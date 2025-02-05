from django.shortcuts import get_object_or_404, render
from category.models import Category
from store.models import Product

# Create your views here.
def store(request, category_slug = None):
    categories = None
    product   = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug = category_slug)
        product    = Product.objects.filter(category = categories, is_available = True)
    else:
        product    = Product.objects.all().filter(is_available = True)
    context    = {'product' : product}
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug = category_slug , slug = product_slug)
    except Exception as e:
        raise e  

    context = {'single_product': single_product}  
    return render(request, 'store/product_detail.html', context)
 
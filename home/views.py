# from django.shortcuts import render
# from feedback.models import Feedback

# def home_view(request):
#     return render(request, 'home/home.html')


# def home_view(request):
#     reviews = Feedback.objects.all().order_by('-created_at')[:6]
#     return render(request, 'home/home.html', {'reviews': reviews})



# def category_view(request):
#     return render(request, 'home/category.html')

# def contact_view(request):
#     return render(request, 'home/contact.html')


from django.shortcuts import render
from feedback.models import Feedback

from products.models import Product, Category

def home_view(request):
    reviews = Feedback.objects.all().order_by('-created_at')[:6]
    return render(request, 'home/home.html', {'reviews': reviews})

def about_view(request):
    return render(request, 'home/about.html')

def category_view(request):

    categories = Category.objects.all()

    return render(request, 'home/category.html', {
        'categories': categories
    })

def contact_view(request):
    return render(request, 'home/contact.html')




def home_view(request):
    query = request.GET.get('q')

    reviews = Feedback.objects.all().order_by('-created_at')[:6]
    categories = Category.objects.all()
    products = Product.objects.all().order_by('-created_at')[:12]

    if query:
        products = Product.objects.filter(name__icontains=query)

        related_products = Product.objects.filter(
            description__icontains=query
        ).exclude(id__in=products.values_list('id', flat=True))[:8]
    else:
        related_products = Product.objects.all().order_by('?')[:8]

    return render(request, 'home/home.html', {
        'reviews': reviews,
        'categories': categories,
        'products': products,
        'related_products': related_products,
        'query': query,
    })



def home_view(request):
    reviews = Feedback.objects.all().order_by('-created_at')[:6]
    categories = Category.objects.all()
    products = Product.objects.all()

    return render(request, 'home/home.html', {
        'reviews': reviews,
        'categories': categories,
        'products': products,
    })




    
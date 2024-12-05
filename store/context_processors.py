from .models import Category

def categories(request):
    """Context processor to include all categories in every template."""
    categories = Category.objects.all()
    categories = sorted(categories, key=lambda x: x.name)
    return {
        'categories': categories
    }

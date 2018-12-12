from .models import Category


def pass_data_to_context(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return context

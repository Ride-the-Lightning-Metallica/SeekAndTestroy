from .models import Category


def main_context_processor(request):
    context = {
        'categories': Category.objects.all()
    }

    return context

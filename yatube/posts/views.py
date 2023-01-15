from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls INDEX.")


def group_posts(request, slug):
    return HttpResponse("Hello, world. You're at the GROUP posts.")

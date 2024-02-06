from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Kania Almyra Bilqist',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)

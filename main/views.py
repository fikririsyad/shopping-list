from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Fikri Risyad Indratno',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
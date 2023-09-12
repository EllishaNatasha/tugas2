from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Ellisha Natasha',
        'class': 'PBP D',
        'description': 'Glasses',
        'amount': '50',
    }

    return render(request, "main.html", context)
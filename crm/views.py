from django.shortcuts import render


# Create your views here.
def indexPage(request):
    return render(request, './indexPage.html', )


def promoPage(request):
    return render(request, './promoPage.html', )


def examplesPage(request):
    return render(request, './examplesPage.html', )


def contactsPage(request):
    return render(request, './contactsPage.html', )


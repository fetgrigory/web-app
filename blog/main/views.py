'''
This module make

Athor: Fetkulin Grigory, Fetkulin.G.R@yandex.ru
Starting  03/12/2024
Ending 03/12/2024

'''
from django.shortcuts import render


# View function to render the index page
def index(request):
    """AI is creating summary for index

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    return render(request, 'main/index.html')


# View function to render the about page
def about(request):
    """AI is creating summary for about

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    return render(request, 'main/about.html')

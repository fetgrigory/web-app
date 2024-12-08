'''
This module make

Athor: Fetkulin Grigory, Fetkulin.G.R@yandex.ru
Starting  03/12/2024
Ending 08/12/2024

'''
from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArtilesForm
from django.views.generic import DetailView, UpdateView, DeleteView


# View function to display a list of news articles on the homepage
def news_home(request):
    """AI is creating summary for news_home

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    # Get all Artiles objects from the database
    news = Artiles.objects.all()
    # Render the template, passing the news data
    return render(request, "news/news_home.html", {"news": news})


# Class-based view to display details of a single news article
class PostDetailsView(DetailView):
    """AI is creating summary for PostDetailsView

    Args:
        DetailView ([type]): [description]
    """
    model = Artiles
    template_name = 'news/post_details.html'
    context_object_name = 'article'


# Class-based view to update an existing news article.
class PostUpdateView(UpdateView):
    """AI is creating summary for PostUpdateView

    Args:
        UpdateView ([type]): [description]
    """
    model = Artiles
    template_name = 'news/write_article.html'
    form_class = ArtilesForm


#  Class-based view to delete a news article
class PostDeleteView(DeleteView):
    """AI is creating summary for PostDeleteView

    Args:
        DeleteView ([type]): [description]
    """
    model = Artiles
    success_url = '/news/'
    template_name = 'news/post_delete.html'


# View function to create a new news article
def write_article(request):
    """AI is creating summary for write_article

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    # Variable to store any error messages
    error = ""
    if request.method == "POST":
        # Create a form instance from POST data
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
        # Redirect to the home page after successful submission
            return redirect("home")
        else:
            error = form.errors
    else:
        # Create an empty form instance for GET requests
        form = ArtilesForm()
        # Prepare data for rendering the template
    data = {"form": form, "error": error}
    # Render the template with form and error data
    return render(request, "news/write_article.html", data)

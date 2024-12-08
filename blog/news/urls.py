'''
This module make

Athor: Fetkulin Grigory, Fetkulin.G.R@yandex.ru
Starting  03/12/2024
Ending 08/12/2024

'''
from django.urls import path
from . import views
urlpatterns = [
     # Maps the root URL ('/') to the news_home view
    path('', views.news_home, name='news_home'),
    # Maps the URL 'write_article' to the write_article view
    path('write_article', views.write_article, name='write_article'),
    # Maps a URL with an integer primary key (pk) to the PostDetailsView
    path('<int:pk>', views.PostDetailsView.as_view(), name='post_details_view'),
    # Maps a URL with an integer primary key (pk) followed by '/update' to the PostUpdateView
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='post_update_view'),
    # Maps a URL with an integer primary key (pk) followed by '/delete' to the PostDeleteView
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='post_delete_view'),
]

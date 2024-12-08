'''
This module make

Athor: Fetkulin Grigory, Fetkulin.G.R@yandex.ru
Starting  03/12/2024
Ending 04/12/2024

'''
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # Includes Django's built-in admin interface at the '/admin/' URL
    path('admin/', admin.site.urls),
    # Includes URL patterns from the 'main' app
    path('', include('main.urls')),
    # Includes URL patterns from the 'news' app, accessible at '/news/'.
    path('news/', include('news.urls'))
    # Adds static files handling, allowing access to static files (e.g., CSS, JavaScript, images) during development and deployment.
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

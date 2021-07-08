import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.static import serve

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('ads/', include('ads.urls')),
    path('autos/', include('autos.urls')),
    path('cats/', include('cats.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]

# Serve the static HTML
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns += [
    url(r'^site/(?P<path>.*)$', serve,
        {'document_root': os.path.join(BASE_DIR, 'site'),
        'show_indexes': True},
        name='site_path'
        ),
]

# Serve the favicon - Keep for later
urlpatterns += [
    path('favicon.ico', serve, {
            'path': 'favicon.ico',
            'document_root': os.path.join(BASE_DIR, 'home/static'),
        }
    ),
]

# Switch to social login
try:
    from . import social_settings
    social_login = 'registration/login_social.html'
    urlpatterns.insert(0, path('accounts/login/', auth_views.LoginView.as_view(template_name=social_login)))
    print('Using', social_login, 'as the login template')
except:
    print('Using registration/login.html as the login template')


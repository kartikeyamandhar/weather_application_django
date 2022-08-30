from django.contrib import admin
from django.urls import path,include

# app/ is the url for the main weather users_app
# admin/ is the url for the django admin page
# account/ is the sublink for registration, login and logout forms

urlpatterns = [
    path('admin/',admin.site.urls),
    path('app/', include('weatherapp.urls')),
    path('account/', include('users_app.urls')),
]

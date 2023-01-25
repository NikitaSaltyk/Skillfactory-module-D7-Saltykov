from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   path("accounts/", include("allauth.urls")),
   path('pages/', include('django.contrib.flatpages.urls')),
   # Делаем так, чтобы все адреса из нашего приложения (newapp/urls.py)
   # подключались к главному приложению с префиксом posts/.
   path('news/', include('newapp.urls')),
   path('appointments/', include(('appointment.urls', 'appointment'), namespace='appointments')),

]
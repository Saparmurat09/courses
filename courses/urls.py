from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('coursesapp.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', RedirectView.as_view(url='docs/', permanent=True)),
]
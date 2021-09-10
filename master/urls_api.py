

from django.urls import path, include

urlpatterns = [
    path('pools/', include('pools.urls')),
]

urlpatterns = [path("api/", include(urlpatterns))]
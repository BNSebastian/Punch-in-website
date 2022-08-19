# schools/urls.py
from django.urls import (
    path,
    include,
)
from application import views
# from application.views import pontaj

urlpatterns = [  
    path("", views.homepage, name='homepage'),
    path("pontaj/", views.pontaj, name='pontaj'),
    # path("pontaj/", pontaj.as_view(), name='pontaj'),
    path("entries/", views.entries, name='entries'),
    path("entries_all/", views.entries_all, name='entries_all'),
    path("delete/<id>", views.delete, name='delete'),
    path("time_all/", views.time_all, name="time_all"),
    path("time/", views.time, name="time"),
]


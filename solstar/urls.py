from django.urls import path

from . import views

app_name = 'solstar'
urlpatterns = [
    # home page
    path('', views.index, name='index'),
    path('collection', views.collection, name='collection')
]

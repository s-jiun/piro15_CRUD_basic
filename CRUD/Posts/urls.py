from django.urls import path
from . import views

app_name = 'Posts'

urlpatterns = [
    path('', view = views.post_list, name='list'),
    path('<int:pk>/', view=views.post_detail, name='detail'),
]
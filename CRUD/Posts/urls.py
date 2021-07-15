from django.urls import path
from . import views

app_name = 'Posts'

urlpatterns = [
    path('', view = views.post_list, name='list'),
    path('<int:pk>/', view=views.post_detail, name='detail'),
    path('create/', view=views.post_create, name='create'),
    path('<int:pk>/update/', view=views.post_update, name='update'),
    path('<int:pk>/delete/', view=views.post_delete, name='delete'),
]
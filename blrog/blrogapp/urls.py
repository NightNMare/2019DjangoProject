from blrogapp import views
from django.urls import path


app_name = 'blrogapp'

urlpatterns = [
    path('',views.lists,name='lists'),
    path('<int:content_id>/',views.reading,name='reading'),
]
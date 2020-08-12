
from django.urls import path
from . import views, forms


urlpatterns = [
    path('',views.index, name = "Resume"),
    path('submit/',views.submit,name="submit"),


]
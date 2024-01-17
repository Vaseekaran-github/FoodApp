from django.contrib import admin
from django.urls import include,path
from . import views

urlpatterns = [
    #food/
    path("",views.index,name="index"),
    path("<int:item_id>/",views.details,name="detail"),
    path("add/",views.create_item,name="create_item"),
    path("update/<int:id>",views.update_item,name="update_item"),
    path("delete/<int:id>",views.delete_item,name="delete_item")
]
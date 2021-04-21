from django.urls import path

from . import views

urlpatterns = [
    path("<category_from_url>/",views.category, name="category")
]
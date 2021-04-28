from django.urls import path

from . import views

urlpatterns = [
    path("<category_from_url>/",views.category, name="category"),
    path("<category_from_url>/comments/<int:post_id_from_url>/",views.comments, name="comments")
]
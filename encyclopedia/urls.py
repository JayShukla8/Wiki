from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new_page, name="new"),
    path("random/", views.random_page, name="random"),
    path("<str:name>/", views.g_entry, name="entry"),
    path("<str:name>/edit/", views.edit_page, name="edit"),
]

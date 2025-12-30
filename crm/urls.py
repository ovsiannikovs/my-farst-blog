# crm/urls.py
from django.urls import path
from . import views

app_name = "crm"

urlpatterns = [
    # Заявки
    path("tickets/", views.tickets_list, name="tickets_list"),
    path("tickets/new/", views.ticket_create, name="ticket_create"),
    path("tickets/<int:pk>/", views.ticket_edit, name="ticket_edit"),
    path("tickets/<int:pk>/comment/", views.ticket_add_comment, name="ticket_add_comment"),

    # База знаний
    path("kb/", views.kb_list, name="kb_list"),
    path("kb/new/", views.kb_create, name="kb_create"),
    path("kb/<int:pk>/", views.kb_edit, name="kb_edit"),
]

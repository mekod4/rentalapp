from django.conf.urls import url

from .views import LoginView, LogoutView, RegistrationView

urlpatterns = [
    url(r'^login/$', LoginView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^registration/$', RegistrationView.as_view()),
]
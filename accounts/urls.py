from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('',views.indexView,name="home"),
    path('statementmuondu/',views.statementView,name="statementmuondu"),
    path('contribution/',views.contributionView,name="contribution"),
    path('login/',LoginView.as_view(),name="login_url"),
]
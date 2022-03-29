from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    path('signup', views.signup, name = 'signup'),
    path('withdraw', views.withdraw, name = 'withdraw'),
    path('deposit', views.deposit, name = 'deposit'),
    path('bnb', views.bnb, name = 'bnb'),
    path('btc', views.btc, name = 'btc'),
    path('eth', views.eth, name = 'eth'),
    path('sol', views.sol, name = 'sol'),
    path('usdt', views.usdt, name = 'usdt'),
    path('dashboard', views.dashboard, name = 'dashboard'),
]

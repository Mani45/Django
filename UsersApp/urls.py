from UsersApp import views
from django.urls import path

urlpatterns=[
    path('users',views.UsersAPI),
    path('strategies',views.strategiesAPI),
    path('login',views.LoginAPI),
    path('updateStrategyRecord',views.updateStrategy),
    path('deleteStrategyRecord',views.deleteStrategy)

]
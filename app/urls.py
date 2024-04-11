from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('home', home, name='home'),
    path('create_racer', RacerCreate.as_view(), name='create_racer'),
    path('create_team', TeamCreate.as_view(), name='create_team'),
    path('create_bolide', BolideCreate.as_view(), name='create_bolide'),
    path('create_admin', AdminCreate.as_view(), name='create_admin'),
    path('view_racer/<int:pk>/', RacerView.as_view(), name='view_racer'),
    path('view_team/<int:pk>/', TeamView.as_view(), name='view_team'),
    path('view_bolide/<int:pk>/', BolideView.as_view(), name='view_bolide'),
    path('racers_list', RacersList.as_view(), name='racers_list'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
from django.urls import path, include
from .views import *

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    # path('<user>/', ProfileView.as_view(), name='profile'),
    path('<slug>/', RestaurantView.as_view(), name='restaurant'),

    # path('restaurant/contact/', ContactView.as_view(), name='contact'),
    path('category/', ItemCategoryView.as_view(), name='category'), # TODO: change path to <restaurant>/category
]

from django.urls import path, include
from .views import *

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # restaurant
    path('<slug>/', RestaurantView.as_view(), name='restaurant-info'),
    path('<slug>/contact/', ContactView.as_view(), name='restaurant-contact'),
    # categories
    path('<slug>/categories/', ItemCategoryListView.as_view(), name='restaurant-category'),
    # TODO: change url from <name> to <pk>
    path('<slug>/categories/<id>/', ItemCategoryDetailView.as_view(), name='restaurant-category-detail'),
    # dashboard
    path('categories/create/', ItemCategoryCreateView.as_view(), name='restaurant-category-create'),
    # items
    path('<slug>/items/', ItemListview.as_view(), name='restaurant-items'),
    path('<slug>/items/<id>/', ItemDetailView.as_view(), name='restaurant-item-detail'),
    # dashboard
    path('items/create/', ItemCreateView.as_view(), name='restaurant-item-create'),
]

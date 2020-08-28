from django.urls import path, include
from .views import *

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # restaurant
    path('<slug>/', RestaurantView.as_view(), name='restaurant-info'),
    path('<slug>/contact/', ContactView.as_view(), name='restaurant-contact'),
    path('<slug>/review/', RestaurantReviewView.as_view(), name='restaurant-review'),
    # categories
    path('<slug>/categories/', ItemCategoryListView.as_view(), name='restaurant-category'),
    path('<slug>/categories/<id>/', ItemCategoryDetailView.as_view(), name='restaurant-category-detail'),
    # dashboard
    path('categories/create/', ItemCategoryCreateView.as_view(), name='restaurant-category-create'),
    # items
    path('<slug>/items/', ItemListview.as_view(), name='restaurant-items'),
    path('<slug>/item/<id>/', ItemDetailView.as_view(), name='restaurant-item-detail'),
    path('<slug>/item/<id>/review/', ItemReviewView.as_view(), name='restaurant-item-review'),
    # dashboard
    path('items/create/', ItemCreateView.as_view(), name='restaurant-item-create'),
]

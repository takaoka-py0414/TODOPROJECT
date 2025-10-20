from django.urls import path
from django.views.generic import RedirectView
from . import views
from django.contrib.auth import views as auth_views

app_name = 'todo'  

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='list', permanent=False), name='home'),

    path('list/', views.TodoList.as_view(), name='list'),
    path('detail/<int:pk>/', views.TodoDetail.as_view(), name='detail'),
    path('create/', views.TodoCreate.as_view(), name='create'),
    path('delete/<int:pk>/', views.TodoDelete.as_view(), name='delete'),
    path('update/<int:pk>/', views.TodoUpdate.as_view(), name='update'),

    path('top/', views.TopView.as_view(), name='top'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('select/', views.SelectView.as_view(), name='select'),
    path('mypage/', views.MypageView.as_view(), name='mypage'),
    path('meal-input/', views.MealInputView.as_view(), name='meal_input'),
    path('history/', views.HistoryView.as_view(), name='history'),

    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('meal/list/', views.MealListView.as_view(), name='meal_list'),
    path('meal/detail/<int:pk>/', views.MealDetailView.as_view(), name='meal_detail'),
    path('meal/create/', views.MealCreateView.as_view(), name='meal_create'),
    path('meal/update/<int:pk>/', views.MealUpdateView.as_view(), name='meal_update'),
    path('meal/delete/<int:pk>/', views.MealDeleteView.as_view(), name='meal_delete'),

    path('products/list/', views.ProductListView.as_view(), name='products_list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='products_detail'),
    path('products/create/', views.ProductCreateView.as_view(), name='products_create'),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='products_update'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='products_delete'),

    path('product/<int:pk>/edit/', views.ProductEditView.as_view(), name='product_edit'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
]

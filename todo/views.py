from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
)
from .models import TodoModel, Meal, Product
from django.urls import reverse_lazy

class TodoList(ListView):
    template_name = 'meal/list.html'
    model = TodoModel

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')

class TopView(TemplateView):
    template_name = 'top.html'

class SignupView(TemplateView):
    template_name = 'accounts/signup.html'  # ← 修正

class SelectView(TemplateView):
    template_name = 'select.html'

class MypageView(TemplateView):
    template_name = 'mypage.html'

class MealInputView(TemplateView):
    template_name = 'meal-input.html'

class HistoryView(TemplateView):
    template_name = 'history.html'

class LoginView(TemplateView):
    template_name = 'login.html'

class MealListView(ListView):
    model = Meal
    template_name = 'meal/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        breakfast_list = Meal.objects.filter(category='朝食')
        lunch_list = Meal.objects.filter(category='昼食')
        dinner_list = Meal.objects.filter(category='夕食')
        groups = [
            {'title': '朝食', 'items': breakfast_list},
            {'title': '昼食', 'items': lunch_list},
            {'title': '夕食', 'items': dinner_list},
        ]
        context['groups'] = groups
        return context

class MealDetailView(DetailView):
    model = Meal
    template_name = 'meal/detail.html'

class MealCreateView(CreateView):
    model = Meal
    template_name = 'meal/create.html'
    fields = '__all__'
    success_url = reverse_lazy('meal_list')

class MealUpdateView(UpdateView):
    model = Meal
    template_name = 'meal/update.html'
    fields = '__all__'
    success_url = reverse_lazy('meal_list')

class MealDeleteView(DeleteView):
    model = Meal
    template_name = 'meal/delete.html'
    success_url = reverse_lazy('meal_list')

class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'products/create.html'
    fields = '__all__'
    success_url = reverse_lazy('products_list')

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'products/update.html'
    fields = '__all__'
    success_url = reverse_lazy('products_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('products_list')

class ProductEditView(TemplateView):
    template_name = 'edit.html'

from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView, RedirectView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .models import TodoModel, Meal, Product
from django.urls import reverse_lazy

class TodoList(RedirectView):
    pattern_name = 'todo:meal_list'
    permanent = False

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('todo:list')

class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('todo:list')

class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('todo:list')

class TopView(TemplateView):
    template_name = 'products/top.html'  

class SignupView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('todo:login')

class SelectView(TemplateView):
    template_name = 'select.html'

class MypageView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/mypage.html'
    login_url = reverse_lazy('todo:login')

class MealInputView(TemplateView):
    template_name = 'meal-input.html'

class HistoryView(TemplateView):
    template_name = 'meal/history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = Meal.objects.order_by('-duedate')
        grouped = {}
        for m in qs:
            d = m.duedate
            if hasattr(d, 'date'):
                d = d.date()
            grouped.setdefault(d, []).append(m)
        history = sorted(grouped.items(), key=lambda x: (x[0] is None, x[0]), reverse=True)
        context['history'] = history
        return context

class MealListView(ListView):
    model = Meal
    template_name = 'meal/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        breakfast_list = Meal.objects.filter(category='朝食')
        lunch_list = Meal.objects.filter(category='昼食')
        dinner_list = Meal.objects.filter(category='夕食')
        context['breakfast_list'] = breakfast_list
        context['lunch_list'] = lunch_list
        context['dinner_list'] = dinner_list
        return context

class MealDetailView(DetailView):
    model = Meal
    template_name = 'meal/detail.html'

class MealCreateView(CreateView):
    model = Meal
    template_name = 'meal/create.html'
    fields = '__all__'
    success_url = reverse_lazy('todo:meal_list')

class MealUpdateView(UpdateView):
    model = Meal
    template_name = 'meal/update.html'
    fields = '__all__'
    success_url = reverse_lazy('todo:meal_list')

class MealDeleteView(DeleteView):
    model = Meal
    template_name = 'meal/delete.html'
    success_url = reverse_lazy('todo:meal_list')

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
    success_url = reverse_lazy('todo:products_list')

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'products/update.html'
    fields = '__all__'
    success_url = reverse_lazy('todo:products_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('todo:products_list')

class ProductEditView(TemplateView):
    template_name = 'edit.html'

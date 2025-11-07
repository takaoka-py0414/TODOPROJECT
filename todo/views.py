from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView, RedirectView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import TodoModel, Meal, Product
from .forms import CustomUserCreationForm

class TodoList(LoginRequiredMixin, RedirectView):
    login_url = reverse_lazy('todo:login')
    pattern_name = 'todo:meal_list'
    permanent = False

class TodoDetail(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('todo:login')
    template_name = 'detail.html'
    model = TodoModel

class TodoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('todo:login')
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('todo:list')

class TodoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('todo:login')
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('todo:list')

class TodoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('todo:login')
    template_name = 'update.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('todo:list')

class TopView(TemplateView):
    template_name = 'products/top.html'

class SignupView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('todo:login')

class SelectView(TemplateView):
    template_name = 'select.html'

class MypageView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/mypage.html'
    login_url = reverse_lazy('todo:login')

class MealInputView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('todo:login')
    template_name = 'meal-input.html'

class HistoryView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('todo:login')
    template_name = 'meal/history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = Meal.objects.filter(user=self.request.user).order_by('-duedate')
        grouped = {}
        for m in qs:
            d = m.duedate
            if hasattr(d, 'date'):
                d = d.date()
            grouped.setdefault(d, []).append(m)
        history = sorted(grouped.items(), key=lambda x: (x[0] is None, x[0]), reverse=True)
        context['history'] = history
        return context

class MealListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('todo:login')
    model = Meal
    template_name = 'meal/list.html'

    def get_queryset(self):
        return Meal.objects.filter(user=self.request.user).order_by('-duedate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = self.get_queryset()
        context['breakfast_list'] = qs.filter(category='朝食')
        context['lunch_list'] = qs.filter(category='昼食')
        context['dinner_list'] = qs.filter(category='夕食')
        return context

class MealDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('todo:login')
    model = Meal
    template_name = 'meal/detail.html'

    def get_queryset(self):
        return Meal.objects.filter(user=self.request.user)

class MealCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('todo:login')
    model = Meal
    template_name = 'meal/create.html'
    fields = ['title', 'memo', 'priority', 'duedate', 'category']
    success_url = reverse_lazy('todo:meal_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MealUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('todo:login')
    model = Meal
    template_name = 'meal/update.html'
    fields = ['title', 'memo', 'priority', 'duedate', 'category']
    success_url = reverse_lazy('todo:meal_list')

    def get_queryset(self):
        return Meal.objects.filter(user=self.request.user)

class MealDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('todo:login')
    model = Meal
    template_name = 'meal/delete.html'
    success_url = reverse_lazy('todo:meal_list')

    def get_queryset(self):
        return Meal.objects.filter(user=self.request.user)

class ProductListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('todo:login')
    model = Product
    template_name = 'products/list.html'

class ProductDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('todo:login')
    model = Product
    template_name = 'products/detail.html'

class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('todo:login')
    model = Product
    template_name = 'products/create.html'
    fields = '__all__'
    success_url = reverse_lazy('todo:products_list')

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('todo:login')
    model = Product
    template_name = 'products/update.html'
    fields = '__all__'
    success_url = reverse_lazy('todo:products_list')

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('todo:login')
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('todo:products_list')

class ProductEditView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('todo:login')
    template_name = 'edit.html'

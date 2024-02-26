from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Expense
from .forms import AddExpenseForm
from django.views import View
# Create your views here.


class Home(View):
    def get(self, request):
        expense_data = Expense.objects.all()
        return render(request, 'expenses/landing.html', {'expense_data': expense_data})


class Add_Expense(View):
    def get(self, request):
        form = AddExpenseForm
        return render(request, 'expenses/add_expense.html', {'form': form})

    def post(self, request):
        form = AddExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'expenses/add_expense.html', {'form': form})


class Delete_Expense(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        expense_data = Expense.objects.get(id=id)
        expense_data.delete()
        return redirect('/')


class Edit_Expense(View):
    def get(self, request, id):
        expense_data = get_object_or_404(Expense, id=id)
        form = AddExpenseForm(instance=expense_data)
        return render(request, 'expenses/edit_expense.html', {'form': form})

    def post(self, request, id):
        expense_data = get_object_or_404(Expense, id=id)
        form = AddExpenseForm(request.POST, instance=expense_data)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'expenses/edit_expense.html', {'form': form})

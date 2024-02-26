from django.urls import path
from . import views
from .views import Home, Add_Expense, Delete_Expense, Edit_Expense

app_name = 'expenses'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('add/', Add_Expense.as_view(), name='add_expense'),
    path('edit_expense/<int:id>/', Edit_Expense.as_view(), name='edit_expense'),
    path('delete_expense/<int:id>/', Delete_Expense.as_view(), name='delete_expense'),
]
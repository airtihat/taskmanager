from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Expense
from .forms import ExpenseForm  # تأكد من وجود نموذج لتسجيل المصروفات

def expense_list(request):
    return render(request, 'family_expenses/list.html')

@login_required
def expense_dashboard(request):
    return render(request, 'family_expenses/expense_list.html')

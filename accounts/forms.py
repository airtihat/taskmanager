from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

# ✅ نموذج تسجيل الدخول
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='اسم المستخدم',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم المستخدم'})
    )
    password = forms.CharField(
        label='كلمة المرور',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'كلمة المرور'})
    )

# ✅ نموذج إنشاء مستخدم جديد
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="البريد الإلكتروني",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'البريد الإلكتروني'})
    )
    phone_number = forms.CharField(
        required=True,
        label="رقم الجوال",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رقم الجوال'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']
        labels = {
            'username': 'اسم المستخدم',
            'password1': 'كلمة المرور',
            'password2': 'تأكيد كلمة المرور',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم المستخدم'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'كلمة المرور'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'تأكيد كلمة المرور'}),
        }

from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib.auth import authenticate, login
from .forms import UserLoginForm, SignupForum
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


from myapp.models import *

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Перенаправляем на главную страницу после входа
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})



def signup(request):
    if request.method == 'POST':
        form = SignupForum(request.POST)
        if form.is_valid():
            print("Valid")
            user = form.save()
            login(request, user)
            return redirect('login')
        else:
            print("Invalid")
    else:
        form = SignupForum()
    return render(request, 'signup.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect('/login/')  # Перенаправляем на главную страницу после выхода

def home(request):
    all_mae=Mobels.objects.all()
    all_category=Category.objects.all()
    return render(request, 'home.html',{'all_mae':all_mae,'all_category':all_category})

def signup_view(request):
    return render(request, 'signup.html')


def my_view(request):
    user_authenticated = request.user.is_authenticated  # Проверяем, аутентифицирован ли пользователь
    return render(request, 'home.html', {'user_authenticated': user_authenticated})

def base(request):
    return render(request, 'base2.html')

def service1(request):
    all_mae=Mobels.objects.all()
    all_category=Category.objects.all()
    every_posts=Mobels.objects.all()
    return render(request,'service.html',{'ML':every_posts, 'all_mae':all_mae,'all_category':all_category})

# def show_post(request, Mobels_id):
#     mebel1=get_object_or_404(Mobels, id=Mobels_id)
#     categ = Category.objects.all()
#     return render(request,'service.html',{
#         'mebel':mebel1.mebel
#         'content': mebel1.
#     })

# def show_post(request, Mobels_id):
#     mebel1 = get_object_or_404(Mobels, id=Mobels_id)
#     categ = Category.objects.filter(category=mebel1.category)
#     return render(request, 'service.html', {
#         'mebel': mebel1,
#         'content': categ,
#     })

def index(request):
    all_mebels = Mobels.objects.all()
    category = Category.objects.all()
    return render(request, 'home.html',{'mebel':all_mebels,'cat':category})

# def mobels_by_category(request,category_id):
#     category = get_object_or_404(Category, id=category_id)
#     mobels = Mobels.objects.filter(category=category)
#     return render(request,'mobels_by_category.html', {'LK':category, 'KL':mobels} )
# def mobels_by_category(request, category_id):
#     category = get_object_or_404(Category, id=category_id)
#     mobels = Mobels.objects.filter(category=category)
#     categories = Category.objects.all()  # Assuming you want to list all categories

#     return render(request, 'mobels_by_category.html', {
#         'LK': category,
#         'KL': mobels,
#         'categories': categories  # Pass all categories to the template
#     })
def mobels_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    mobels = Mobels.objects.filter(category=category)
    categories = Category.objects.all()

    return render(request, 'mobels_by_category.html', {
        'LK': category,
        'KL': mobels,
        'categories': categories
    })

# def post_detail(request, Mobels_id):
#     mebel = get_object_or_404(Mobels, id=Mobels_id)
#     category=Category.objects.all()
#     return render(request, 'postdetail.html', {
#         'mebel':mebel.mebel,
#         'content': mebel.content,
#         'category':category})



def post_detail(request, Mobels_id):
    mebel = get_object_or_404(Mobels, id=Mobels_id)
    categories = Category.objects.all()
    all_mebels = Mobels.objects.all()
    return render(request, 'postdetail.html', {
        'mebel': mebel,
        'categories': categories,
        'mebel2':all_mebels
    })

def show_category(request,category_id):
    all_mae=Mobels.objects.filter(id=category_id)
    all_category=Category.objects.all()
    return render(request, 'service.html', {'all_mae':all_mae,'all_category':all_category})
    

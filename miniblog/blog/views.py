from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginForm, PostForm, ContactForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import  messages
from blog.models import Post
from django.contrib.auth.models import Group

# Create your views here.
def home(request):
    posts=Post.objects.all()
    return render(request, 'blog/home.html',{'posts':posts})

def aboutus(request):
    return render(request, 'blog/aboutus.html')

def contact(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form=ContactForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Your message has been sent Successfully!!!')
                form=ContactForm()
        else:
            form=ContactForm()
        return render(request, 'blog/contact.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')



def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user=request.user
        full_name=user.get_full_name()
        gps=user.groups.all()
        return render(request, 'blog/dashboard.html',{'posts':posts,'full_name':full_name, 'groups':gps})
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def signup(request):
    if request.method == "POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Congratulations you have become an Author !!!!')
            user=fm.save()
            group=Group.objects.get(name='Author')
            user.groups.add(group)

            # un=fm.cleaned_data.get('username')
            # fn=fm.cleaned_data['first_name']
            # ls=fm.cleaned_data['last_name']
            # em=fm.cleaned_data['email']
            # user=authenticate(username=un,first_name=fn,last_name=ls,email=em)
            # login(request, user)
            # return HttpResponseRedirect('/')
            fm = SignUpForm()

    else:
        fm=SignUpForm()
    return render(request, 'blog/signup.html', {'form':fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method =="POST":
            form=LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                pwd=form.cleaned_data.get('password')
                user=authenticate(username=uname, password=pwd)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in successfully!!!')
                    return HttpResponseRedirect('/dashboard/')
        else:
                form=LoginForm()
        return render(request, 'blog/login.html', {'form':form})

    else:
        return HttpResponseRedirect('/dashboard/')


#Add new Post
def Add_Post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form=PostForm(request.POST)
            if form.is_valid():
                title=form.cleaned_data['title']
                desc=form.cleaned_data['desc']
                pst=Post(title=title,desc=desc)
                pst.save()
                form=PostForm()
        else:
            form=PostForm()
        return render(request, 'blog/add_post.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

#update Post
def Update_Post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi=Post.objects.get(pk=id)
            form=PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                messages.success(request,'Blog Updated Successfully!!!')
                form=PostForm()
        else:
            pi=Post.objects.get(pk=id)
            form=PostForm(instance=pi)
        return render(request, 'blog/update_post.html',{'form':form})
    else:
          return HttpResponseRedirect('/login/')

def Delete_Post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi=Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post, Category, Profile
from .forms import PostForm, CommentForm, ProfileForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import folium
from ipware import get_client_ip


def split_location_string(post_location):
    coords_list = list(post_location)
    coords_list.reverse()
    return coords_list


def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse(status=200, headers={'HX-Trigger': 'postListChanged'})
        else:
            messages.error(request, 'Username or password does not exist')
    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logout_page(request):
    logout(request)
    return redirect('home')


def register_page(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            profile = Profile()
            profile.user = user
            profile.save()
            login(request, user)
            return HttpResponse(status=204, headers={'HX-Trigger': 'postListChanged'})
        else:
            messages.error(request, 'An error occurred during registration')
    context = {'form': form}
    return render(request, 'base/login_register.html', context)


def home(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    posts = Post.objects.filter(
        Q(category__name__icontains=q) |
        Q(name__icontains=q) |
        Q(poster__username__icontains=q)
    )

    # Needed for live server deployment
    ip, is_routable = get_client_ip(request)

    categories = Category.objects.all()

    comment_form = CommentForm()
    post_form = PostForm()

    maps = {}
    for post in posts:
        m = folium.Map(width=438,
                       height=263,
                       location=split_location_string(post.location),
                       zoom_start=15,
                       tiles='https://tile.thunderforest.com/mobile-atlas/{z}/{x}/{y}.png?apikey=a5928b37b24b4d5fba800722daa1c9aa',
                       attr='s',
                       control_scale=True,
                       attributionControl=False)
        if post.category_id == 1:
            folium.Marker(split_location_string(post.location),
                          popup=
                          f'<img src="media/{post.photo}" style="height: 100px;">'
                          f'<p>{post.name}</p>',
                          icon=folium.Icon(color='blue', icon='university', prefix='fa')).add_to(m)
        if post.category_id == 2:
            folium.Marker(split_location_string(post.location),
                          popup=
                          f'<img src="media/{post.photo}" style="height: 100px;">'
                          f'<p>{post.name}</p>',
                          icon=folium.Icon(color='green', icon='trophy', prefix='fa')).add_to(m)
        if post.category_id == 3:
            folium.Marker(split_location_string(post.location),
                          popup=
                          f'<img src="media/{post.photo}" style="height: 100px;">'
                          f'<p>{post.name}</p>',
                          icon=folium.Icon(color='red', icon='paint-brush', prefix='fa')).add_to(m)

        if post.category_id == 4:
            folium.Marker(split_location_string(post.location),
                          popup=
                          f'<img src="media/{post.photo}" style="height: 100px;">'
                          f'<p>{post.name}</p>',
                          icon=folium.Icon(color='black', icon='lightbulb-o', prefix='fa')).add_to(m)

        m = m._repr_html_()
        maps.update({post.id: m})

    form = PostForm()

    m2 = folium.Map(
        location=[54.68, 25.27],
        zoom_start=12,
        tiles='https://tile.thunderforest.com/mobile-atlas/{z}/{x}/{y}.png?apikey=a5928b37b24b4d5fba800722daa1c9aa',
        attr='s',
        control_scale=True,
        attributionControl=True)
    for post in posts:
        if post.category_id == 1:
            folium.Marker(split_location_string(post.location),
                          popup=
                          f'<img src="media/{post.photo}" style="height: 100px;">'
                          f'<p>{post.name}</p>',
                          icon=folium.Icon(color='blue', icon='university', prefix='fa')).add_to(m2)
        if post.category_id == 2:
            folium.Marker(split_location_string(post.location),
                          popup=
                          f'<img src="media/{post.photo}" style="height: 100px;">'
                          f'<p>{post.name}</p>',
                          icon=folium.Icon(color='green', icon='trophy', prefix='fa')).add_to(m2)
        if post.category_id == 3:
            folium.Marker(split_location_string(post.location),
                          popup=
                          f'<img src="media/{post.photo}" style="height: 100px;">'
                          f'<p>{post.name}</p>',
                          icon=folium.Icon(color='red', icon='paint-brush', prefix='fa')).add_to(m2)

        if post.category_id == 4:
            folium.Marker(split_location_string(post.location),
                          popup=
                          f'<img src="media/{post.photo}" style="height: 100px;">'
                          f'<p>{post.name}</p>',
                          icon=folium.Icon(color='black', icon='lightbulb-o', prefix='fa')).add_to(m2)

    m2 = m2._repr_html_()

    context = {'posts': posts,
               'categories': categories,
               'comment_form': comment_form,
               'post_form': post_form,
               'maps': maps,
               'full_map': m2,
               'ip': ip,
               'form': form}
    return render(request, 'base/home.html', context)


@login_required(login_url='login')
def create_post(request):
    form = PostForm(initial={'poster': request.user})
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'postListChanged'})
    context = {'form': form}
    return render(request, 'base/post_form2.html', context)


@login_required(login_url='login')
def update_post(request, pk):
    post_instance = Post.objects.get(id=pk)
    form = PostForm(instance=post_instance)

    if request.user != post_instance.poster:
        return HttpResponse('Access denied')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post_instance)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'postListChanged'})
    context = {'form': form}
    return render(request, 'base/post_form2.html', context)


@login_required(login_url='login')
def delete_post(request, pk):
    post_instance = Post.objects.get(id=pk)

    if request.user != post_instance.poster:
        return HttpResponse('Access denied')

    if request.method == 'POST':
        post_instance.delete()
        return HttpResponse(headers={'HX-Trigger': 'postListChanged'}, status=204)
    return render(request, 'base/delete.html', {'obj': post_instance})


@login_required(login_url='login')
def create_comment(request, pk):
    form = CommentForm(initial={'post': int(pk), 'user': request.user})
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'postListChanged'})

    context = {'comment_form': form}
    return render(request, 'base/comment_form.html', context)


def like_post(request, pk):
    if request.method == "POST":
        instance = Post.objects.get(id=pk)
        if not instance.likes.filter(id=request.user.id).exists():
            instance.likes.add(request.user)
            instance.save()
            return render(request, 'base/likes_area.html', context={'post': instance})
        else:
            instance.likes.remove(request.user)
            instance.save()
            return render(request, 'base/likes_area.html', context={'post': instance})


def full_map(request):
    posts = Post.objects.all()
    m = folium.Map(
        location=[54.68, 25.27],
        zoom_start=12,
        tiles='https://tile.thunderforest.com/mobile-atlas/{z}/{x}/{y}.png?apikey=a5928b37b24b4d5fba800722daa1c9aa',
        attr='s',
        control_scale=True,
        attributionControl=True)
    for post in posts:
        if post.category_id == 1:
            folium.Marker(split_location_string(post.location),
                          popup=
                          f'<img src="media/{post.photo}" style="height: 100px;">'
                          f'<p>{post.name}</p>',
                          icon=folium.Icon(color='blue', icon='university', prefix='fa')).add_to(m)
        if post.category_id == 2:
            folium.Marker(split_location_string(post.location),
                          popup=
                          f'<img src="media/{post.photo}" style="height: 100px;">'
                          f'<p>{post.name}</p>',
                          icon=folium.Icon(color='green', icon='trophy', prefix='fa')).add_to(m)
        if post.category_id == 3:
            folium.Marker(split_location_string(post.location),
                          popup=
                          f'<img src="media/{post.photo}" style="height: 100px;">'
                          f'<p>{post.name}</p>',
                          icon=folium.Icon(color='red', icon='paint-brush', prefix='fa')).add_to(m)

    m = m._repr_html_()
    return render(request, 'base/full_map.html', {'map': m})


def profile(request, pk):
    posts = Post.objects.filter(poster=pk)
    user = User.objects.filter(id=pk)
    context = {'posts': posts, 'user': user}
    return render(request, 'base/profile.html', context)


def edit_profile(request, pk):
    profile_instance = User.objects.get(id=pk)
    form = ProfileForm(instance=profile_instance)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile_instance)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204)

    context = {'form': form}
    return render(request, 'base/profile_form.html', context)

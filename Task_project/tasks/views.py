from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import TaskForm, ContactForm
from .models import Task, Contact


def home(request):
    """Homepage: carousel + 7 feature cards."""
    slides = [
        {'image': 'tasks/images/slide1.jpg', 'title': 'Welcome to TaskMaster',
         'text': 'The simple way to organize your student life.'},
        {'image': 'tasks/images/slide2.jpg', 'title': 'Organize. Execute. Succeed.',
         'text': 'Register tasks and track them to completion.'},
        {'image': 'tasks/images/slide3.jpg', 'title': 'Your Tasks, Simplified',
         'text': 'Everything you need in one place.'},
    ]

    cards = [
        {'image': 'tasks/images/card1.jpg', 'title': 'Plan Your Day',
         'text': 'Lay out everything you need to get done, in one clear list.'},
        {'image': 'tasks/images/card2.jpg', 'title': 'Stay Organized',
         'text': 'Keep every assignment and deadline in a single place.'},
        {'image': 'tasks/images/card3.jpg', 'title': 'Track Progress',
         'text': 'See exactly what has been registered and what is pending.'},
        {'image': 'tasks/images/card4.jpg', 'title': 'Never Miss a Task',
         'text': 'Register a task once and always find it on the task list.'},
        {'image': 'tasks/images/card5.jpg', 'title': 'Boost Productivity',
         'text': 'Spend less time remembering, more time doing.'},
        {'image': 'tasks/images/card6.jpg', 'title': 'Manage Deadlines',
         'text': 'Add a description to every task so nothing is unclear.'},
        {'image': 'tasks/images/card7.jpg', 'title': 'Achieve Your Goals',
         'text': 'Small consistent steps, tracked well, add up fast.'},
    ]
    return render(request, 'tasks/home.html', {'slides': slides, 'cards': cards})


@login_required
def task_page(request):
    """Task page: register a task with task-name and description."""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task registered successfully!')
            return redirect('task_list')
    else:
        initial = {}
        if request.user.is_authenticated:
            initial['student_name'] = request.user.get_username()
        form = TaskForm(initial=initial)
    return render(request, 'tasks/task_page.html', {'form': form})


def task_list(request):
    """Task-list page: retrieve tasks from the database and display them."""
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def contactviewpage(request):
    """Contact page: submit contact details, save + retrieve on the same page,
    plus 3 pictures and 2 videos."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks! Your message has been received.')
            return redirect('contactviewpage')
    else:
        form = ContactForm()

    contacts = Contact.objects.all()

    gallery_images = [
        'tasks/images/contact1.jpg',
        'tasks/images/contact2.jpg',
        'tasks/images/contact3.jpg',
    ]
    gallery_videos = [
        'tasks/videos/video1.mp4',
        'tasks/videos/video2.mp4',
    ]

    return render(request, 'tasks/contactviewpage.html', {
        'form': form,
        'contacts': contacts,
        'gallery_images': gallery_images,
        'gallery_videos': gallery_videos,
    })

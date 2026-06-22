from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactForm
from .models import Project, Service, Skill


DEFAULT_SERVICES = [
    {'icon': 'UI', 'title': 'Frontend Development', 'short_description': 'Responsive, interactive interfaces using HTML, CSS, JavaScript and React.'},
    {'icon': 'BE', 'title': 'Backend Development', 'short_description': 'Secure Django backends, database design, authentication and admin dashboards.'},
    {'icon': 'API', 'title': 'API Development', 'short_description': 'REST APIs for web and mobile applications with clean, scalable architecture.'},
]
DEFAULT_SKILLS = [
    {'name': 'HTML & CSS', 'percentage': 95},
    {'name': 'JavaScript', 'percentage': 88},
    {'name': 'Python & Django', 'percentage': 90},
    {'name': 'SQL Database', 'percentage': 85},
    {'name': 'React', 'percentage': 82},
]
DEFAULT_PROJECTS = [
    {'title': 'AutoMart Car Buying Website', 'category': 'Django + SQL', 'description': 'A responsive car listing platform with search, category filters and an admin-managed inventory.', 'tech_stack': 'Django, Python, HTML, CSS, SQL'},
    {'title': 'Men\'s Wear E-commerce', 'category': 'React + Frontend', 'description': 'Responsive fashion shop with product cards, category sections and cart features.', 'tech_stack': 'React, JavaScript, CSS'},
    {'title': 'Employee Management System', 'category': 'Django Admin', 'description': 'Employee data management website with records, forms and an easy administration workflow.', 'tech_stack': 'Python, Django, SQLite'},
    {'title': 'Food Selling Website', 'category': 'Full-stack Website', 'description': 'A clean online food catalog interface for browsing products and placing orders.', 'tech_stack': 'HTML, CSS, JavaScript, Django'},
]


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks! Your message has been sent successfully.')
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'portfolio/home.html', {
        'form': form,
        'services': list(Service.objects.all()) or DEFAULT_SERVICES,
        'skills': list(Skill.objects.all()) or DEFAULT_SKILLS,
        'projects': list(Project.objects.all()) or DEFAULT_PROJECTS,
    })

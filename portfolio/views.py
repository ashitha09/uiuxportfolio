from django.shortcuts import render, get_object_or_404
from .models import Project, Contact
from .forms import ContactForm

def home(request):
    featured_projects = Project.objects.all()[:2]  # first 2 projects
    return render(request, 'portfolio/home.html', {'featured_projects': featured_projects})


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})

def about(request):
    return render(request, 'portfolio/about.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # or a 'thank you' page
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})

def jewelry_case_study(request):
    return render(request, 'portfolio/jewelry_case_study.html')

def mindspace_case_study(request):
    return render(request, 'portfolio/mindspace_case_study.html')

def smarthome_case_study(request):
    return render(request, 'portfolio/smarthome_case_study.html')


def gocab_case_study(request):
    return render(request, 'portfolio/gocab_case_study.html')

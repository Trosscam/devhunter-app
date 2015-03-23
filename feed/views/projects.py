# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render
from feed.forms.projects import ProjectForm
from foro.utils.decorators import administrator_required
from feed.models import Project


@administrator_required
def new_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            project = form.save()

    else:
        form = ProjectForm()
    return render(request, 'new_project.html', {'form': form})


def proyectos(request):
	proyectos = Project.objects.all()
	return render(request, 'proyectos.html', {"proyectos":proyectos,})
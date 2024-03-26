from django.shortcuts import render, redirect
from .forms import ElectionForm
from .models import Election
from django.contrib.auth.decorators import login_required


def add_candidate(request):
    template_name = 'elect/add.html'
    form = ElectionForm()
    if request.method == 'POST':
        form = ElectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)


def show_candidate(request):
    template_name = 'elect/show.html'
    votes = Election.objects.all()
    context = {'votes': votes}
    return render(request, template_name, context)


def update_candidate(request, pk):
    template_name = 'elect/add.html'
    obj = Election.objects.get(id=pk)
    form = ElectionForm(instance=obj)
    if request.method == 'POST':
        form = ElectionForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)


def delete_candidate(request, pk):
    obj = Election.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    return render(request, 'elect/confirm.html')

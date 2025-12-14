from django.shortcuts import render, redirect, get_object_or_404
from .models import Sala
from .forms import SalaForm
from django.contrib import messages
from django.db.models import ProtectedError

def sala_list(request):
    salas = Sala.objects.all().order_by('nome')
    return render(request, 'salas/list.html', {'salas': salas})


def sala_create(request):
    form = SalaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('sala_list')

    return render(request, 'salas/form.html', {'form': form})

def sala_edit(request, pk):
    sala = get_object_or_404(Sala, pk=pk)
    form = SalaForm(request.POST or None, instance=sala)

    if form.is_valid():
        form.save()
        return redirect('sala_list')

    return render(request, 'salas/form.html', {'form': form})

def sala_delete(request, pk):
    sala = get_object_or_404(Sala, pk=pk)
    try:
        sala.delete()
        messages.success(request, "Sala deletada com sucesso.")
    except ProtectedError:
        messages.error(request, "Não é possível deletar esta sala porque há alunos associados a ela.")
    return redirect('sala_list')
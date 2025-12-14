from django.shortcuts import render, redirect, get_object_or_404

from salas.models import Sala
from .models import Aluno
from .forms import AlunoForm

def aluno_list(request):
    alunos = Aluno.objects.all()
    salas = Sala.objects.all()

    search = request.GET.get('search')
    sala_id = request.GET.get('sala')
    order = request.GET.get('order') or 'nome'

    if search:
        alunos = alunos.filter(nome__icontains=search)
    if sala_id:
        alunos = alunos.filter(sala_id=sala_id)

    alunos = alunos.order_by(order)

    return render(request, 'alunos/list.html', {
        'alunos': alunos,
        'salas': salas
    })

def aluno_create(request):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('aluno_list')
    return render(request, 'alunos/form.html', {'form': form})

def aluno_edit(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    form = AlunoForm(request.POST or None, instance=aluno)
    if form.is_valid():
        form.save()
        return redirect('aluno_list')
    return render(request, 'alunos/form.html', {'form': form})

def aluno_delete(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    aluno.delete()
    return redirect('aluno_list')
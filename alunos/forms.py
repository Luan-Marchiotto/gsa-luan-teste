from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = ['nome', 'data_nascimento', 'endereco', 'sala']

    def __init__(self, *args, **kwargs):
        # Recebe o objeto aluno que está sendo editado, se houver
        self.instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        # Filtra todos os alunos com o mesmo nome, exceto o que está sendo editado
        qs = Aluno.objects.filter(nome=nome)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Já existe um aluno cadastrado com este nome.")
        return nome
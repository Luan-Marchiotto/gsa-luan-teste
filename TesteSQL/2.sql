--2. Crie um comando SELECT para selecionar apenas os alunos que possuem “Alves” no nome.
SELECT id,
    nome,
    data_nascimento
FROM alunos_aluno
WHERE nome ILIKE '%alves%';

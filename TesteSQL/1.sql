--1. Crie um comando SELECT para selecionar apenas os alunos que estão na sala de aula “A”.

SELECT alunos_aluno.id,
    alunos_aluno.nome,
    alunos_aluno.data_nascimento,
    salas_sala.nome
FROM alunos_aluno
    INNER JOIN salas_sala ON alunos_aluno.sala_id = salas_sala.id
WHERE salas_sala.nome = 'A';
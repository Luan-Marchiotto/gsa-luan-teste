--3. Crie um comando SELECT para selecionar apenas os alunos nascidos antes de 2013.
SELECT id,
    nome,
    data_nascimento
FROM alunos_aluno
WHERE data_nascimento < DATE '2013-01-01'
ORDER BY data_nascimento ASC;

--5. Crie um comando INSERT na tabela de sala de aula com todos os campos da tabela (qualquer valor a sua escolha).

INSERT INTO salas_sala (nome, descricao, data_criacao)
VALUES (
        'C',
        'Sala destinada a novos alunos',
        CURRENT_DATE
    );

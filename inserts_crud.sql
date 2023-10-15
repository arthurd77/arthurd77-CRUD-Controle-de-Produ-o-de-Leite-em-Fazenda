use bubalinocultura;
insert into raca (nome) values 
("carabao"), ("jafarabadi");

insert into lote (ocupacao, metros_quadrados, quantidade_bubalinos) values 
("leite", 15.000, 30), ("carne", 14.000, 45), ("leite", 11.000, 11), ("leite", 12.000, 11), ("carne", 14.000, 45);

INSERT INTO bubalino (codigo_animal, data_nascimento, status_vacinacao, peso_Nascimento, raca_cod_raca, lote_cod_lote, status)
VALUES
(1, '2022-01-10', 'pendente', 25.5, 1, 2, 'abatido'),
(2, '2021-11-15', 'vacinado', 22.0, 2, 1, 'vivo'),
(3, '2022-03-05', 'vacinado', 28.3, 1, 2, 'vivo'),
(4, '2022-02-20', 'pendente', 24.8, 2, 1, 'abatido'),
(5, '2022-04-12', 'vacinado', 26.1, 1, 1, 'vivo'),
(6, '2022-03-30', 'pendente', 23.7, 2, 1, 'vivo'),
(7, '2021-12-18', 'vacinado', 27.2, 1, 2, 'vivo');

INSERT INTO cargo (nome) values 
("Veterinario"), ("Ordenador"), ("Abatedor");

INSERT INTO funcionario (cpf, nome, status, cargo_codigo)
VALUES
(12345678901, 'João Silva', 'ativo', 1),
(23456789012, 'Maria Souza', 'ativo', 2),
(34567890123, 'Pedro Santos', 'inativo', 1),
(45678901234, 'Ana Oliveira', 'ativo', 3),
(56789012345, 'Luiz Pereira', 'ativo', 2),
(67890123456, 'Julia Rodrigues', 'inativo', 1),
(78901234567, 'Marcos Alves', 'ativo', 3);

INSERT INTO producao_carne (data_abatimento, qualidade_da_carne, quantidade_kilos, lote_cod_lote, bubalino_codigo_animal)
VALUES
('2023-09-14', 'consumível', 198.6, 1, 7),
('2023-09-15', 'consumível', 210.3, 2, 6),
('2023-09-16', 'inconsumível', 190.7, 1, 5),
('2023-09-17', 'consumível', 220.0, 2, 4),
('2023-09-18', 'consumível', 180.8, 1, 3),
('2023-09-19', 'inconsumível', 150.2, 2, 2),
('2023-09-20', 'consumível', 200.5, 1, 1);

INSERT INTO producao_leite (data_coletada, qualidade_do_leite, quantidade_litros, lote_cod_lote, bubalino_codigo_animal)
VALUES
('2023-09-14', 'boa', 18.1, 1, 7),
('2023-09-15', 'inconsumível', 10.7, 2, 6),
('2023-09-16', 'boa', 17.3, 1, 5),
('2023-09-17', 'boa', 16.8, 2, 4),
('2023-09-18', 'inconsumível', 12.0, 1, 3),
('2023-09-19', 'boa', 14.5, 2, 2),
('2023-09-20', 'boa', 15.2, 1, 1);

INSERT INTO vacina (nome, lote_vacina, data_validade) values 
('Febre aftosa ', 122332, '2025-02-21'),
('Leptospirose', 233445, '2024-02-21'),
('Brucelose', 333223, '2023-12-21'),
('raiva', 3333332, '2025-02-21');

INSERT INTO vacinacao (data_vacinacao, vacina_cod_vacina, bubalino_cod_animal, funcionario_cpf)
VALUES
('2023-09-14', 4, 7, 34567890123),
('2023-09-15', 3, 6, 23456789012),
('2023-09-16', 2, 5, 23456789012),
('2023-09-16', 2, 5, 34567890123),
('2023-09-17', 1, 4, 23456789012),
('2023-09-18', 3, 3, 12345678901),
('2023-09-18', 3, 3, 23456789012),
('2023-09-19', 2, 2, 12345678901),
('2023-09-20', 1, 1, 12345678901);

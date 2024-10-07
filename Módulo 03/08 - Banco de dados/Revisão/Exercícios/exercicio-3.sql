CREATE DATABASE exercicio3;


CREATE TABLE sexo (
	cdSexo INTEGER PRIMARY KEY,
	dsSexo VARCHAR(10)
);


CREATE TABLE porte (
	cdPorte INTEGER PRIMARY KEY,
	dsPorte VARCHAR(50)
);


CREATE TABLE servico (
	cdServico INTEGER PRIMARY KEY,
	dsServico VARCHAR(100),
	vlServico INTEGER
);


CREATE TABLE atendente (
	cdAtendente INTEGER PRIMARY KEY,
	nmAtendente VARCHAR(100),
	hrDispInicio TIME,
	hrDispFinal TIME
);


CREATE TABLE disponibilidadeagendamento (
	cdAgendamento INTEGER PRIMARY KEY,
	hrDispInicial TIME,
	hrDispFinal TIME
);


CREATE TABLE cliente (
	cdCliente INTEGER PRIMARY KEY,
	Sexo_cdSexo INTEGER,
	dsNome VARCHAR(100),
	dsSobrenome VARCHAR(100),
	dsRua VARCHAR(100),
	dsBairro VARCHAR(100),
	nrCasa INTEGER,
	nrCep INTEGER,
	dsCidade VARCHAR(50),
	nrTelefone VARCHAR(20),
	nrCelular VARCHAR(20),
	nrIdade INTEGER,
	idAdmin BOOLEAN,
	dsEmail VARCHAR(100),
	dsUsuario VARCHAR(50),
	dsSenha VARCHAR(50),
	FOREIGN KEY (Sexo_cdSexo) REFERENCES Sexo(cdSexo)
);


CREATE TABLE animal (
	cdAnimal INTEGER PRIMARY KEY,
	Porte_cdPorte INTEGER,
	Sexo_cdSexo INTEGER,
	Cliente_cdCliente INTEGER,
	dsNome VARCHAR(100),
	dsRaca VARCHAR(50),
	dtNascimento DATE,
	dsCorPelagem VARCHAR(50),
	FOREIGN KEY (Porte_cdPorte) REFERENCES Porte(cdPorte),
	FOREIGN KEY (Sexo_cdSexo) REFERENCES Sexo(cdSexo),
	FOREIGN KEY (Cliente_cdCliente) REFERENCES Cliente(cdCliente)
);


CREATE TABLE agendamento (
	cdAgendamento INTEGER PRIMARY KEY,
	Animal_cdAnimal INTEGER,
	Servico_cdServico INTEGER,
	Atendente_cdAtendente INTEGER,
	dtAgendamento DATE,
	hrAgenInicial TIME,
	hrAgenFinal TIME,
	idAprovado BOOLEAN,
	FOREIGN KEY (Animal_cdAnimal) REFERENCES Animal(cdAnimal),
	FOREIGN KEY (Servico_cdServico) REFERENCES Servico(cdServico),
	FOREIGN KEY (Atendente_cdAtendente) REFERENCES Atendente(cdAtendente)
);


INSERT INTO sexo (cdSexo, dsSexo)
VALUES 
(1, 'Masculino'),
(2, 'Feminino');


INSERT INTO porte (cdPorte, dsPorte)
VALUES 
(1, 'Pequeno'),
(2, 'Médio'),
(3, 'Grande');


INSERT INTO servico (cdServico, dsServico, vlServico)
VALUES 
(1, 'Banho', 50),
(2, 'Tosa', 70);

INSERT INTO atendente (cdAtendente, nmAtendente, hrDispInicio, hrDispFinal)
VALUES 
(1, 'João Silva', '07:00', '16:00');


INSERT INTO disponibilidadeagendamento (cdAgendamento, hrDispInicial, hrDispFinal)
VALUES 
(1, '08:00:00', '12:00:00');


INSERT INTO cliente (cdCliente, Sexo_cdSexo, dsNome, dsSobrenome, dsRua, dsBairro, nrCasa, nrCep, dsCidade, nrTelefone, nrCelular, nrIdade, idAdmin, dsEmail, dsUsuario, dsSenha)
VALUES 
(2, 2, 'Ana', 'Moura', 'R. Boa Hora', 'Jardins', 456, 87654321, 'Rio de Janeiro', '1144556677', '21987654321', 25, 1, 'ana.moura@email.com', 'ana_m', 'senha456');


INSERT INTO animal (cdAnimal, Porte_cdPorte, Sexo_cdSexo, Cliente_cdCliente, dsNome, dsRaca, dtNascimento, dsCorPelagem)
VALUES 
(1, 1, 1, 1, 'Ruffos', 'Bulldog', '2020-05-10', 'Branco');



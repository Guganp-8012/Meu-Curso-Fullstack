CREATE DATABASE exercicio1;


CREATE TABLE FARMACIA (
	CNPJ_farmacia VARCHAR(14) PRIMARY KEY,
	tel_farmacia VARCHAR(15) NULL,
	nome_farmacia VARCHAR(100) NOT NULL,
	end_farmacia VARCHAR(255) NULL
);


CREATE TABLE FARMACEUTICO (
	RG_farmaceutico VARCHAR(9) PRIMARY KEY,
	nome_farmaceutico VARCHAR(100) NOT NULL,
	CNPJ_farmacia VARCHAR(14),
	FOREIGN KEY (CNPJ_farmacia) REFERENCES FARMACIA(CNPJ_farmacia) ON DELETE CASCADE
);


CREATE TABLE PRODUTO (
  cod_produto INTEGER PRIMARY KEY,
  qtd_produto INTEGER NOT NULL,
  valor_produto DECIMAL(10, 2) NOT NULL,
  CNPJ_farmacia VARCHAR(14),
  FOREIGN KEY (CNPJ_farmacia) REFERENCES FARMACIA(CNPJ_farmacia)
);


INSERT INTO farmacia (CNPJ_farmacia, tel_farmacia, nome_farmacia, end_farmacia) VALUES ('09876543210987', '869812335265', 'Farmabom', 'R.Seu Jorge, 175 - Floresta');


INSERT INTO farmaceutico (RG_farmaceutico, nome_farmaceutico, CNPJ_farmacia) VALUES ('123456789', 'Robson', '09876543210987');


INSERT INTO produto (cod_produto, qtd_produto, valor_produto, CNPJ_farmacia) VALUES ('45672392', '2', '22.90', '09876543210987');
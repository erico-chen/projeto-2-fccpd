# Projeto 2 - Fundamentos de Computação Concorrente, Paralela e Distribuída

Este repositório é composto por 5 desafios desenvolvidos para a disciplina FCCPD – Fundamentos de Computação em Cloud e Processamento Distribuído.
Cada desafio explora conceitos essenciais de ambientes distribuídos, virtualização, containers, redes e comunicação entre serviços, utilizando ferramentas modernas como Docker, Python e arquiteturas simples de microsserviços.

Os desafios foram estruturados de forma progressiva, permitindo que cada etapa consolide os conhecimentos fundamentais antes de avançar para cenários mais complexos. Eles estão organizados em dois blocos principais:

## 🐳 Desafios com Docker (3 desafios)

Esses desafios introduzem os conceitos essenciais de conteinerização, comunicação entre containers, armazenamento persistente e orquestração de múltiplos serviços.

Desafio 1 — Containers em Rede
Comunicação entre serviços isolados através de uma rede Docker customizada.

Desafio 2 — Volumes e Persistência
Utilização de volumes Docker para manter dados mesmo após reinicialização dos containers.

Desafio 3 — Docker Compose Orquestrando Serviços
Estruturação de múltiplos containers, redes e dependências usando Docker Compose.

## 🕸️ Desafios com Microsserviços (2 desafios)

Nesta etapa, os desafios expandem os conceitos de distribuição com foco em arquitetura, independência entre serviços e roteamento via API Gateway.

Desafio 4 — Microsserviços Independentes
Construção de serviços isolados, cada um responsável por uma função específica.

Desafio 5 — Microsserviços com API Gateway
Integração dos microsserviços por meio de um gateway central, responsável por roteamento, padronização e unificação da comunicação.

## 📁 Estrutura do Projeto

```
.
├── desafio1
├── desafio2
├── desafio3
├── desafio4
└── desafio5
```


## Como executar o projeto
### 1. Clone o repositório
``` bash
git clone https://github.com/erico-chen/projeto-2-fccpd.git
```

### 2. Escolha o Desafio
<details closed>
<summary>Desafio 1</summary>
<br>

## 🛠️ Execução do Desafio
### 2.1.1 Vá para o diretório do desafio
``` bash
cd desafio1
```
### 2.1.2 Crie a rede Docker
``` bash
docker network create [SEU_NOME_REDE]
```

### 2.1.3 Faça o build das imagens
``` bash
docker build -t [SUA_TAG_IMAGEM] -f Dockerfile.server .
docker build -t [SUA_TAG_IMAGEM] -f Dockerfile.client .
```

### 2.1.4 Rode o Servidor
``` bash
docker run -d --name [SEU_NOME_CONTAINER_SERVIDOR] --network [SEU_NOME_REDE] -p 8080:8080 [SUA_TAG_IMAGEM]
```

### 2.1.5 Rode o Cliente
``` bash
docker run -d --name [SEU_NOME_CONTAINER_CLIENTE] --network [SEU_NOME_REDE] [SUA_TAG_IMAGEM]
```

### 2.1.6 Visualize os logs dos Containers
``` bash
docker logs -f [SEU_NOME_CONTAINER_CLIENTE]
docker logs -f [SEU_NOME_CONTAINER_SERVIDOR]
```

### 2.1.7 Verifique os Containers conectados a rede criada
``` bash
docker network inspect [SEU_NOME_REDE]
```

### 2.1.8 Resultados Esperados:
<br>
<img width="1319" alt="containers-logs" src="https://github.com/user-attachments/assets/3b84fa1b-c28d-4460-b063-0a066871d812">
<br>
<img width="1319" alt="rede-inspecionado" src="https://github.com/user-attachments/assets/410742fa-d78f-4f96-9578-3a457e2ff9f3">
<br>
</details>

<details closed>
<summary>Desafio 2</summary>
<br>

## 🛠️ Execução do Desafio
### 2.2.1 Crie um volume Docker
``` bash
docker volume create [SEU_NOME_VOLUME]
```
### 2.2.2 Suba um container PostgreSQL usando o volume
``` bash
docker run -d --name [SEU_NOME_CONTAINER] -e POSTGRES_USER=[SEU_USUARIO] -e POSTGRES_PASSWORD=[SUA_SENHA] -e POSTGRES_DB=[SEU_NOME_BD] -v desafio2_pgdata:/var/lib/postgresql/data -p 5432:5432 postgres:16
```

### 2.2.3 Conecte-se ao banco
``` bash
docker exec -it [SEU_NOME_CONTAINER] psql -U [SEU_USUARIO] -d [SEU_NOME_BD]
```

### 2.2.4 Crie dados
Crie a tabela "Clientes"
``` bash
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    criado_em TIMESTAMP DEFAULT NOW()
);
```
Insira linhas na tabela
``` bash
INSERT INTO clientes (nome) VALUES
('Ana'),
('Bruno'),
('Carla');
```
Visualize as linhas da tabela
``` bash
SELECT * FROM clientes;
```

### 2.2.5 Saia do psql
``` bash
\q
```

### 2.2.6 Remova o container
``` bash
docker rm -f [SEU_NOME_CONTAINER]
```

### 2.2.7 Suba um novo container usando o mesmo volume
``` bash
docker run -d --name [SEU_NOME_CONTAINER] -e POSTGRES_USER=[SEU_USUARIO] -e POSTGRES_PASSWORD=[SUA_SENHA] -e POSTGRES_DB=[SEU_NOME_BD] -v desafio2_pgdata:/var/lib/postgresql/data -p 5432:5432 postgres:16
```

### 2.2.8 Comprove a persistência dos dados
Conecte-se ao banco novamente
``` bash
docker exec -it [SEU_NOME_CONTAINER] psql -U [SEU_USUARIO] -d [SEU_NOME_BD]
```
Visualize as linhas da tabela
``` bash
SELECT * FROM clientes;
```
Você deverá ver os mesmos registros.

### 2.2.9 Resultados Esperados:
<br>
<img width="1319" alt="desafio2-print-1" src="https://github.com/user-attachments/assets/2c29af4b-73b5-4ca9-a4c6-378330739f09">
<br>
<img width="1319" alt="desafio2-print-2" src="https://github.com/user-attachments/assets/19410d20-cc16-4ce0-823a-d1c957191312">
<br>

</details>

<details closed>
<summary>Desafio 3</summary>
<br>
    
## 🧱 Arquitetura proposta (web + db + cache)

Serviços:

- Web: aplicação Flask em Python.

    - Lê/escreve no PostgreSQL.

    - Usa Redis como cache simples.

- DB: PostgreSQL.

- Cache: Redis.

Comunicação:

- A web fala com db via postgresql://…@db:5432/...

- A web fala com cache via redis://cache:6379/0

- Tudo em uma rede interna criada automaticamente pelo docker-compose.


## 🛠️ Execução do Desafio
### 2.3.1 Vá para o diretório do desafio
``` bash
cd desafio3
```
### 2.3.2 Suba os containers com Docker Compose
``` bash
docker compose up --build
```

</details>



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
Este desafio demonstra como dois containers Docker podem se comunicar entre si através de uma rede customizada.
A ideia principal é simular dois serviços independentes:

- Servidor (service A): expõe uma rota HTTP simples usando Python/Flask.

- Cliente (service B): executa periodicamente requisições HTTP para o servidor usando requests.

Ambos os serviços são colocados dentro da mesma rede Docker, o que permite ao cliente acessar o servidor pelo nome do container (ex.: http://server:8080).
Isso mostra que, dentro de uma rede Docker, os containers funcionam como se estivessem em uma “LAN privada”, com DNS interno e isolamento do host.
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
Este desafio demonstra persistência de dados no Docker usando volumes.
A proposta é executar um container PostgreSQL e armazenar seus dados em um volume chamado desafio2_db.

Dessa forma:

- Mesmo que o container seja removido (docker rm),

- Mesmo que você suba outro container novo,

- Mesmo que atualize a imagem,

os dados continuam existindo, porque o volume está fora do ciclo de vida do container.
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
Isso irá subir:

- desafio3_db (PostgreSQL)

- desafio3_cache (Redis)

- desafio3_web (Flask)

A aplicação web ficará disponível em:
```
http://localhost:8080
```
### 2.3.3 Inicialize o Banco de Dados
Acesse: 
```
http://localhost:8080/init-db
```
Isso cria a tabela acessos no banco desafio_3_db.

### 2.3.4 Teste a comunicação com o Banco de Dados
Acesse: 
```
http://localhost:8080/db
```
Cada chamada:

- Insere um registro em acessos.
- Retorna o total de registros (comprova que a web está falando com o db).

### 2.3.5 Teste a comunicação com o Cache (Redis)
Acesse: 
```
http://localhost:8080/cache
```
Cada chamada:

- Incrementa a chave contador_acessos no Redis.
- Retorna o valor atual (comprova que a web está falando com o cache).

### 2.3.6 Encerre os serviços
```
docker compose down
```
</details>

<details closed>
<summary>Desafio 4</summary>
<br>
    
## 🧱 Arquitetura da Solução

A solução foi dividida em dois microsserviços escritos em Python + Flask:

### Microsserviço A — Provedor de Dados
- Expõe um endpoint HTTP que retorna uma lista de usuários em formato JSON.

- É responsável por fornecer a “base de dados” que o serviço B irá consumir.

- Porta interna: 5008

- Porta exposta no host: 5010 → 5008

### Microsserviço B — Consumidor / Agregador

- Faz requisições HTTP para o serviço A usando seu nome DNS dentro da rede Docker.

- Processa as informações recebidas e retorna mensagens combinadas:

        “Usuário X ativo desde Y”

- Porta: 5001

### Comunicação:

A comunicação entre serviços ocorre na rede interna do Docker Compose:
```
service_b → http://servico_a:5008/users
```

### Cada microsserviço possui:

- Seu próprio código

- Seu próprio Dockerfile

- Suas dependências isoladas

## Detalhes de Implementação

### Microsserviço A
Retorna a lista de usuários:

<b>Endpoint</b>:
```
GET /users
```

<b>Saída esperada</b>:
```
[
  {"id": 1, "nome": "Gabi", "ativo_desde": "2021-01-01"},
  {"id": 2, "nome": "Jorge", "ativo_desde": "2022-03-15"},
  {"id": 3, "nome": "Saulo", "ativo_desde": "2023-07-10"}
]
```

### Microsserviço B
Consome o Servico A por HTTP usando o nome do container:

```
http://servico_a:5008/users
```

<b>Endpoint</b>:
```
GET /users-detalhado
```

<b>Saída esperada</b>:
```
{
  "origem": "service-b",
  "mensagens": [
    "Usuário Ana ativo desde 2021-01-01",
    "Usuário Bruno ativo desde 2022-03-15",
    "Usuário Carla ativo desde 2023-07-10"
  ]
}
```

## 🛠️ Execução do Desafio
### 2.4.1 Vá para o diretório do desafio
``` bash
cd desafio4
```
### 2.4.2 Suba os containers com Docker Compose
``` bash
docker compose up --build
```

### 2.4.3 Teste Microsserviço A
Acesse: 
```
http://localhost:5010/users
```

### 2.4.4 Teste Microsserviço B
Acesse: 
```
http://localhost:5001/users-detalhado
```

### 2.4.5 Encerre os serviços
```
docker compose down
```
</details>

</details>

<details closed>
<summary>Desafio 5</summary>
<br>

## Objetivo

Implementar uma arquitetura de microsserviços onde **uma API Gateway atua como ponto único de entrada**, roteando requisições para **dois serviços internos**:

- `tenista-service`: lista tenistas.
- `premiacao-service`: lista as premiações associadas a tenistas.

## 🧱 Arquitetura da Solução

A arquitetura é composta por **3 serviços**:

### 1. API Gateway (`api-gateway`)
- Único serviço exposto externamente.
- Porta exposta no host: `8080`.
- Responsável por receber as requisições do cliente e encaminhar para os microsserviços internos.
- Endpoints externos:
  - `GET /tenistas` → encaminha para `tenista-service`.
  - `GET /premiacoes` → encaminha para `premiacao-service`.

### 2. Microsserviço de Tenistas (`tenista-service`)
- Porta interna: `5001`.
- Não é exposto diretamente ao host, apenas para a rede interna do Docker.
- Endpoint interno:
  - `GET /tenistas` → retorna a lista de tenistas em JSON.

### 3. Microsserviço de Premiações (`premiacao-service`)
- Porta interna: `5002`.
- Também não é exposto diretamente ao host.
- Endpoint interno:
  - `GET /premiacoes` → retorna a lista de premiações em JSON.


### Comunicação na rede interna

Todos os serviços estão na mesma rede Docker (`desafio5_net`).  
Dentro dessa rede, o gateway acessa os serviços pelos **nomes dos containers**:

- `http://tenista-service:5001/tenistas`
- `http://premiacao-service:5002/premiacoes`

Do ponto de vista do cliente externo, porém, **apenas o gateway é acessível**:

- `http://localhost:8080/tenistas`
- `http://localhost:8080/premiacoes`

Isso garante o **gateway como ponto único de entrada**.

### Cada microsserviço possui:

- Código-fonte isolado (um arquivo Python com Flask).

- Um Dockerfile próprio, com suas dependências.

- Configuração de rede feita pelo docker-compose.yml.

## Integração entre os Serviços

### Tenista-service
Responde com uma lista de tenistas:

<b>Endpoint</b>:
```
GET /tenistas
```

<b>Saída esperada</b>:
```
[
  { "id": 1, "nome": "Rafael Nadal", "virou_profissional": "2001" },
  { "id": 2, "nome": "Roger Federer", "virou_profissional": "1998" }
]

```

### Premiacao-service
Responde com uma lista de premiações:

<b>Endpoint</b>:
```
GET /premiacoes
```

<b>Saída esperada</b>:
```
[
    {"id": 101, "tenista_id": 1, "premiacao_carreira": 112500000},
    {"id": 102, "tenista_id": 2, "premiacao_carreira": 108800000},
]
```
- O api-gateway integra esses serviços ao expor endpoints externos:

    - /tenistas → proxy direto para a lista de tenistas.

    - /premiacoes → proxy direto para a lista de premiações.
## 🛠️ Execução do Desafio
### 2.5.1 Vá para o diretório do desafio
``` bash
cd desafio5
```
### 2.5.2 Suba os containers com Docker Compose
``` bash
docker compose up --build
```

### 2.5.3 Liste tenistas (via gateway)
Acesse: 
```
http://localhost:8080/tenistas
```

### 2.5.4 Liste premiações (via gateway)
Acesse: 
```
http://localhost:8080/premiacoes
```

### 2.5.5 Encerre os serviços
```
docker compose down
```
</details>


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
### 2.1 Vá para o diretório do desafio
``` bash
cd desafio1
```
### 2.2 Crie a rede Docker
``` bash
docker network create [SEU_NOME_REDE]
```

### 2.3 Faça o build das imagens
``` bash
docker build -t [SUA_TAG_IMAGEM] -f Dockerfile.server .
docker build -t [SUA_TAG_IMAGEM] -f Dockerfile.client .
```

### 2.4 Rode o Servidor
``` bash
docker run -d --name [SEU_NOME_CONTAINER_SERVIDOR] --network [SEU_NOME_REDE] -p 8080:8080 [SUA_TAG_IMAGEM]
```

### 2.5 Rode o Cliente
``` bash
docker run -d --name [SEU_NOME_CONTAINER_CLIENTE] --network [SEU_NOME_REDE] [SUA_TAG_IMAGEM]
```

### 2.6 Visualize os logs dos Containers
``` bash
docker logs -f [SEU_NOME_CONTAINER_CLIENTE]
docker logs -f [SEU_NOME_CONTAINER_SERVIDOR]
```

### 2.7 Verifique os Containers conectados a rede criada
``` bash
docker network inspect [SEU_NOME_REDE]
```

### 2.8 Resultados Esperados:
<br>
<img width="1319" alt="containers-logs" src="https://github.com/user-attachments/assets/3b84fa1b-c28d-4460-b063-0a066871d812">
<br>
<img width="1319" alt="rede-inspecionado" src="https://github.com/user-attachments/assets/410742fa-d78f-4f96-9578-3a457e2ff9f3">
<br>

</details>




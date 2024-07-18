```markdown
# Calculadora Simples

Este é um projeto de uma calculadora simples em Python, que utiliza o Docker para facilitar a execução em diferentes ambientes.

## Requisitos

- Docker
- Docker Compose

## Como usar

### Passo 1: Clonar o repositório

Clone este repositório para o seu ambiente local:

```bash
git clone https://github.com/eduardopetrocchi/container_calculadora
cd container_calculadora
```

### Passo 2: Construir e executar o contêiner

Use o Docker Compose para construir e executar o contêiner:

```bash
docker-compose up
```

### Estrutura do projeto

```
.
├── calculadora.py
├── docker-compose.yml
└── Dockerfile
```

### calculadora.py

Este é o script principal que contém a lógica da calculadora. A calculadora aceita operações básicas como adição, subtração, multiplicação e divisão.

### Dockerfile

O Dockerfile define a imagem Docker para a calculadora. Ele usa a imagem base do Ubuntu e instala o Python 3.

### docker-compose.yml

O arquivo docker-compose.yml define o serviço da calculadora e como ele deve ser executado.

## Licença

Este projeto está licenciado sob a Licença MIT.
```

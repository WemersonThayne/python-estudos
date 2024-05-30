# Gerenciador de Tarefas

## Visão Geral

O sistema Gerenciador de Tarefas será uma aplicação backend desenvolvida em Python, destinada a permitir que os usuários possam gerenciar suas tarefas diárias de maneira eficiente. A aplicação deve possibilitar a criação, leitura, atualização e exclusão de tarefas, além de permitir a categorização e priorização das mesmas. Este documento descreve as funcionalidades requeridas para o sistema, sem incluir o desenvolvimento da interface frontend.

## Funcionalidades Principais

### 1. Autenticação e Autorização
- **Cadastro de Usuário**: Permitir que novos usuários se registrem no sistema.
- **Login de Usuário**: Permitir que os usuários registrados façam login no sistema.
- **Autenticação por Token**: Usar tokens JWT (JSON Web Tokens) para autenticar e autorizar usuários em cada requisição.

### 2. Gerenciamento de Tarefas
- **Criar Tarefa**: Permitir que o usuário crie novas tarefas com os seguintes atributos:
  - Título (obrigatório)
  - Descrição (opcional)
  - Data de vencimento (opcional)
  - Prioridade (baixa, média, alta)
  - Categoria (opcional)
  - Status (obrigatório)
- **Visualizar Tarefas**: Permitir que o usuário visualize todas as suas tarefas ou filtre por:
  - Data de vencimento
  - Prioridade
  - Categoria
  - Status
- **Atualizar Tarefa**: Permitir que o usuário atualize os detalhes de uma tarefa existente.
- **Excluir Tarefa**: Permitir que o usuário exclua uma tarefa existente.

### 3. Gerenciamento de Categorias
- **Criar Categoria**: Permitir que o usuário crie novas categorias para organizar suas tarefas.
- **Listar Categorias**: Permitir que o usuário visualize todas as categorias criadas.
- **Atualizar Categoria**: Permitir que o usuário atualize os detalhes de uma categoria existente.
- **Excluir Categoria**: Permitir que o usuário exclua uma categoria existente, com a opção de mover as tarefas para outra categoria ou deixá-las sem categoria.

### 4. Configurações de Usuário
- **Atualizar Perfil**: Permitir que o usuário atualize suas informações pessoais, como nome e email.
- **Alterar Senha**: Permitir que o usuário altere sua senha.
- **Recuperação de Senha**: Permitir que o usuário recupere sua senha através de email.

## Requisitos Não Funcionais

### 1. Segurança
- Armazenar senhas de forma segura utilizando hashing.
- Proteger endpoints com autenticação JWT.

### 2. Desempenho
- O sistema deve ser capaz de lidar com múltiplas requisições simultâneas de forma eficiente.

### 3. Escalabilidade
- O sistema deve ser projetado de forma a permitir fácil escalabilidade para atender a um número crescente de usuários.

### 4. Documentação
- Fornecer documentação clara e detalhada da API, utilizando ferramentas como Swagger ou Postman.

## Estrutura de Dados

### Tabela de Usuários
- `id`: Identificador único
- `nome`: Nome do usuário
- `email`: Email do usuário (único)
- `senha_hash`: Hash da senha do usuário
- `data_criacao`: Data de criação do usuário

### Tabela de Tarefas
- `id`: Identificador único
- `titulo`: Título da tarefa
- `descricao`: Descrição da tarefa
- `status`: Status da tarefa
- `data_vencimento`: Data de vencimento da tarefa
- `prioridade`: Prioridade da tarefa (baixa, média, alta)
- `categoria_id`: ID da categoria associada (pode ser nulo)
- `usuario_id`: ID do usuário proprietário da tarefa
- `data_criacao`: Data de criação da tarefa
- `data_atualizacao`: Data da última atualização da tarefa

### Tabela de Categorias
- `id`: Identificador único
- `nome`: Nome da categoria
- `descricao`: Descrição da categoria (opcional)
- `data_criacao`: Data de criação da categoria

## Endpoints da API

### Autenticação
- `POST /register`: Registrar um novo usuário
- `POST /login`: Autenticar um usuário e fornecer um token JWT
- `POST /logout`: Invalidar o token JWT

### Tarefas
- `GET /tasks`: Listar todas as tarefas do usuário
- `POST /tasks`: Criar uma nova tarefa
- `GET /tasks/{id}`: Obter detalhes de uma tarefa específica
- `PUT /tasks/{id}`: Atualizar uma tarefa existente
- `DELETE /tasks/{id}`: Excluir uma tarefa

### Categorias
- `GET /categories`: Listar todas as categorias do usuário
- `POST /categories`: Criar uma nova categoria
- `GET /categories/{id}`: Obter detalhes de uma categoria específica
- `PUT /categories/{id}`: Atualizar uma categoria existente
- `DELETE /categories/{id}`: Excluir uma categoria

### Usuários
- `GET /user/profile`: Obter detalhes do perfil do usuário
- `PUT /user/profile`: Atualizar perfil do usuário
- `POST /user/change-password`: Alterar senha do usuário
- `POST /user/recover-password`: Recuperar senha do usuário

## Tecnologias e Ferramentas

### Backend
- **Linguagem**: Python
- **Framework**: Flask ou Django
- **Autenticação**: JWT (JSON Web Tokens)
- **Banco de Dados**: PostgreSQL ou MySQL
- **ORM**: SQLAlchemy (para Flask) ou Django ORM (para Django)
- **Documentação da API**: Swagger ou Postman

## Conclusão

Esta especificação funcional define os requisitos e funcionalidades do sistema Gerenciador de Tarefas, que será desenvolvido utilizando Python como linguagem de backend. O sistema proporcionará aos usuários uma maneira eficiente de gerenciar suas tarefas diárias, com recursos de autenticação segura, categorização de tarefas e gerenciamento de perfis de usuário.
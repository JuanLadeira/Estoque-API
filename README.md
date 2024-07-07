Estoque API
# Projeto de estoque

## License: MIT

### Settings
Moved to settings.

## Modelo / Model

## Pré-requisitos / Prerequisites
- Docker
- bash

## Comandos Básicos / Basic Commands

### Configurando seus usuários / Setting Up Your Users
Para criar uma conta de usuário normal, vá para Sign Up e preencha o formulário. Após enviar, você verá uma página "Verify Your E-mail Address". Vá ao seu console para ver uma mensagem de verificação simulada por e-mail. Copie o link para o seu navegador. Agora o e-mail do usuário deve estar verificado e pronto para uso.

To create a normal user account, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

Para criar uma conta de superusuário, use este comando:

```bash
$ task createsuperuser
```

To create a superuser account, use this command:

```bash
$ task createsuperuser
```

Para conveniência, você pode manter seu usuário normal logado no Chrome e seu superusuário logado no Firefox (ou similar), para que você possa ver como o site se comporta para ambos os tipos de usuários.

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Verificação de Tipos / Type Checks
Executando verificações de tipo com mypy:

```bash
$ mypy estoque_api
```

Running type checks with mypy:

```bash
$ mypy estoque_api
```

### Cobertura de Testes / Test Coverage
Para rodar os testes, verificar a cobertura dos testes e gerar um relatório HTML de cobertura:

```shell
$ task test
$ coverage html
$ open htmlcov/index.html
```

To run the tests, check your test coverage, and generate an HTML coverage report:

```shell
$ task test
$ coverage html
$ open htmlcov/index.html
```

## Celery
Esta aplicação vem com o Celery.

Para rodar um worker do Celery:

```bash
cd estoque_api
celery -A config.celery_app worker -l info
```

To run a celery worker:

```bash
cd estoque_api
celery -A config.celery_app worker -l info
```

Para executar tarefas periódicas, você precisará iniciar o serviço de agendamento do celery beat. Você pode iniciá-lo como um processo independente:

To run periodic tasks, you'll need to start the celery beat scheduler service. You can start it as a standalone process:

```bash
cd estoque_api
celery -A config.celery_app beat
```

ou você pode embutir o serviço beat dentro de um worker com a opção -B (não recomendado para uso em produção):

or you can embed the beat service inside a worker with the -B option (not recommended for production use):

```bash
cd estoque_api
celery -A config.celery_app worker -B -l info
```

## Servidor de Email / Email Server
No desenvolvimento, muitas vezes é útil ver os e-mails que estão sendo enviados pela sua aplicação. Por esse motivo, o servidor SMTP local Mailpit com uma interface web está disponível como contêiner Docker.

O contêiner mailpit será iniciado automaticamente quando você executar todos os contêineres docker. Por favor, verifique a documentação Docker do cookiecutter-django para mais detalhes sobre como iniciar todos os contêineres.

Container mailpit will start automatically when you will run all docker containers. Please check cookiecutter-django Docker documentation for more details how to start all containers.

Com o Mailpit em execução, para visualizar as mensagens enviadas pela sua aplicação, abra seu navegador e vá para [http://127.0.0.1:8025](http://127.0.0.1:8025)

With Mailpit running, to view messages that are sent by your application, open your browser and go to [http://127.0.0.1:8025](http://127.0.0.1:8025)

## Tarefas do bash / bash Tasks
Com Docker e bash instalados, você pode usar os seguintes comandos:

With Docker and bash installed, you can use the following commands:

- Construir a aplicação / Build the application:

```bash
task build
```

- Iniciar a aplicação / Start the application:

```bash
task up
```

- Parar a aplicação / Stop the application:

```bash
task down
```

- Abrir um shell no contêiner Django / Open a shell in the Django container:

```bash
task shell
```

- Rodar os testes com pytest / Run tests with pytest:

```bash
task test
```

- Criar novas migrações / Make new migrations:

```bash
task makemigrations
```

- Aplicar migrações / Apply migrations:

```bash
task migrate
```

- Criar um superusuário / Create a superuser:

```bash
task createsuperuser
```

## Deployment
The following details how to deploy this application.

### Docker
See detailed cookiecutter-django Docker documentation.
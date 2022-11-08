# GameBots

> Веб-сайт по презентации и продаже игровых ботов.

> Версия: 0.3.0

> License: MIT

## Настройки `config/settings`

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Модели

TODO

## Basic Commands

### Type checks

Running type checks with mypy:

    $ mypy gamebots

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

### Pytest

    $ pytest
    $ pytest -s (with i/o logging)

Тест отдельного модуля

    $ pytest /tests/test_models.py

Тест только с декоратором `@pytest.mark.slow`

    $ pytest -v -m slow

Инверсия предыдущей команды - исключить тесты с декоратором `@pytest.mark.slow`)

    $ pytest -v -m "not slow"

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

### Celery

This app comes with Celery.

To run a celery worker:

``` bash
cd gamebots
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.

### Email Server

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server [MailHog](https://github.com/mailhog/MailHog) with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.
Please check [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html) for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to `http://127.0.0.1:8025`

### Sentry

Sentry is an error logging aggregator service. You can sign up for a free account at <https://sentry.io/signup/?code=cookiecutter> or download and host it yourself.
The system is set up with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

#### Команды

    $ docker-compose -f local.yml build

    $ docker-compose -f local.yml up

    $ set(export) COMPOSE_FILE=local.yml  (задать путь к докер конфигу)
    $ docker-compose up
    $ docker-compose up -d  (detached-daemon)

#### Вызов команды внутри контейнера

    $ docker-compose -f local.yml run --rm django python manage.py migrate
    $ docker-compose -f local.yml run --rm django python manage.py createsuperuser
    $ docker-compose -f local.yml run --rm django pip install

#### Ребилд

    $ docker-compose -f local.yml up --build

#### Bash

    $ docker-compose -f local.yml run django bash
    $ docker-compose -f local.yml exec django bash
    $ exit


### Custom Bootstrap Compilation

The generated CSS is set up with automatic Bootstrap recompilation with variables of your choice.
Bootstrap v5 is installed using npm and customised by tweaking your variables in `static/sass/custom_bootstrap_vars`.

You can find a list of available variables [in the bootstrap source](https://github.com/twbs/bootstrap/blob/main/scss/_variables.scss), or get explanations on them in the [Bootstrap docs](https://getbootstrap.com/docs/5.1/customize/sass/).

Bootstrap's javascript as well as its dependencies is concatenated into a single file: `static/js/vendors.js`.

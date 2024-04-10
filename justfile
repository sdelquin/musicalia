@runserver:
    python manage.py runserver

@sh:
    # https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-doctest_mode
    python manage.py shell

@dbsh:
    python manage.py dbshell

@check:
    python manage.py check

makemigrations app="":
    python manage.py makemigrations {{ app }}

migrate app="":
    python manage.py migrate {{ app }}

showmigrations app="":
    python manage.py showmigrations {{ app }}

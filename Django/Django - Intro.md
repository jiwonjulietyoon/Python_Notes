



# Create New Workspace on C9.io

(start with 'Blank' Template)

Open new terminal, and run the following codes 

- (copy & paste line by line)

```shell
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
exec "$SHELL"
```

```shell
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
exec "$SHELL"
```

```shell
pyenv install 3.6.7
pyenv global 3.6.7
```

- At this point, check that `python --version` yields `Python 3.6.7`



# Create New Folder and Project

Note) A single C9 workspace will hold multiple Django projects. Thus create a new folder for each new project.

Ex) Project name : `practice`

##### Create new folder (via terminal)

- `mkdir PRACTICE`
  - for readability, the name of the main folder should be written in all-caps
- `cd PRACTICE`

##### Set up Virtual Environment

- `pyenv virtualenv 3.6.7 practice-venv`
- `pyenv local practice-venv`
  - check that `(practice-venv)` has now been prepended to the terminal prompt
  - `(practice-venv)` indicates that the virtual environment has been activated
    - `cd ../` to break out of the virtual environment
    - `cd PRACTICE/` to return to the virtual environment

##### Install Django and Create New Project

- `pip install django`

- `django-admin startproject practice .`

  - At this point, `tree .` should yield:

  - ```
    .
    ├── manage.py
    └── practice
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
    
    1 directory, 5 files
    ```

##### Validify HTTP_HOST header

- In `settings.py` (`PRACTICE/practice/settings.py`), modify:
  - e.g): `ALLOWED_HOSTS = ['django-prac-whitejcme.c9users.io']`
  - (where `django-prac` is the name of the workspace)

##### Internationalization : Adjust server time zone and language

- Deactivate server
  - Preferably, rerun server upon modifying `settings.py` or other core settings
- In `settings.py`, modify:
  - `TIME_ZONE = 'Asia/Seoul'`   (originally `'UTC'`)
  - `LANGUAGE_CODE = 'ko-kr'`  (originally `'en-us'`)

##### Run Server

- `python manage.py runserver $IP:$PORT`
  - `$IP:$PORT` is for C9 only



# Create Application (within Project)

Ex) Application name: `pages`

##### Setting Up

- `python manage.py startapp pages` to create new app
- In `PRACTICE/practice/settings.py`:
  - add `'pages',` as the last item of `INSTALLED_APPS`
- Create a new `templates/` folder under `PRACTICE/pages` 
  - (this is where all `html` files will go)













//
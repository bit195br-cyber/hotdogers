import os
from pathlib import Path

# Define o caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# SEGURANÇA: Mantenha a chave secreta em segredo em produção!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-uma-chave-padrao-para-desenvolvimento-local')

# A variável DEBUG é True por padrão, a menos que a env var diga 'False'
DEBUG = True

# Adicionamos o seu domínio do Railway diretamente na lista de hosts permitidos.
ALLOWED_HOSTS = ['gabrielferreira.pythonanywhere.com', 'localhost', '127.0.0.1', 'web']

# Adicionamos também na lista de origens confiáveis para que os formulários funcionem.
CSRF_TRUSTED_ORIGINS = ['https://gabrielferreira.pythonanywhere.com/']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hotdogs', # Adicionado o nome da sua pasta como app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# AJUSTADO: Apontando para a pasta hotdogs
ROOT_URLCONF = 'hotdogs.urls' 

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# AJUSTADO: Apontando para o WSGI da pasta hotdogs
WSGI_APPLICATION = 'hotdogs.wsgi.application'

DATABASES = {
    'default': { # Corrigido de caracteres especiais para 'default'
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# Arquivos Estáticos
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_collected')
# AJUSTADO: Caminho dos estáticos dentro da pasta hotdogs
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
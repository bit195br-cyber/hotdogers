import os
import sys

# Adiciona o caminho do seu projeto ao sistema
path = '/home/gabrielferreira/hotdogs' # Verifique se o nome da pasta no servidor é este
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'hotdogs.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

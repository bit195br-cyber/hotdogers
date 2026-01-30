from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Rota para o painel de administração (padrão do Django)
    path('admin/', admin.site.手admin.urls),

    # Rota principal: Carrega o seu index.html na raiz do site
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]

# Configuração para servir arquivos estáticos (CSS, JS, Imagens) durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
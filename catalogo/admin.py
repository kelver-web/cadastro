from django.contrib import admin
from .models import Categoria, Produto

# Register your models here.


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome_produto', 'categoria', 'quantidade', 'descricao',
                    'publicado', 'ativo')
    list_filter = ('nome_produto', 'categoria','criado_em')
    search_fields = ('nome_produto', 'descricao')
    ordering = ('nome_produto',)

admin.site.register(Categoria)

from django.contrib import admin
from .models import Profissao, Contato, ContractType

# Register your models here.

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email',
                    'data_criacao', 'profissao', 'mostrar')
    list_display_links = ('id', 'nome', 'sobrenome')
    # list_filter = ('nome', 'sobrenome')
    list_per_page = 10
    search_fields = ('nome', 'sobrenome', 'telefone')
    list_editable = ('telefone', 'mostrar')

admin.site.register(Profissao)
admin.site.register(ContractType)
admin.site.register(Contato, ContatoAdmin)
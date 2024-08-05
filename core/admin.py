from django.contrib import admin

from .models import Cargo, Servicos, Equipe, Features, Planos, Avaliacao

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')

@admin.register(Servicos)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')

@admin.register(Equipe)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')

@admin.register(Features)
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'icone')

@admin.register(Planos)
class PlanosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'usuario', 'capacidade', 'suporte', 'atualizacoes', 'icone')

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'avaliacao')
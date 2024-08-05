import uuid
from django.db import models
from stdimage import StdImageField

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return  filename


class Base(models.Model):

    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField("Ativo?" , default=True)

    class Meta:
        abstract = True

class Servicos(Base):
    ICONE_CHOICE = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    servico = models.CharField("Serviço", max_length=100)
    descricao = models.TextField("Descrição", max_length=200)
    icone = models.CharField("Icone", max_length=12, choices=ICONE_CHOICE)

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"
    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField("Cargo", max_length=100)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

    def __str__(self):
        return self.cargo

class Equipe(Base):
    nome = models.CharField("Nome", max_length=100)
    cargo = models.ForeignKey("core.Cargo", verbose_name="Cargo", on_delete=models.CASCADE)
    bio = models.TextField("Bio", max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField("Facebook", max_length=100, default='#')
    twitter = models.CharField("Twitter", max_length=100, default='#')
    instagram = models.CharField("Instagram", max_length=100, default='#')

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"
    def __str__(self):
        return self.nome


class Features(Base):
    F_ICONE_CHOICE = (
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'Laptop'),
        ('lni-cog', 'Engrenagem'),
        ('lni-leaf', 'Folha'),
        ('lni-layers', 'Camadas')
    )
    nome = models.CharField("Nome", max_length=100)
    descricao = models.TextField("Descrição", max_length=250)
    icone = models.CharField("Icone", max_length=16, choices=F_ICONE_CHOICE)

    class Meta:
        verbose_name = "Funcionalidade"
        verbose_name_plural = "Funcionalidades"
    def __str__(self):
        return self.nome

class Planos(Base):
    P_ICONE_CHOICE = (
        ('lni-package', 'Caixa'),
        ('lni-drop', 'Gota'),
        ('lni-star', 'Estrela')
    )
    nome = models.CharField("Nome", max_length=100)
    valor = models.FloatField("Valor")
    usuario = models.CharField("Usuários", max_length=100)
    capacidade = models.CharField("Capacidade", max_length=100)
    suporte = models.CharField("Suporte", max_length=100)
    atualizacoes = models.CharField("Atualizações", max_length=100)
    icone = models.CharField("Icone", max_length=20, choices=P_ICONE_CHOICE, default='lni-package')

    class Meta:
        verbose_name = "Plano"
        verbose_name_plural = "Planos"
    def __str__(self):
        return self.nome

import uuid
from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_path

class GetFilePathTestCase(TestCase):

    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))


class ServicosTestCase(TestCase):
    
    def setUp(self):
        self.servicos = mommy.make("Servicos")

    def test_str(self):
        self.assertEquals(str(self.servicos), (self.servicos.servico))



class CargoTestCase(TestCase):
    
    def setUp(self):
        self.cargo = mommy.make("Cargo")

    def test_str(self):
        self.assertEquals(str(self.cargo), (self.cargo.cargo))


class EquipeTestCase(TestCase):

    def setUp(self):
        self.equipe = mommy.make("Equipe")

    def test_str(self):
        self.assertEquals(str(self.equipe), (self.equipe.nome))



class FeaturesTestCase(TestCase):

    def setUp(self):
        self.feature = mommy.make("Features")

    def test_str(self):
        self.assertEquals(str(self.feature), (self.feature.nome))


class PlanosTestCase(TestCase):

    def setUp(self):
        self.plano = mommy.make("Planos")

    def test_str(self):
        self.assertEquals(str(self.plano), (self.plano.nome))


class AvaliacaoTestCase(TestCase):

    def setUp(self):
        self.avaliacao = mommy.make("Avaliacao")

    def test_str(self):
        self.assertEquals(str(self.avaliacao), (self.avaliacao.nome))

from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):

    def setUp(self):
        
        self.dados = {

            'nome': "Teste Nome",
            'email': "testemail@gmail.com",
            'assunto': "Teste Assunto",
            'mensagem': "Teste Mensagem"
        }
        self.cliente = Client()

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertAlmostEquals(request.status_code, 302)

    def test_form_invalid(self):
        dados = {
            'nome' : "Teste para dar erro",
            'email' : "testeerro@gmail.com" 
        }
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertAlmostEquals(request.status_code, 200)
from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy
from model_mommy import mommy


class IndexViewTestCase(TestCase):

    def setUp(self):
        
        self.dados = {

            'nome': "Teste Nome",
            'email': "testemail@gmail.com",
            'assunto': "Teste Assunto",
            'mensagem': "Teste Mensagem"
        }
        self.cliente = Client()

        self.avaliacao = mommy.make("Avaliacao")


    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        dados = {
            'nome' : "Teste para dar erro",
            'email' : "testeerro@gmail.com" 
        }
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200)

    def test_for_estrela(self):

        lista_estrela = ['b' for _ in range(self.avaliacao.estrela)]

        self.assertEquals(len(lista_estrela), self.avaliacao.estrela)


    def test_for_sem_estrela(self):

        list_estrelaNull = ['c' for _ in range(5 - self.avaliacao.estrela)]

        self.assertEquals(len(list_estrelaNull), 5 - self.avaliacao.estrela)


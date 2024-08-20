from django.test import TestCase

from core.forms import ContatoForm


class ContatoFormTestCase(TestCase):

    def setUp(self):
        self.nome = "Matheus"
        self.email = "teste@gmail.com"
        self.assunto = "Envio de teste Formulario"
        self.mensagem = "Este email serve apenas como um teste para o formulário implementado no site para envio de emails."

        self.dados = {

            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem
        }
        
        self.form = ContatoForm(data=self.dados)


    def test_send_mail(self):
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()

        self.assertEquals(res1, res2)

from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Equipe, Servicos, Features, Planos, Avaliacao
from .forms import ContatoForm

#Testando email usado para efetuar commits no trabalho

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servicos.objects.order_by('?').all()
        context['equipe'] = Equipe.objects.order_by('?').all()
        context['planos'] = Planos.objects.all()
        

        features = Features.objects.order_by('?').all()
        metade = len(features) // 2
        context['features_col1'] = features[:metade]
        context['features_col2'] = features[metade:]

        avali = Avaliacao.objects.order_by('?').all()
        avali_com_estrelas = []

        for a in avali:
            lista_estrela = ['b' for _ in range(a.estrela)]  # Cria uma lista com 'b' repetido 'a.estrela' vezes
            list_estrelaNull = ['c' for _ in range(5 - a.estrela)] # Criando uma lista com 'c' para o restante da conta de 5(limite de estrelas) menos quantidade de estrela
            avali_com_estrelas.append({
                'avaliacao': a,
                'estrelas': lista_estrela,
                'estrelasN': list_estrelaNull
            })

        context['avali'] = avali_com_estrelas
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)

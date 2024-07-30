from django.views.generic import TemplateView

from .models import Equipe, Servicos
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servicos.objects.order_by('?').all()
        context['equipe'] = Equipe.objects.order_by('?').all()
        return context
from django.views.generic import TemplateView

from .models import Equipe, Servicos, Features
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servicos.objects.order_by('?').all()
        context['equipe'] = Equipe.objects.order_by('?').all()

        features = Features.objects.order_by('?').all()
        metade = len(features) // 2
        context['features_col1'] = features[:metade]
        context['features_col2'] = features[metade:]
        return context
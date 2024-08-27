
from django.views.generic import TemplateView
from common.views import TitleMixin



class MovesView(TitleMixin, TemplateView):
    
    template_name = 'main/index.html'
    title = 'Движения'

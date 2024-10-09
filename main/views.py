from django.views.generic import DetailView, ListView
from common.views import TitleMixin
from main.models import Movements


class MovesView(TitleMixin, ListView):
    model = Movements
    template_name = 'main/index.html'
    title = 'Движения'
    context_object_name = 'movements'

class MovementsDetailView(TitleMixin, DetailView):
    model = Movements
    template_name = 'main/movement_detail.html'
    context_object_name = 'movement'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.movement_type
        return context

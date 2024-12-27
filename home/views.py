from django.shortcuts import render
from django.views.generic import TemplateView
from order.models import Order


# Create your views here.

class HomePage(TemplateView):
    template_name = 'home/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['orders'] = Order.objects.all()
        return context

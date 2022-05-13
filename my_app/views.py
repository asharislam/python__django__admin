from django.shortcuts import render
from django.views.generic import TemplateView



class HomeView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            list = [1, 2, 3, 4, 5, 6]
            context['list'] = list
            return context


class AboutView(TemplateView):
    template_name = "about.html"
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['first_name'] = "Ashar"
            context['last_name'] = "Islam"
            context['country_name'] = "Bangladesh"
            return context

class ContractView(TemplateView):
    template_name = "contract.html"
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['your_first_name'] = "Fahad"
            context['your_last_name'] = "Islam"
            context['your_country_name'] = "Bangladesh"
            return context

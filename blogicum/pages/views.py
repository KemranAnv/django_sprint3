"""View function of app pages."""

from django.views.generic import TemplateView


class AboutView(TemplateView):
    """Aboutview."""

    template_name = 'pages/about.html'


class RulesView(TemplateView):
    """Rulesview."""

    template_name = 'pages/rules.html'

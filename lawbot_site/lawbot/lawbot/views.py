from django.views.generic import TemplateView

#-- TemplageView
class HomeView(TemplateView):
    template_name = 'home.html'

from django.views.generic import ListView, DetailView
from judgement_detail.models import Judgement_detail

class JudgementLV(ListView):
    model = Judgement_detail

class JudgementDV(DetailView):
    model = Judgement_detail

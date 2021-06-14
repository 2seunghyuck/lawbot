from django.url import path
from Judgement_detail.views import Judgement_detailLV, Judgement_detailDV

app_name = 'judgement_detail'
urlpatterns = [
    path('', Judgement_detailLV.as_view(), name='index'),
    path('<int:pk>/', Judgement_detailDV.as_view(), name='detail'),

]
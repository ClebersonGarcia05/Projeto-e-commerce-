from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('carrinho/', CarrinhoView.as_view(), name='carrinho'),
    path('informacao-item/', ItemPageView.as_view(), name='informacao'),
    path('login/', login_view, name='login'),
    path('pagamento/', PagamentoView.as_view(), name='pagamento'),
]

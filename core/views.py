
from django.contrib import messages
from django.contrib.auth.models import AbstractUser, BaseUserManager, auth
from django.shortcuts import redirect, render
from django.views.generic import FormView, TemplateView

from .forms import CustomUsuarioCreationForm, LoginForm
from .models import *


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context[""] = ''
        return context

class CadastroView(TemplateView):
    template_name = 'cadastro.html'

class CarrinhoView(TemplateView):
    template_name = 'carrinho.html'

class ItemPageView(TemplateView):
    template_name = 'item_page.html'

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credenciais inválidas')

            return redirect('login.html')
    else:
        return render(request, 'login.html')


class PagamentoView(TemplateView):
    template_name = 'pagamento.html'

from django.shortcuts import render, redirect
from app.forms import CarrosForm
from app.models import Carros
from app.static import catalog
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    return render(request, 'index.html')

def vendas(request):
    return render(request, 'vendas.html')

def financeiro(request):
    return render(request, 'financeiro.html')
    
def produtos(request):
    return render(request, 'produtos.html')


def projetos(request):
    data = {}
    data['form'] = CarrosForm()
       
    search = request.GET.get('search')
    if search:
        data['db'] = Carros.objects.filter(modelo__icontains=search)
    else:
        data['db'] = Carros.objects.all()
    #all = Carros.objects.all()
    #paginator = Paginator(all, 5)
    #pages = request.GET.get('page')
    #data['db'] = paginator.get_page(pages)
    return render(request, 'projetos.html', data)
     
def form(request):
    data = {}
    data['form'] = CarrosForm()
    return render(request, 'form.html')

def create(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('projetos')

def view(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    data['form'] = CarrosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    form = CarrosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Carros.objects.get(pk=pk)
    db.delete()
    return redirect('projetos')



def producao(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Carros.objects.filter(modelo__icontains=search)
    else:
        data['db'] = Carros.objects.all()
    #all = Carros.objects.all()
    #paginator = Paginator(all, 5)
    #pages = request.GET.get('page')
    #data['db'] = paginator.get_page(pages)
    return render(request, 'projetos.html', data)
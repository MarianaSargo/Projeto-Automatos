from django.shortcuts import render
from .models import Automato, MTuring
from .forms import AutomatoForm, ExpressaoForm, MTuringForm, ExpressaoMTForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .func import valida_automato, valida_maquina
from .func import desenha_automato, desenha_mt
from django.core.files.storage import FileSystemStorage
from pathlib import Path
import os
import json



# Create your views here.

def introducao_page_view(request):
	return render(request, 'automatos/introducao.html')

def automatos_page_view(request):
	context = {'automatos': Automato.objects.all()}
	return render(request, 'automatos/automatos.html', context)

def mturing_page_view(request):
	context = {'mturings': MTuring.objects.all()}
	return render(request, 'automatos/mturing.html', context)

def criarafd_page_view(request):

	form = AutomatoForm(request.POST or None)

	if form.is_valid():
		form.save()
		UltimoAutomato = Automato.objects.all().count() - 1
		desenha_automato(UltimoAutomato)
		return HttpResponseRedirect(reverse('automatos:automatos'))


	context = {'form': form}
	return render(request, 'automatos/criarafd.html', context)

def editarafd_page_view(request, automato_id):

	automato = Automato.objects.get(id=automato_id)
	form = AutomatoForm(request.POST or None, instance=automato)

	if form.is_valid():
		form.save()
		UltimoAutomato = Automato.objects.all().count() - 1
		desenha_automato(UltimoAutomato)
		return HttpResponseRedirect(reverse('automatos:automatos'))

	context = {'form': form, 'automato_id': automato_id}
	return render(request, 'automatos/editarafd.html', context)


def apagarafd_page_view(request, automato_id):

    Automato.objects.get(id=automato_id).delete()
    return HttpResponseRedirect(reverse('automatos:automatos'))

def visualafd_page_view(request, automato_id):
	automato = {'detalhes':Automato.objects.get(id=automato_id)}
	return render(request, 'automatos/visualafd.html', automato)

def testarafd_page_view(request, automato_id):

	resultado = expressao = None

	if request.POST:
		form = ExpressaoForm(request.POST)  # a expressão submetida no formulário é guardada na variável form
		if form.is_valid():
			expressao = form.cleaned_data['expressao']
			try:
				resultado = valida_automato(expressao, automato_id)
			except:
				resultado = "expressão inválida"

	form = ExpressaoForm(request.POST)

	context = {
		'form': form,
		'resultado': resultado,
		'expressao': expressao
	}

	return render(request, 'automatos/testarafd.html', context)

def jsonafd_page_view(request):
	if request.method == 'POST':
		uploaded_file = request.FILES['document']
		print(uploaded_file.name)
		print(uploaded_file.size)
		fs = FileSystemStorage()
		fs.save(uploaded_file.name, uploaded_file)

		with open(os.path.join(uploaded_file.name), 'r') as json_file:
			conteudo = json.load(json_file)
			json_file.close()
		Alfabeto = conteudo['alfabeto']
		Estados = conteudo['estados']
		EstadoInicial = conteudo['EstadosDeAceitacao']
		EstadoDeAceitacao = conteudo['EstadoInicial']
		Transicoes = conteudo['DicionarioTransicao']
		Descricao = conteudo['Descricao']
		print(Alfabeto)

		UltimoAutomato = Automato.objects.all().count() - 1
		if UltimoAutomato >= 0:
			id = Automato.objects.all()[UltimoAutomato].id + 1
		else:
			id = 0
		novo = Automato(id,EstadoInicial,EstadoDeAceitacao,Transicoes,Estados,Alfabeto,Descricao)
		novo.save()
		UltimoAutomato = Automato.objects.all().count() - 1
		desenha_automato(UltimoAutomato)
	return render(request, 'automatos/uploadjson.html')

def criarmt_page_view(request):

	form = MTuringForm(request.POST or None)

	if form.is_valid():
		form.save()
		UltimoMT = MTuring.objects.all().count() - 1
		desenha_mt(UltimoMT)
		return HttpResponseRedirect(reverse('automatos:mturing'))


	context = {'form': form}
	return render(request, 'automatos/criarmt.html', context)

def visualmt_page_view(request, mt_id):

	mturing = {'detalhess':MTuring.objects.get(id=mt_id)}
	return render(request, 'automatos/visualmt.html', mturing)

def editarmt_page_view(request, mt_id):

	mt = MTuring.objects.get(id=mt_id)
	form = MTuringForm(request.POST or None, instance=mt)

	if form.is_valid():
		form.save()
		UltimoMT = MTuring.objects.all().count() - 1
		desenha_mt(UltimoMT)
		return HttpResponseRedirect(reverse('automatos:mturing'))

	context = {'form': form, 'mt_id': mt_id}
	return render(request, 'automatos/editarmt.html', context)


def apagarmt_page_view(request, mt_id):

    MTuring.objects.get(id=mt_id).delete()
    return HttpResponseRedirect(reverse('automatos:mturing'))

def jsonmt_page_view(request):
	if request.method == 'POST':
		uploaded_file = request.FILES['document']
		print(uploaded_file.name)
		print(uploaded_file.size)
		fs = FileSystemStorage()
		fs.save(uploaded_file.name, uploaded_file)

		with open(os.path.join(uploaded_file.name), 'r') as json_file:
			conteudo = json.load(json_file)
			json_file.close()
		Alfabeto = conteudo['alfabeto']
		Estados = conteudo['estados']
		EstadoInicial = conteudo['EstadosDeAceitacao']
		EstadoDeAceitacao = conteudo['EstadoInicial']
		Transicoes = conteudo['DicionarioTransicao']
		Descricao = conteudo['Descricao']
		print(Alfabeto)

		UltimoMT = MTuring.objects.all().count() - 1
		if UltimoMT >= 0:
			id = MTuring.objects.all()[UltimoMT].id + 1
		else:
			id = 0
		novo = MTuring(id,EstadoInicial,EstadoDeAceitacao,Transicoes,Estados,Alfabeto,Descricao)
		novo.save()
		UltimoMT = MTuring.objects.all().count() - 1
		desenha_mt(UltimoMT)
	return render(request, 'automatos/uploadjson.html')

def testarmt_page_view(request, mt_id):

	resultado = expressao = None

	if request.POST:
		form = ExpressaoMTForm(request.POST)  # a expressão submetida no formulário é guardada na variável form
		if form.is_valid():
			expressao = form.cleaned_data['expressaoMT']
			try:
				resultado = valida_maquina(expressao, mt_id)
			except:
				resultado = "expressão inválida"

	form = ExpressaoMTForm(request.POST)

	context = {
		'form': form,
		'resultado': resultado,
		'expressao': expressao
	}

	return render(request, 'automatos/testarmt.html', context)

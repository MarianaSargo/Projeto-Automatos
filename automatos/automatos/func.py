import os

from automatos.models import Automato, MTuring
from automatos import views
from graphviz import Digraph

def valida_automato(sequencia, automato_id):
	Objeto = Automato.objects.get(id=automato_id)
	EstadoInicial = Objeto.EstadoInicial
	EstadoFinal = set(Objeto.EstadoFinal)
	Dic_Transicoes = {}

	for i in Objeto.Transicoes.split():
		primeiroestado = i[0]
		simbolo = i[1]
		segundoestado = i[2]
		Dic_Transicoes[(primeiroestado, simbolo)] = segundoestado
	for i in sequencia:
		EstadoInicial = Dic_Transicoes[(EstadoInicial, i)]
	if EstadoInicial in EstadoFinal:
		return "Expressão Aceite"
	else:
		return "Expressão Não Aceite"

def desenha_automato(automato_id):
		automato = Automato.objects.all()[automato_id]
		class Grafico():
			def __init__(self):
				self.Alfabeto = automato.Alfabeto
				self.Estados = set(automato.Estados)
				self.EstadoInicial = automato.EstadoInicial
				self.EstadosDeAceitacao = set(automato.EstadoFinal)
				ListaDicionarioTransicoes = automato.Transicoes.split()
				self.DicionarioTransicao = {}
				self.Descricao = automato.Descricao
				for elemento in ListaDicionarioTransicoes:
					self.DicionarioTransicao[elemento[0], elemento[1]] = elemento[2]
				d = Digraph(name=self.Descricao)

				# configurações gerais
				d.graph_attr['rankdir'] = 'LR'
				d.edge_attr.update(arrowhead='vee', arrowsize='1')
				# d.edge_attr['color'] = 'blue'
				d.node_attr['shape'] = 'circle'
				# d.node_attr['color'] = 'blue'

				# Estado inicial
				d.node('Start', label='', shape='none')

				# Estados de transição
				estadosDeTransicao = set(self.Estados) - set(self.EstadosDeAceitacao)
				for estado in estadosDeTransicao:
					d.node(estado)

				# Estado aceitação
				for estado in self.EstadosDeAceitacao:
					d.node(estado, shape='doublecircle')

				# Transicoes
				d.edge('Start', self.EstadoInicial)

				for tuplo, estadoSeguinte in self.DicionarioTransicao.items():
					d.edge(tuplo[0], estadoSeguinte, label=tuplo[1])

				# print(d.source)
				d.format = 'svg'
				path = os.getcwd()
				d.render(path + '\\automatos\\static\\automatos\\images\\ImagesAutomatos\\' + self.Descricao)

		teste = Grafico()


def valida_maquina(sequencia, mt_id):
	Objeto = MTuring.objects.get(id=mt_id)
	EstadoInicial = Objeto.EstadoInicial
	EstadoDeAceitacao = Objeto.EstadoFinal
	dictransicoes = {}

	for i in Objeto.Transicoes.split():
		primeiroestado = i[0]
		primeirosimbolo = i[1]
		segundosimbolo = i[2]
		direcao = i[3]
		segundoestado = i[4]
		dictransicoes[(primeiroestado, primeirosimbolo)] = segundosimbolo, direcao, segundoestado
		print(dictransicoes)

	estadoatual = EstadoInicial
	lista = ['Δ'] * 20
	cabeca = 10
	lista[10:0] = sequencia
	dictransicoes.update({'exit': 1})
	erro = False

	while estadoatual != EstadoDeAceitacao and erro != True:
		for tuplo1, tuplo2 in dictransicoes.items():
			if tuplo1[0] == estadoatual and tuplo1[1] == lista[cabeca]:
				lista[cabeca] = tuplo2[0]
				estadoatual = tuplo2[2]
				if tuplo2[1] == 'R':
					cabeca = cabeca + 1
				if tuplo2[1] == 'L':
					cabeca = cabeca - 1
				break
			if tuplo1 == 'exit':
				erro = True

	if estadoatual == EstadoDeAceitacao:
		return ("Sequencia Valida")
	if erro == True:
		return ("Sequencia Invalida")

def desenha_mt(mt_id):
	Objeto = MTuring.objects.all()[mt_id]

	class Grafic():
		def __init__(self):
			self.Alfabeto = Objeto.Alfabeto
			self.Estados = Objeto.Estados
			self.EstadoInicial = Objeto.EstadoInicial
			self.EstadosDeAceitacao = Objeto.EstadoFinal
			ListaDicionarioTransicoes = Objeto.Transicoes.split()
			self.DicionarioTransicao = {}
			self.Descricao = Objeto.Descricao
			for elemento in ListaDicionarioTransicoes:
				self.DicionarioTransicao[elemento[0], elemento[1]] = elemento[2], elemento[3], elemento[4]
			d = Digraph(name=self.Descricao)

			# configurações gerais
			d.graph_attr['rankdir'] = 'LR'
			d.edge_attr.update(arrowhead='vee', arrowsize='1')
			# d.edge_attr['color'] = 'blue'
			d.node_attr['shape'] = 'circle'
			# d.node_attr['color'] = 'blue'

			# Estado inicial
			d.node('Start', label='', shape='none')

			# Estados de transição
			estadosDeTransicao = set(self.Estados) - set(self.EstadosDeAceitacao)
			for estado in estadosDeTransicao:
				d.node(estado)

			# Estado aceitação
			for estado in self.EstadosDeAceitacao:
				d.node(estado, shape='doublecircle')

			# Transicoes
			d.edge('Start', self.EstadoInicial)

			for tuplo1, tuplo2 in self.DicionarioTransicao.items():
				d.edge(tuplo1[0], tuplo2[2], label=tuplo1[1] + tuplo2[0] + tuplo2[1])

			# print(d.source)
			d.format = 'svg'
			path = os.getcwd()
			d.render(path + '\\automatos\\static\\automatos\\images\\ImagesMaquinas\\' + self.Descricao)

	teste = Grafic()
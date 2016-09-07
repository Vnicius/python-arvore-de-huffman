"""
	Essa classe primeiramente guardará uma lista com todos os caracteres do texto lido, cada caractere vai ser atribuído a um nó e 
	ordenados em ordem crescente de frequência.
	A partir dessa lista ordenada será criada a árvore binária.

	raiz - primeiramente será uma lista de objetos da classe No, mas quando a árvore estiver formada seu primeiro e único elemento será a raiz da árvore;
	texto - uma lista de caracteres que representa todo o texto, é usado para gerar a lista e o texto em binário.

	insereRaiz() - insere um objeto na cabeça da lista;
	insere() - insere um objeto no fim da lista, mas se houver algum objeto com o mesmo caractere então só incrementa a frequência desse objeto,
		um sorted() é usado para deixar a lista sempre ordenada em ordem crescente de frequência;
	criaLista() - cria uma lista de caracteres a partir do texto, instancia os objetos No e insere com os métodos anteriores;
	printLista() - imprime na tela, um a um, os objetos guardados na lista;
	criaArv() - cria a Árvore de Huffman. Primeiramente chama o método para criar a lista e a partir da lista formada começa a criação da árvore.
		Cria-se um novo objeto da classe No, sem caractere, com a frequência sendo a soma da frequência dos dois primeiros elementos das listas e seus
		filhos da esquerda e direita são, respectivamente, esses dois primeiros elementos da lista. Os dois primeiros elementos são retirados da lista
		e o objeto criado anteriormente é inserido na lista.

"""

from No import No

class ListaNos:

	raiz = 0
	texto = ''

	def __init__(self, lista):
		self.texto = lista

	def insereRaiz(self, novo):	#insere o primeiro elemento da lista
		self.raiz = [novo] 
		return

	def insere(self, novo):	#insere o elemento no fim da lista
		
		for item in self.raiz:
			if item.conteudo == novo.conteudo:	# se houver outro elemento na lista com o mesmo caractere
				item.freq += 1					# a frequência é incrementada
				self.raiz = sorted(self.raiz, key=lambda no: no.freq) # e a lista reordenada
				return							# e finaliza o método

		self.raiz += [novo]					# se não, o novo objeto é inserido
		self.raiz= sorted(self.raiz, key=lambda no: no.freq) # e a lista reordenada
		
		return

	def criaLista(self):
		for letter in self.texto:
			if self.raiz == 0:							 # se a lista está vazia
															 # insere o primeiro elemento

				self.insereRaiz(No(letter,1,'', None, None)) # para guardar o caractere em si

				#self.insereRaiz(No(str(ord(letter)),1,'', None, None)) # para inserir o valor em ASCII do caractere
			else: 
														 # se não, insere o elemento nomalmente
				self.insere(No(letter,1,'', None, None)) # para guardar o caractere em si

				#self.insere(No(str(ord(letter)),1,'',None,None)) # para inserir o valor em ASCII do caractere
		return

	def printLista(self): # exibe cada elemento separadamente
		for tup in self.raiz:
			print (tup)
		return

	def criaArv(self):
		
		self.criaLista()	# chama o método para a criar a lista

		while len(self.raiz)>1:	# esse laço executa até restar apenas um elemento na lista, que será a raiz da árvore

			novo= No("",self.raiz[0].freq + self.raiz[1].freq,'',self.raiz[0],self.raiz[1])	# cria o nó intermediário
			
			del self.raiz[0]	#deleta os dois primeros elementos
			del self.raiz[0]

			self.raiz += [novo]	#insere o nó intermediário na lista
			self.raiz = sorted(self.raiz, key=lambda no: no.freq) # reordena a lista

		return
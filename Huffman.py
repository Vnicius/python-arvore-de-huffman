#### Iniciso da classe No ####

"""
	Objetos dessa classe serão os nós para a árvore binária de Huffman.
	
	conteudo - conteúdo que cada nó irá guardar um caractere;
	freq - frequência de cada caractere no texto;
	bin - código em binário que representa o caminho da raiz até dado nó;
	left - o filho da esquerda do nó;
	right - filho da direita;

	isLeaf() - retorna true se o nó é uma folha da árvore.


"""

class No:
	conteudo = 0
	bin = ""
	def __init__(self, conteudo, freq, bin, left, right):
		self.conteudo = conteudo
		self.freq = freq
		self.bin = bin
		self.left = left
		self.right = right

	def __repr__(self):
		return repr((self.conteudo, self.freq, self.bin))

	def isLeaf(self):
		return self.left is None and self.right is None

#### Fim da classe Nó ####


#### Inicio da classe ListaNos ###

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
class ListaNos:

	raiz = 0
	texto = ''

	def __init__(self, lista):
		ListaNos.texto = lista

	def insereRaiz(self, novo):	#insere o primeiro elemento da lista
		ListaNos.raiz = [novo] 
		return

	def insere(self, novo):	#insere o elemento no fim da lista
		
		for item in ListaNos.raiz:
			if item.conteudo == novo.conteudo:	# se houver outro elemento na lista com o mesmo caractere
				item.freq += 1					# a frequência é incrementada
				ListaNos.raiz = sorted(ListaNos.raiz, key=lambda no: no.freq) # e a lista reordenada
				return							# e finaliza o método

		ListaNos.raiz += [novo]					# se não, o novo objeto é inserido
		ListaNos.raiz= sorted(ListaNos.raiz, key=lambda no: no.freq) # e a lista reordenada
		
		return

	def criaLista(self):
		for letter in self.texto:
			if ListaNos.raiz == 0:							 # se a lista está vazia
															 # insere o primeiro elemento

				self.insereRaiz(No(letter,1,'', None, None)) # para guardar o caractere em si

				#self.insereRaiz(No(str(ord(letter)),1,'', None, None)) # para inserir o valor em ASCII do caractere
			else: 
														 # se não, insere o elemento nomalmente
				self.insere(No(letter,1,'', None, None)) # para guardar o caractere em si

				#self.insere(No(str(ord(letter)),1,'',None,None)) # para inserir o valor em ASCII do caractere
		return

	def printLista(self): # exibe cada elemento separadamente
		for tup in ListaNos.raiz:
			print (tup)
		return

	def criaArv(self):
		
		self.criaLista()	# chama o método para a criar a lista

		while len(ListaNos.raiz)>1:	# esse laço executa até restar apenas um elemento na lista, que será a raiz da árvore

			novo= No("",ListaNos.raiz[0].freq + ListaNos.raiz[1].freq,'',ListaNos.raiz[0],ListaNos.raiz[1])	# cria o nó intermediário
			
			del ListaNos.raiz[0]	#deleta os dois primeros elementos
			del ListaNos.raiz[0]

			ListaNos.raiz += [novo]	#insere o nó intermediário na lista
			ListaNos.raiz = sorted(ListaNos.raiz, key=lambda no: no.freq) # reordena a lista

		return

#### Fim da classe ListaNos ####

# usado apenas para debug
def navegar(no):	# apenas navega pela árvore e imprime na tela os elementos em pré-ordem
	if no is None: return

	if no.left is not None: navegar(no.left)

	if no.isLeaf(): print (no)

	if no.right is not None: navegar(no.right)

	return

def codifica(no):	# gera o código em binário para cada nó da árvore
					# esse código representa o caminho da raiz até o dado nó
		if no is None: return

		if no.left is not None:
			no.left.bin = no.bin +'1'	# sempre que for para a esquerda, concatena '1' ao código do filho
			codifica(no.left)

		if no.right is not None:
			no.right.bin = no.bin + '0'	# sempre que for para a direita, concatena '0' ao código do filho
			codifica(no.right)

		return


def getTextBin(arv,texto): # a partir da árvore e de uma lista com o texto original, 
							# retorna uma string com o texto em binário conforme o código de cada caracter na árvore
	result = ''
	for letter in texto:
		result += getBinLetter(arv,letter)  # para quando os elementos já são carateres
		#result += getBinLetter(arv,str(ord(letter))) # para elmentos em ASCII
	
	return result

def getBinLetter(arv,letter): # procura um dado caractere na árvore e retorna seu código

	bin = ''

	if arv.conteudo == letter:
		bin = arv.bin

	if arv.left is not None: bin = getBinLetter(arv.left,letter)

	if bin == '':
		if arv.right is not None: bin = getBinLetter(arv.right,letter)

	return bin

def arvToBin(arv): # retorna uma string com a formação da árvore em pré-ordem
	result = ''

	if arv is None: return

	if arv.left is None and arv.right is None:
		result += arv.conteudo

	if arv.left is not None: result += '1'+ arvToBin(arv.left)

	if arv.right is not None: result += '0'+ arvToBin(arv.right)

	return result

def openFile(file_name):	# pega o texto incial	
	try:
		file = open(file_name, "r")
		text = file.read()
		file.close()
	except IOError:
		print ("Erro ao abrir o arquivo")
	return text

def creatFile(file_name, text):		# escreve um arquivo com o texto em binário
	try:
		file = open(file_name, 'w')
		file.write(text)
		file.close()
	except IOError:
		raise print("Erro ao criar o arquivo")

def decodeBin(arv,textBin):	# a partir da árvore e do texto em binário resgata o texto original
	arvore = arv
	result =''
	for bin in textBin:
		if bin == '1':
			if arvore.left is not None:
				arvore = arvore.left
				if arvore.left is None and arvore.right is None:
					#result += (chr(int(arvore.conteudo))) # para quando os elmentos estão em ASCII
					result += (arvore.conteudo)			# para elementos sendo characteres
					arvore = arv
		else:
			if arvore.right is not None:
				arvore = arvore.right
				if arvore.left is None and arvore.right is None:
					#result += (chr(int(arvore.conteudo))) # para quando os elmentos estão em ASCII
					result += (arvore.conteudo)		# para elementos sendo characteres
					arvore = arv

	return result

##############################################

lista = list(openFile("abra.txt"))
listaNos = ListaNos(lista)
listaNos.criaArv()
codifica(listaNos.raiz[0])
#navegar(listaNos.raiz[0])

creatFile("result.txt",arvToBin(listaNos.raiz[0])+'\n'+getTextBin(listaNos.raiz[0],listaNos.texto))

print("Arvore  pre-ordem  "+arvToBin(listaNos.raiz[0]))

print(getTextBin(listaNos.raiz[0],listaNos.texto))

print(decodeBin(listaNos.raiz[0],getTextBin(listaNos.raiz[0],listaNos.texto)))

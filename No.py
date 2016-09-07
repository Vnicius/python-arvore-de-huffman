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
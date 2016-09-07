class HuffmanTree:
	# usado apenas para debug
	def navegar(self,no):	# apenas navega pela árvore e imprime na tela os elementos em pré-ordem
		if no is None: return

		if no.left is not None: self.navegar(no.left)

		if no.isLeaf(): print (no)

		if no.right is not None: self.navegar(no.right)

		return

	def codifica(self,no):	# gera o código em binário para cada nó da árvore
						# esse código representa o caminho da raiz até o dado nó
			if no is None: return

			if no.left is not None:
				no.left.bin = no.bin +'1'	# sempre que for para a esquerda, concatena '1' ao código do filho
				self.codifica(no.left)

			if no.right is not None:
				no.right.bin = no.bin + '0'	# sempre que for para a direita, concatena '0' ao código do filho
				self.codifica(no.right)

			return


	def getTextBin(self,arv,texto): # a partir da árvore e de uma lista com o texto original, 
								# retorna uma string com o texto em binário conforme o código de cada caracter na árvore
		result = ''
		for letter in texto:
			result += self.getBinLetter(arv,letter)  # para quando os elementos já são carateres
			#result += self.getBinLetter(arv,str(ord(letter))) # para elmentos em ASCII
		
		return result

	def getBinLetter(self,arv,letter): # procura um dado caractere na árvore e retorna seu código

		bin = ''

		if arv.conteudo == letter:
			bin = arv.bin

		if arv.left is not None: bin = self.getBinLetter(arv.left,letter)

		if bin == '':
			if arv.right is not None: bin = self.getBinLetter(arv.right,letter)

		return bin

	def arvToBin(self,arv): # retorna uma string com a formação da árvore em pré-ordem
		result = ''

		if arv is None: return

		if arv.left is None and arv.right is None:
			result += arv.conteudo

		if arv.left is not None: result += '1'+ self.arvToBin(arv.left)

		if arv.right is not None: result += '0'+ self.arvToBin(arv.right)

		return result

	

	def decodeBin(self,arv,textBin):	# a partir da árvore e do texto em binário resgata o texto original
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

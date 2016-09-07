from ListaNos import ListaNos
from HuffmanTree import HuffmanTree

##############################################
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


##############################################

########## Main ##############

lista = list(openFile("abra.txt"))
ht = HuffmanTree()
listaNos = ListaNos(lista)
listaNos.criaArv()
ht.codifica(listaNos.raiz[0])
#ht.navegar(listaNos.raiz[0])

creatFile("result.txt",ht.arvToBin(listaNos.raiz[0])+'\n'+ht.getTextBin(listaNos.raiz[0],listaNos.texto))

print("Arvore  pre-ordem  "+ht.arvToBin(listaNos.raiz[0]))

print(ht.getTextBin(listaNos.raiz[0],listaNos.texto))

print(ht.decodeBin(listaNos.raiz[0],ht.getTextBin(listaNos.raiz[0],listaNos.texto)))

#ESCREVENDO
arquivo = open('teste.txt', 'w') #o 'w' sobre escreve no arquivo
arquivo.write('Meu primeiro texto')
arquivo.close()

arquivo = open('teste.txt', 'a') #o 'a' add texto no arquivo, não apaga o anterior
arquivo.write('\nSegunda linha')
arquivo.close()

def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

if __name__ == '__main__':
    escrever_arquivo('Primeira linha.\n')
    atualizar_arquivo('Segunda linha.\n')

#LENDO
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

if __name__ == '__main__':
    ler_arquivo('teste.txt')

# Altere o Nome do Arquivo RAR
# Senha do Arquivo de Teste: ac

# RARFile Documentation
# https://rarfile.readthedocs.io/en/latest/index.html


import rarfile
import constantes
import datetime

# nome_do_arquivo_RAR = tuple('Teste_Password_ac.rar')


lista_senha = []
lista_indice_caracteres = []


#======================================================================================================================
# Autor: Cleber
# Descrição:  Função Principal do Programa
#======================================================================================================================
def main(nome_do_arquivo):
    ultima_senha_testada = ''
    numero_de_tentativas = 0

    inicio_Data_Hora = datetime.datetime.now()

    print(inicio_Data_Hora)





    with rarfile.RarFile(nome_do_arquivo) as rf:
        while 1:
            senha = geraSenha()
            print(senha)

            if senha != '':
                ultima_senha_testada = senha

                try:
                    rf.extractall(pwd=senha)
                except rarfile.RarWrongPassword:
                    numero_de_tentativas += 1
                except rarfile.BadRarName:
                    pass
                else:
                    print('Arquivo Descompactado')
                    tempo_decorrido = datetime.datetime.now() - inicio_Data_Hora
                    salvarSenha(nome_do_arquivo, senha, numero_de_tentativas, str(tempo_decorrido), True)
                    break
            else:
                salvarSenha(nome_do_arquivo, ultima_senha_testada, numero_de_tentativas, False)
                print('Opções Exauridas !')
                print('Senha Não Encontrada !')
                break


    return


#======================================================================================================================
# Autor: Cleber
# Descrição:  Caso encontre a Senha que descompacta o arquivo, a salva em um arquivo de texto.
#             Caso não encontre, salva a última senha que foi utilizada para tentar descompactar o arquivo.
#======================================================================================================================
def salvarSenha(nome_do_arquivo, senha, numero_de_tentativas, tempo_decorrido, sucesso):

    if sucesso:
        with open('Senhas.txt', 'a') as arquivo:
            arquivo.write(nome_do_arquivo + '  <--->  Senha: \"' + senha + '\"  <--->  Tentativas: ' + str(numero_de_tentativas) + '  <--->  Tempo Decorrido: ' + tempo_decorrido + '\n')
    else:
        with open('Senhas.txt', 'a') as arquivo:
            arquivo.write(nome_do_arquivo + '  <--->  Opções Exauridas ! Senha Não Encontrada ! Última Senha Testada: \"' + senha + '\"  <--->  Tentativas: ' + str(numero_de_tentativas) + '  <--->  Tempo Decorrido: ' + tempo_decorrido + '\n')

    return


#======================================================================================================================
# Autor: Cleber
# Descrição:  Realiza a Inicialização das Variáveis envolvidas no processo de Força Bruta.
#======================================================================================================================
def geraSenha():

    global lista_indice_caracteres


    tamanho_lista = len(lista_senha)

    if tamanho_lista == 0:
        lista_senha.append(constantes.caracteres[constantes.posicao_inicial])
        lista_indice_caracteres.append(constantes.posicao_inicial)
        return toString(lista_senha)

    else:
        return calculaNovaSenha()


#======================================================================================================================
# Autor: Cleber
# Descrição:  Determina qual é a próxima String que será utilizada no processo de Força Bruta.
#======================================================================================================================
def calculaNovaSenha(indice_lista:int = 0):

    global lista_senha
    global lista_indice_caracteres

    tamanho_lista = len(lista_senha)

    lista_indice_caracteres[indice_lista] += 1

    # Verifica se todos os Caracteres já foram testados na posição atual.
    if lista_indice_caracteres[indice_lista] >= constantes.numero_de_caracteres:
        # Reseta Caractere da Posição Atual
        lista_indice_caracteres[indice_lista] = constantes.posicao_inicial
        lista_senha[indice_lista] = constantes.caracteres[lista_indice_caracteres[indice_lista]]

        # Verifica se Todas as Possibilidades com o Tamanho Atual da Lista de Caracteres já foram Geradas
        indice_lista += 1
        if indice_lista >= tamanho_lista:
            # Verifica se o Tamanho da Senha já atingiu o Número Máximo de Caracteres
            if indice_lista >= constantes.tamanho_maximo_senha:
                # Retorna valor que finaliza o programa
                return ''
            else:
                # Adiciona Mais um Caractere à Senha
                lista_senha.append(constantes.caracteres[lista_indice_caracteres[constantes.posicao_inicial]])
                lista_indice_caracteres.append(constantes.posicao_inicial)
                return toString(lista_senha)
        else:
            # Chama esta Função de Forma Recursiva
            return calculaNovaSenha(indice_lista)
    else:
        lista_senha[indice_lista] = constantes.caracteres[lista_indice_caracteres[indice_lista]]
        return toString(lista_senha)


#======================================================================================================================
# Autor: Cleber
# Descrição: Converte uma Lista em uma String
#======================================================================================================================
def toString(lista):

    return ''.join(lista)


#======================================================================================================================
# Autor: Cleber
# Descrição: Chama a Função Principal para Iniciar o Programa
#======================================================================================================================
main(toString(nome_do_arquivo_RAR))



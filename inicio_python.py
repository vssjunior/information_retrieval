########################### A C E N T U A Ç Ã O ##################
# -*- coding: utf-8 -*-

################## C O N D I C I O N A I S ###########################
# if 1 == 1:
#     print("1");
# elif 2 == 2:
#     print("2");
# else
#     print ("3");

    
# for i in range(10):
#     print(i);

###################### S T R I N G ################################
from platform import architecture


a = "Valdeci \n";
minha_string = "O rato roeu a roupa do rei de Roma";

minha_lista = minha_string.split();
minha_lista_2 = minha_string.split("r");#Quebra removendo o caractere

# print(minha_string.replace("rei", "rainha"));
# print(minha_string.find("rei"));
# print(minha_lista_2);

# print(a);

# print(a.split());

#print(a.strip()); #Remove espaços e caracteres especiais 

#print(a.lower());

# print(a[0]);

# print(len("tamanho"));

################## E N T R A D A     DE    D A D O S    #######################
# Recebendo textos
# meu_texto = input("Digite um texto: ")
# #Recebendo números
# numero_inteiro = int(input("Digite um numero inteiro: "))
# numero_decimal = float(input("Digite um numero decimal: "))#3.3 virgula não funciona

# print(meu_texto, numero_decimal, numero_inteiro);
 
########################## F U N Ç A O ######################
# def soma(x,y):
#     print(x+y);

# soma(2,4);

# def multiplicaco(x,y):
#     return x*y;

# print(multiplicaco(2,3));


###################### A R Q U I V O S ###########################
# arquivo = open("arquivo.txt");
# texto_completo = arquivo.read();
# print(texto_completo);

# linhas = arquivo.readlines();
# print(linhas);

# w = open("arquivo2.txt", "w");
# w.write("Esse eh o meu arquvio");
# w.close();

# arquivo = open("arquivo2.txt");

# print(arquivo.read());



############################## L I S T A S ############################
# minha_lista_2 = [1, "abacaxi", 2, "melancia", 3.3, "abacate"];
# minha_lista_2.append(True); #adiciiona item na lista 

# minha_lista = [1,6,8,3,0,4,5];
# minha_lista.sort();#Só serve para lista com o mesmo tipo de dados
# print(minha_lista);
# minha_lista.sort(reverse=True);#Ordem decrescente
# print(minha_lista);
# minha_lista.reverse();#Inverte a oderm, do último para o primeiro
# print(minha_lista);
# print(minha_lista[2]);

# del minha_lista[2];#apaga segundo elemento

# for item in minha_lista:
#     print(item);

# del minha_lista[:];#apaga toda a lista

# if 2 in minha_lista:
#     print (minha_lista);



########################################## D I C I O N Á R I O S ######################################
meu_dicionario = {"A":"AMOR", "B":"BAIXINHO", "C":"CASA"};

# print(meu_dicionario);
# print(meu_dicionario["A"]);

# for chave in meu_dicionario:
#     print(chave+":"+meu_dicionario[chave]);

# for i in meu_dicionario.items(): #Transforma em uma TUPLA
#     print(i);

# for i in meu_dicionario.values():
#     print(i);


#################################### Nº A L E A T O R I O ################################
import random

numero = random.randint(0, 10);
# print(numero);

# lista_escolha = [6,45,9]
# numero = random.choice(lista_escolha)
# print(numero)


########################### E X C E P T I O N S ######################################
# a = 2
# b = 0
# try:
#     print(a/b)
# except:
#     print("Falha ao realizar a operação, contate o administrador do sistema")


############### L I S T       C O M P R E H E N S I O N ##########################
x = [1,2,3,4,5]
y = []

for i in x:
    y.append(i**2) #Eleva ao quadrado e adiciona a lista Y

# print(x)
# print(y)

# #[valor_a_adicionar laço condição]    
# y = [i**2 for i in x] #Está sem condição, faz o mesmo que o laço de cima
# y = [i**2 for i in x if i%2==1] #Está com condição de inserir somente os impares

# print(x)
# print(y)

############## F U N Ç Ã O       E N U M E R A T E #######################
lista = ["abacate", "bola", "cachorro"]

# for i, nome in enumerate(lista):
#     print(i, nome)

#################### F U N Ç Ã O     M A P  ######################
def dobro(x):
    return x*2

valor = [1,2,3,4,5]

valor_dobrado = map(dobro, valor) #Aplica a função dobro em cada um dos elementos da lista

valor_dobrado = list(valor_dobrado) #Converte o retorno da função MAP para list, já que ela retorna um objeto
# print(valor_dobrado);

########################## F U N Ç Ã O      R E D U C E #######################
from functools import reduce ##Importando função reduce

def soma(x,y):
    return x+y

lista = [1,2,3,5,10,20]


soma = reduce(soma, lista)#Percorre cada elemento da lista vazendo uma soma
print(soma)


###################### F U N Ç Ã O     Z I P #######################
lista1 = [1,2,3,4,5]
lista2 = ["abacate", "bola", "cachorro", "dinheiro", "elefante"]
lista3 = ["R$2,00", "R$5,00", "R$", "R$", "R$"]

for numero, nome, valor in zip(lista1, lista2, lista3):
    print(numero, nome, valor)
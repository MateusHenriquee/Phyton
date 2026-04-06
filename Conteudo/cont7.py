fr= "cursodeanaliseededesenvolvimentodesistemas"    
print(fr[3])                               #isso mostra o espaço da memoria
print(fr[3:40])                            #intervalo de caracteres menos o ultimo caractere
print(fr[3:2])                             #pula de 2 em 2
print(fr[:19])                             #do caractere q escolheu até o final
print(fr[1::19])                           #do caractere q escolheu vai pulando do numero q escolheu ate o final

print(len(fr))                             #conta quantitade de caracteres
print(fr.count("e"))                       #procura o caractere especifico na variavel
print(fr.count("e", 1,19))                 #procura o caractere num intervalo específico
print(fr.find("desenvolvimento"))          #ver onde começa
print(fr.find("android"))                  #-1 pq n tem issae
print("sistemas"in(fr))                    #verifica se aquele conjunto string ta presente na variavel
def verifyLetra(texto):
    qnt = texto.lower().count('a')
    
    if qnt > 0:
        print(f"A letra A aparece {qnt} vez(es) na string.")
    else:
        print("A letra A não aparece na string.")
        

texto = input("Digite uma palavra ou frase que contenham a letra A: ")
verifyLetra(texto)
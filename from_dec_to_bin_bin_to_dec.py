def binario_to_decimale(binario):
    # Conversione da binario a decimale
    decimale = 0
    base = 1  # 2^0
    
    # Itera attraverso i caratteri del numero binario da destra a sinistra
    for cifra in reversed(binario):  # Usa reversed per iterare da destra a sinistra
        if cifra == '1':
            decimale += base
        base *= 2  # Incrementa la potenza di 2
    return decimale

def decimale_to_binario(decimale):
    # Conversione da decimale a binario utilizzando un array (lista)
    if decimale == 0:
        return [0]  # Se il numero è 0, restituisci una lista con un singolo elemento 0
    
    binario = []  # Array per memorizzare i resti della divisione per 2
    
    # Continua a dividere il numero decimale per 2 e salva i resti nell'array
    while decimale > 0:
        resto = decimale % 2
        binario.append(resto)  # Aggiungi il resto alla lista
        decimale //= 2  # Divisione intera per 2
    
    # Inverti l'array per ottenere l'ordine corretto
    binario.reverse()  # Il numero binario viene costruito al contrario
    
    return binario

def is_binario_valido(binario):
    # Controllo se l'input binario è valido (solo 0 e 1)
    for cifra in binario:
        if cifra != '0' and cifra != '1':
            return False
    return True

def main():
    print("Scegli un'opzione:")
    print("1. Converti da binario a decimale")
    print("2. Converti da decimale a binario")
    
    scelta = int(input())
    
    if scelta == 1:
        binario = list(input("Inserisci il numero binario: "))  # Memorizza l'input come una lista di caratteri
        
        # Verifica se l'input binario è valido
        if is_binario_valido(binario):
            decimale = binario_to_decimale(binario)
            print(f"Il numero decimale è: {decimale}")
        else:
            print("Errore: input binario non valido. Inserisci solo '0' e '1'.")
    
    elif scelta == 2:
        decimale = int(input("Inserisci il numero decimale: "))
        binario = decimale_to_binario(decimale)
        print(f"Il numero binario è: {''.join(map(str, binario))}")  # Converte la lista in una stringa
    
    else:
        print("Scelta non valida. Riprova.")

# Esegui il programma principale
main()

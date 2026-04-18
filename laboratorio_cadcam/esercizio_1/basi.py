# ============================================================
# ESERCIZIO 1.1 — Variabili e tipi di dato
# ============================================================

# Le variabili si creano semplicemente assegnando un valore.
# Python capisce da solo il tipo (stringa, numero, decimale).

nome_parte = 'Staffa_superiore' # stringa (testo)
numero_pezzi = 4 # intero (numero senza virgola)
peso_kg = 0.145 # float (numero con virgola)
e_conforme = True # booleano (vero/falso)

# print() stampa un valore sullo schermo.
# La f-string permette di inserire variabili dentro una stringa.
print(f'Parte: {nome_parte}')
print(f'Pezzi: {numero_pezzi}')
print(f'Peso unitario: {peso_kg} kg')
print(f'Peso totale: {numero_pezzi * peso_kg:.3f} kg')

# TODO 1: crea una variabile 'materiale' con il valore 'Al6061'
# TODO 2: stampa la variabile materiale con un messaggio descrittivo

# type() dice di che tipo e' una variabile
print(f'Tipo di nome_parte: {type(nome_parte)}')
print(f'Tipo di numero_pezzi: {type(numero_pezzi)}')

# TODO 3: stampa il tipo di peso_kg e di e_conforme
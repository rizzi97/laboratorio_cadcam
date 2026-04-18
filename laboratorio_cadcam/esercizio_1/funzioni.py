# ============================================================
# ESERCIZIO 1.2 — Funzioni e cicli for
# ============================================================

# Una funzione si definisce con 'def', ha un nome e dei parametri.
# 'return' restituisce il risultato.
def calcola_peso_totale(quantita, peso_unitario):
    """Calcola il peso totale moltiplicando quantita' per peso unitario."""
    peso = quantita * peso_unitario   # calcolo
    return peso                       # restituisce il risultato

# Chiama la funzione con dei valori specifici
risultato = calcola_peso_totale(4, 0.145)
print(f'Peso totale: {risultato} kg')

# TODO 1: crea una funzione 'calcola_costo_totale(quantita, prezzo_unitario)'
#         che restituisce quantita * prezzo_unitario

def calcola_costo_totale(quantita, prezzo_unitario):
    """Ritorna il costo totale moltiplicando la quantitaà per il prezzo unitario. """
    return quantita * prezzo_unitario

# ─── Lista di parti ─────────────────────────────────────────────────────────
# Una lista e' una sequenza ordinata di elementi
distinta_base = [
    {'nome': 'Staffa superiore',  'quantita': 4,  'peso_kg': 0.145},
    {'nome': 'Perno M8',          'quantita': 12, 'peso_kg': 0.025},
    {'nome': 'Rondella piana D8', 'quantita': 24, 'peso_kg': 0.003},
]

# Un ciclo 'for' esegue il codice per ogni elemento della lista
print('\n--- Distinta base ---')
peso_assieme = 0;
for parte in distinta_base:
    # 'parte' e' un dizionario: si accede ai valori con parte['chiave']
    nome     = parte['nome']
    qty      = parte['quantita']
    peso     = parte['peso_kg']
    peso_tot = calcola_peso_totale(qty, peso)
    peso_assieme = peso_assieme + peso_tot
    print(f'{nome:<25} qty={qty:>3}  peso tot={peso_tot:.3f} kg')

print(f'\nPeso TOTALE assieme: {peso_assieme:.3f} kg')

# TODO 2: calcola e stampa il peso TOTALE dell'assieme
#   suggerimento: crea una variabile 'peso_assieme = 0'
#   prima del ciclo, poi aggiungi il peso di ogni parte al ciclo

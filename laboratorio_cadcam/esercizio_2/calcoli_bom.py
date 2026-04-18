# ============================================================
# ESERCIZIO 2.2 — Calcoli con pandas
# ============================================================

import pandas as pd
from pathlib import Path

df = pd.read_csv(Path('esercizio_2') / 'bom_assembly.csv')

# ─── Calcolo su colonne ─────────────────────────────────────────────────────
# Puoi fare operazioni aritmetiche su intere colonne (vettoriale):
# moltiplica OGNI valore di 'quantity' per il corrispondente 'unit_weight_kg'
df['peso_totale_kg'] = df['quantity'] * df['unit_weight_kg']
print('=== PESO TOTALE PER RIGA ===')
print(df[['part_number', 'quantity', 'unit_weight_kg', 'peso_totale_kg']].head(8))

# ─── Statistiche di base ────────────────────────────────────────────────────
# sum() calcola la somma; ignora automaticamente i NaN
peso_assieme = df['peso_totale_kg'].sum()
print(f'\nPeso totale assieme: {peso_assieme:.3f} kg')

# ─── Raggruppare per categoria ───────────────────────────────────────────────
# groupby raggruppa le righe per il valore di una colonna,
# poi applica un'operazione (sum, mean, count...) a ogni gruppo
peso_per_materiale = (
    df.groupby('material')['peso_totale_kg']
      .sum()                   # somma i pesi per ogni materiale
      .sort_values(ascending=False)
      .reset_index()           # trasforma l'indice in colonna
)
print('\n=== PESO TOTALE PER MATERIALE ===')
print(peso_per_materiale)

# TODO 1: calcola il numero di parti (count) per ogni materiale
#   suggerimento: usa .count() invece di .sum()
print('\n=== NUMERI PARTI PER MATERIALE ===')
parti_per_materiale = df.groupby('material')['part_number'].count()
print(parti_per_materiale)

# TODO 2: trova la parte con il peso unitario piu' alto
#   suggerimento: df.sort_values('unit_weight_kg', ascending=False).head(1)
print('\n=== PARTE PIU PESANTE (unitaria) ===')
dataframe_ordinato = df.sort_values('unit_weight_kg',ascending=False)
print(dataframe_ordinato[["part_number","unit_weight_kg"]].head(1))

# ─── Salvare il risultato ────────────────────────────────────────────────────
output_path = Path('esercizio_2') / 'output' / 'peso_per_materiale.csv'
output_path.parent.mkdir(parents=True, exist_ok=True)
peso_per_materiale.to_csv(output_path, index=False)
print(f'\nReport salvato in: {output_path}')

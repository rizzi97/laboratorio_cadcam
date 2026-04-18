# ============================================================
# ESERCIZIO 2.1 — Esplorare un CSV con pandas
# ============================================================
# Prima di eseguire: copia bom_assembly.csv in esercizio_2/
import pandas as pd
from pathlib import Path

# Legge il file CSV e crea un DataFrame (tabella)
df = pd.read_csv(Path('esercizio_2') / 'bom_assembly.csv')

# ─── Esplora la struttura del DataFrame ─────────────────────────────────────
print('=== PRIME 5 RIGHE ===')
print(df.head())              # mostra le prime 5 righe

print('\n=== FORMA DEL DATAFRAME ===')
print(f'Righe: {df.shape[0]}, Colonne: {df.shape[1]}')

print('\n=== NOMI DELLE COLONNE ===')
print(df.columns.tolist())    # lista dei nomi delle colonne

print('\n=== TIPI DI DATO ===')
print(df.dtypes)              # tipo di ogni colonna

print('\n=== VALORI MANCANTI PER COLONNA ===')
print(df.isnull().sum())      # conta i NaN (valori mancanti) per colonna

# ─── Accedere alle colonne ──────────────────────────────────────────────────
print('\n=== COLONNA part_number ===')
print(df['part_number'])      # stampa la colonna part_number

# ─── Filtrare le righe ──────────────────────────────────────────────────────
# Seleziona solo le righe dove la quantita' e' maggiore di 10
molti_pezzi = df[df['quantity'] > 10]
print(f'\nParti con quantita > 10: {len(molti_pezzi)}')
print(molti_pezzi[['part_number', 'description', 'quantity']])

# TODO 1: stampa solo le parti con materiale 'Al6061'
#   suggerimento: df[df['material'] == 'Al6061']
print('\n=== PARTI IN AL6061 ===')
dataframe_al6061 = df[df['material'] == 'Al6061']
print(dataframe_al6061)

# TODO 2: stampa solo le colonne 'part_number' e 'revision'
#   suggerimento: df[['part_number', 'revision']]
print('\n=== COLONNE part_number e revision ===')
print(df[['part_number','revision']])


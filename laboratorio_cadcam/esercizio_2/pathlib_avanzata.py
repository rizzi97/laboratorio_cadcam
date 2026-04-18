# ============================================================
# ESERCIZIO 2.3 — pathlib avanzata: scansione di cartelle
# ============================================================
from pathlib import Path
import shutil

# Usa la cartella modulo1/inbox/ che contiene i file STEP del laboratorio
cartella_step = Path('modulo1') / 'inbox'

# ─── Verifiche di base ──────────────────────────────────────────────────────
if not cartella_step.exists():
    print(f'ATTENZIONE: la cartella {cartella_step} non esiste!')
    print('Crea la cartella modulo1/inbox/ e copiaci i file .step')
else:
    print(f'Cartella trovata: {cartella_step.resolve()}')

# ─── Scansione della cartella ────────────────────────────────────────────────
file_step = list(cartella_step.glob('*.step'))
file_stp  = list(cartella_step.glob('*.stp'))
tutti     = file_step + file_stp

print(f'\nFile STEP trovati: {len(tutti)}')
for file in sorted(tutti):
    dimensione = file.stat().st_size
    print(f'  {file.name:<40}  {dimensione:>8} byte')
    #  {file.name:<40} → allinea a sinistra in 40 caratteri
    #  {dimensione:>8} → allinea a destra in 8 caratteri

# ─── Informazioni su un singolo file ────────────────────────────────────────
if tutti:
    primo = tutti[0]
    print(f'\nDettagli su {primo.name}:')
    print(f'  Percorso completo: {primo.resolve()}')
    print(f'  Cartella padre:   {primo.parent}')
    print(f'  Nome senza estens: {primo.stem}')
    print(f'  Estensione:        {primo.suffix}')

# TODO 1: conta quanti file ci sono in TUTTA la cartella modulo1/
#   suggerimento: usa rglob('*') che cerca anche nelle sottocartelle,
#   poi filtra solo i file con .is_file()

# TODO 2: crea una cartella 'esercizio_2/output/archivio/'
#   e copia in essa tutti i file .step trovati
#   suggerimento: shutil.copy2(sorgente, destinazione)

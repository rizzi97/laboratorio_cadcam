# ============================================================
# ESERCIZIO 1.3 — Leggere e scrivere file con pathlib
# ============================================================

# pathlib.Path e' il modo moderno e portabile di gestire i percorsi.
# Funziona uguale su Windows, Linux e macOS.
from pathlib import Path

# Path('.') indica la cartella corrente.
# / e' usato per unire parti di percorso (come os.path.join ma piu' leggibile).
cartella_output = Path('esercizio_1') / 'output'

# mkdir crea la cartella. parents=True crea anche le cartelle intermedie.
# exist_ok=True non da' errore se la cartella esiste gia'.
cartella_output.mkdir(parents=True, exist_ok=True)
print(f'Cartella creata: {cartella_output}')

# ─── Scrivere un file di testo ──────────────────────────────────────────────
file_output = cartella_output / 'report.txt'

# write_text() scrive una stringa nel file (sovrascrive se esiste)
contenuto = 'Parte: Staffa superiore\nQuantita: 4\nPeso: 0.580 kg\n'
file_output.write_text(contenuto, encoding='utf-8')
print(f'File scritto: {file_output}')

# ─── Leggere un file di testo ───────────────────────────────────────────────
# read_text() legge l'intero contenuto come stringa
testo_letto = file_output.read_text(encoding='utf-8')
print(f'\nContenuto del file:\n{testo_letto}')

# ─── Elencare i file in una cartella ────────────────────────────────────────
# glob('*.txt') trova tutti i file .txt nella cartella
print('File .txt nella cartella output:')
for f in cartella_output.glob('*.txt'):
    print(f'  - {f.name}  ({f.stat().st_size} byte)')

# TODO 1: crea un secondo file 'output/note.txt' con testo a tua scelta

file_output_due = cartella_output / 'note.txt'
file_output_due.write_text("Lezione Cad/CAM 18 Aprile 2026 - Ing. Marco Rizzi", encoding='utf-8')
file_output_due = cartella_output / 'note.txt'
print(f'File scritto: {file_output_due}')

# TODO 2: elenca di nuovo i file e verifica che siano 2

print('File .txt nella cartella output:')
conteggio = 0;
for f in cartella_output.glob('*.txt'):
    conteggio = conteggio + 1
    #print(f'  - {f.name}  ({f.stat().st_size} byte)')

if(conteggio >= 2):
    print("Nella cartella ci sono almeno due file")
else:
    print("Nella cartella non ci sono almeno due file")

# TODO 3: verifica se il file esiste con f.exists() e stampa il risultato
print('\nNome File\tEsiste')
print(f'report.txt\t {file_output.exists()}')
print(f'note.txt\t {file_output_due.exists()}')

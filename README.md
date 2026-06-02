# Bioinformatics Toolkit with Biopython

An educational Python repository that demonstrates the most important Biopython concepts: DNA/RNA/protein sequences, FASTA and GenBank parsing, GC content, transcription, translation, pairwise alignment, motifs, Entrez, and PDB structure parsing.

## Project contents

- `src/sequence_analyzer.py` — DNA analysis: length, GC percentage, complement, reverse complement, transcription, and translation.
- `src/fasta_parser.py` — FASTA/GenBank reading and writing with `Bio.SeqIO` and `SeqRecord`.
- `src/protein_analyzer.py` — protein sequence analysis and amino acid counting.
- `src/gc_plot.py` — GC content plotting for records from a FASTA file.
- `src/alignment_tools.py` — simple pairwise sequence alignment.
- `src/entrez_tools.py` — basic NCBI Entrez search/fetch helpers.
- `src/motif_tools.py` — DNA motif creation and consensus sequence extraction.
- `src/pdb_tools.py` — basic PDB structure parsing.
- `notebooks/` — English learning notebooks with step-by-step examples.
- `docs/` — Biopython tutorial PDF.
- `data/` — small example FASTA files.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run the menu application

```bash
python main.py
```

The menu lets you choose between sequence analysis, FASTA parsing, protein analysis, GC plotting, alignment, and motif creation.

## Examples
## Screenshots

### DNA Sequence Analysis

![DNA Sequence Analysis](images/dna-sequence-analysis.png)

Example of DNA sequence parsing and analysis using Biopython Seq and SeqIO modules.

### Sequence Alignment and Motif Analysis

![Sequence Alignment and Motif Analysis](images/sequence_alignment_and_motif_analysis.png)

Pairwise sequence alignment and motif consensus generation with Biopython.

### NCBI Entrez Search

![NCBI Entrez Search](images/pubmed_search_demo.png)

Searching the PubMed database programmatically through the Entrez API.

### Protein Structure Analysis

![Protein Structure Analysis](images/protein_structure_analysis.png)

Parsing a real Protein Data Bank (PDB) structure and extracting chains, residues and atom statistics.


### DNA analysis

```python
from src.sequence_analyzer import analyze_dna

result = analyze_dna("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
print(result)
```

### FASTA parser

```python
from src.fasta_parser import parse_sequences, summarize_records

records = parse_sequences("data/example.fasta", "fasta")
print(summarize_records(records))
```

### Protein analysis

```python
from src.protein_analyzer import analyze_protein

print(analyze_protein("MAIVMGRWKGAR"))
```

### GC content plot

```python
from src.gc_plot import plot_gc_content

plot_gc_content("data/example.fasta", "outputs/gc_content.png")
```

## Theory to remember

### `Seq`

`Seq` is the core Biopython object for DNA, RNA, or protein sequences. It behaves similarly to a Python string: you can check its length, slice it, count symbols, and search inside it.

### `SeqRecord`

`SeqRecord` stores a sequence together with metadata such as `id`, `name`, `description`, `annotations`, and `seq`.

### `SeqIO`

`SeqIO` is used to read and write biological sequence files, including FASTA and GenBank.

### FASTA vs GenBank

FASTA is a simple format containing an identifier and a sequence. GenBank is richer because it can also store biological annotations.

### Important biological operations

- complement
- reverse complement
- GC content
- transcription: DNA → RNA
- translation: RNA/DNA → protein
- sequence alignment
- motifs and consensus sequences
- PDB structure parsing
- NCBI Entrez search and fetch

## Suggested future improvements

- Add more `pytest` tests.
- Add a full command-line interface with `argparse`.
- Add example GenBank and PDB files.
- Add GitHub Actions for automated tests.
- Add screenshots of generated plots to the README.

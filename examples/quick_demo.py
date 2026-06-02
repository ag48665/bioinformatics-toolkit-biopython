from src.sequence_analyzer import analyze_dna
from src.fasta_parser import parse_sequences, summarize_records
from src.gc_plot import gc_values_from_fasta

print(analyze_dna("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"))
print(summarize_records(parse_sequences("data/example.fasta")))
print(gc_values_from_fasta("data/example.fasta"))

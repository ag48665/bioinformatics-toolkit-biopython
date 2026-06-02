from pathlib import Path

from src.sequence_analyzer import analyze_dna
from src.fasta_parser import parse_sequences, summarize_records
from src.protein_analyzer import analyze_protein
from src.gc_plot import plot_gc_content, gc_values_from_fasta
from src.alignment_tools import global_alignment
from src.motif_tools import create_motif

DATA = Path("data/example.fasta")


def print_menu() -> None:
    print("\nBioinformatics Toolkit")
    print("1. Analyze DNA sequence")
    print("2. Parse FASTA file")
    print("3. Analyze protein sequence")
    print("4. Plot GC content from FASTA")
    print("5. Pairwise alignment")
    print("6. Create DNA motif")
    print("0. Exit")


def main() -> None:
    while True:
        print_menu()
        choice = input("Choose option: ").strip()

        if choice == "1":
            seq = input("DNA sequence: ")
            print(analyze_dna(seq))
        elif choice == "2":
            path = input(f"FASTA path [{DATA}]: ").strip() or str(DATA)
            records = parse_sequences(path, "fasta")
            for summary in summarize_records(records):
                print(summary)
        elif choice == "3":
            seq = input("Protein sequence: ")
            print(analyze_protein(seq))
        elif choice == "4":
            path = input(f"FASTA path [{DATA}]: ").strip() or str(DATA)
            print(gc_values_from_fasta(path))
            print("Saved plot to:", plot_gc_content(path, "outputs/gc_content.png"))
        elif choice == "5":
            seq1 = input("Sequence 1: ")
            seq2 = input("Sequence 2: ")
            print(global_alignment(seq1, seq2))
        elif choice == "6":
            print("Enter motif sequences separated by comma, e.g. ATGC,ATGA,ATGT")
            seqs = [s.strip() for s in input("Sequences: ").split(",") if s.strip()]
            print(create_motif(seqs))
        elif choice == "0":
            break
        else:
            print("Unknown option")


if __name__ == "__main__":
    main()

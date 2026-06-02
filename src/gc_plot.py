"""Plot GC content for sequences in a FASTA file."""
from __future__ import annotations

from pathlib import Path
import matplotlib.pyplot as plt
from Bio.SeqUtils import gc_fraction
from .fasta_parser import parse_sequences


def gc_values_from_fasta(path: str | Path) -> list[tuple[str, float]]:
    records = parse_sequences(path, "fasta")
    return [(record.id, round(gc_fraction(record.seq) * 100, 2)) for record in records]


def plot_gc_content(path: str | Path, output_path: str | Path = "gc_content.png") -> Path:
    values = gc_values_from_fasta(path)
    ids = [item[0] for item in values]
    gc_values = [item[1] for item in values]

    plt.figure(figsize=(8, 4))
    plt.bar(ids, gc_values)
    plt.ylabel("GC content (%)")
    plt.xlabel("Sequence ID")
    plt.title("GC content per FASTA record")
    plt.tight_layout()
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output)
    plt.close()
    return output

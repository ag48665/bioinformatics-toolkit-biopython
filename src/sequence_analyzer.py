"""DNA/RNA sequence analysis utilities using Biopython."""
from __future__ import annotations

from dataclasses import dataclass
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction


@dataclass
class DNAAnalysis:
    sequence: str
    length: int
    gc_percent: float
    complement: str
    reverse_complement: str
    rna: str
    protein: str


def clean_sequence(sequence: str) -> str:
    """Remove whitespace and normalize a biological sequence to uppercase."""
    return "".join(sequence.split()).upper()


def analyze_dna(sequence: str) -> DNAAnalysis:
    """Analyze a DNA sequence: length, GC%, complement, RNA and protein."""
    dna = Seq(clean_sequence(sequence))
    rna = dna.transcribe()
    return DNAAnalysis(
        sequence=str(dna),
        length=len(dna),
        gc_percent=round(gc_fraction(dna) * 100, 2),
        complement=str(dna.complement()),
        reverse_complement=str(dna.reverse_complement()),
        rna=str(rna),
        protein=str(rna.translate(to_stop=False)),
    )


def transcribe_dna(sequence: str) -> str:
    return str(Seq(clean_sequence(sequence)).transcribe())


def translate_sequence(sequence: str, to_stop: bool = False) -> str:
    """Translate DNA or RNA sequence to protein."""
    seq = Seq(clean_sequence(sequence))
    if "T" in seq:
        seq = seq.transcribe()
    return str(seq.translate(to_stop=to_stop))

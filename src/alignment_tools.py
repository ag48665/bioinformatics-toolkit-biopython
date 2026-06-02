"""Simple pairwise alignment example."""
from __future__ import annotations
from Bio import pairwise2
from Bio.pairwise2 import format_alignment


def global_alignment(seq1: str, seq2: str) -> str:
    """Return the best global alignment using simple match/mismatch scores."""
    alignments = pairwise2.align.globalxx(seq1.upper(), seq2.upper())
    return format_alignment(*alignments[0]) if alignments else "No alignment found"

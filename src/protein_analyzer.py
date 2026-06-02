"""Protein sequence utilities."""
from __future__ import annotations

from collections import Counter
from Bio.Data import IUPACData

VALID_AA = set(IUPACData.protein_letters)


def analyze_protein(sequence: str) -> dict[str, object]:
    """Analyze protein length, amino-acid counts and validity."""
    seq = "".join(sequence.split()).upper()
    counts = Counter(seq)
    invalid = sorted(set(seq) - VALID_AA - {"*", "X"})
    return {
        "sequence": seq,
        "length": len(seq),
        "amino_acid_counts": dict(sorted(counts.items())),
        "invalid_symbols": invalid,
    }

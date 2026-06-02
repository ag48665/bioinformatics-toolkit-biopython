"""DNA motif examples."""
from __future__ import annotations
from Bio import motifs
from Bio.Seq import Seq


def create_motif(sequences: list[str]) -> dict[str, object]:
    instances = [Seq(seq.upper()) for seq in sequences]
    motif = motifs.create(instances)
    return {
        "consensus": str(motif.consensus),
        "degenerate_consensus": str(motif.degenerate_consensus),
        "counts": {base: list(motif.counts[base]) for base in "ACGT"},
    }

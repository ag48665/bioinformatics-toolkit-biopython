"""FASTA and GenBank parsing/writing examples with Bio.SeqIO."""
from __future__ import annotations

from pathlib import Path
from typing import Iterable
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


def parse_sequences(path: str | Path, file_format: str = "fasta") -> list[SeqRecord]:
    """Read sequences from FASTA/GenBank/etc. Returns SeqRecord objects."""
    return list(SeqIO.parse(str(path), file_format))


def summarize_records(records: Iterable[SeqRecord]) -> list[dict[str, object]]:
    """Extract common SeqRecord fields into simple dictionaries."""
    return [
        {
            "id": record.id,
            "name": record.name,
            "description": record.description,
            "length": len(record.seq),
            "sequence": str(record.seq),
            "annotations": dict(record.annotations),
        }
        for record in records
    ]


def convert_format(input_path: str | Path, output_path: str | Path, input_format: str, output_format: str) -> int:
    """Convert sequence files, e.g. FASTA -> GenBank when annotations allow it."""
    records = parse_sequences(input_path, input_format)
    return SeqIO.write(records, str(output_path), output_format)

"""NCBI Entrez helpers. Requires internet and a valid email address."""
from __future__ import annotations
from Bio import Entrez


def search_pubmed(term: str, email: str, max_results: int = 5) -> list[str]:
    Entrez.email = email
    handle = Entrez.esearch(db="pubmed", term=term, retmax=max_results)
    record = Entrez.read(handle)
    handle.close()
    return list(record.get("IdList", []))


def fetch_fasta(accession: str, email: str) -> str:
    Entrez.email = email
    handle = Entrez.efetch(db="nucleotide", id=accession, rettype="fasta", retmode="text")
    data = handle.read()
    handle.close()
    return data

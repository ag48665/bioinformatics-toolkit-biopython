"""Basic PDB structure parsing helper."""
from __future__ import annotations
from pathlib import Path
from Bio.PDB import PDBParser


def summarize_pdb(path: str | Path, structure_id: str = "structure") -> dict[str, int]:
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure(structure_id, str(path))
    models = list(structure.get_models())
    chains = list(structure.get_chains())
    residues = list(structure.get_residues())
    atoms = list(structure.get_atoms())
    return {
        "models": len(models),
        "chains": len(chains),
        "residues": len(residues),
        "atoms": len(atoms),
    }

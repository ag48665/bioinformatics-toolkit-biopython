from src.sequence_analyzer import analyze_dna, transcribe_dna, translate_sequence


def test_analyze_dna_basic():
    result = analyze_dna("ATGC")
    assert result.length == 4
    assert result.gc_percent == 50.0
    assert result.rna == "AUGC"


def test_transcribe_dna():
    assert transcribe_dna("ATGC") == "AUGC"


def test_translate_sequence():
    assert translate_sequence("ATGGCC", to_stop=True) == "MA"

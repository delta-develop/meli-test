import pytest
from app.scripts.dna_matrix import DNAMatrix


@pytest.fixture
def bad_matrix():
    matrix = [
        "TAAATT",
        "GGGATT",
        "CCCAGC",
        "TTAGGT",
        "GACATT",
        "CTCTAG",
    ]

    return DNAMatrix(matrix)


@pytest.fixture
def single_matrix():
    matrix = [
        "GAAAAG",
        "GATCTC",
        "AAGGGT",
        "GATCCT",
        "TGAGTG",
        "GCCACC",
    ]

    return DNAMatrix(matrix)


@pytest.fixture
def horizontal_matrix():
    matrix = [
        "AAAAAA",
        "CCCCCC",
        "GGGGGG",
        "TTTTTT",
        "AAAAAA",
        "CCCCCC",
    ]

    return DNAMatrix(matrix)


@pytest.fixture
def vertical_matrix():
    matrix = [
        "CTCTCT",
        "TCTCTC",
        "CGAGGT",
        "TGATCC",
        "CGACTT",
        "TGATCC",
    ]

    return DNAMatrix(matrix)


@pytest.fixture
def diagonal_matrix():
    matrix = [
        "CTTTCA",
        "TCCCAT",
        "CTTACG",
        "CTATGT",
        "CACGCT",
        "ATGTTC",
    ]

    return DNAMatrix(matrix)


@pytest.fixture
def angled_matrix():
    matrix = [
        "TCTCTC",
        "TAAAAT",
        "CGCTCC",
        "TGTCTT",
        "CGTTTC",
        "TGCCCT",
    ]

    return DNAMatrix(matrix)


@pytest.fixture
def empty_matrix():
    matrix = [
        "ACGTAC",
        "GTACGT",
        "ACGTAC",
        "GTACGT",
        "ACGTAC",
        "GTACGT",
    ]

    return DNAMatrix(matrix)


@pytest.fixture
def diagonal_matrix_lower():
    matrix = [
        "CCCTTT",
        "ATTCCC",
        "GACTCT",
        "TGATTT",
        "TTGACC",
        "TTTGCC",
    ]

    return DNAMatrix(matrix)


@pytest.fixture
def almost_mutant_horizontal_matrix():
    matrix = [
        "TAAAAT",
        "TTCCCT",
        "AGGGAA",
        "AATTTA",
        "GCTTGC",
        "GACTGA",
    ]

    return DNAMatrix(matrix)


@pytest.fixture
def almost_mutant_vertical_matrix():
    matrix = [
        "TAGGGT",
        "TACAAT",
        "TACGCA",
        "GACGTC",
        "GTTGTA",
        "GTTCTA",
    ]

    return DNAMatrix(matrix)

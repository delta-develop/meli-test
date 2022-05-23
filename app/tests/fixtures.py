import pytest
from app.scripts.dna_matrix import DNAMatrix


@pytest.fixture
def bad_matrix() -> DNAMatrix:
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
def invalid_matrix() -> DNAMatrix:
    matrix = [
        "XAGGGT",
        "TACAAT",
        "TACGCA",
        "GACGTC",
        "GTTGTA",
        "GTTCTA",
    ]

    return DNAMatrix(matrix)


@pytest.fixture
def single_matrix() -> DNAMatrix:
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
def horizontal_matrix() -> DNAMatrix:
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
def vertical_matrix() -> DNAMatrix:
    matrix = [
        "CTCTCT",
        "TCTCCC",
        "TGAGGT",
        "TGATCC",
        "TGACTT",
        "TGATCC",
    ]

    return DNAMatrix(matrix)


@pytest.fixture
def diagonal_matrix() -> DNAMatrix:
    matrix = [
        "CTTTCA",
        "TCCCAT",
        "CTCACG",
        "CCATGT",
        "TACGCT",
        "ATGTTC",
    ]

    return DNAMatrix(matrix)


@pytest.fixture
def angled_matrix() -> DNAMatrix:
    matrix = [
        "TCTCTC",
        "TAAAAT",
        "CGCTCC",
        "TGTCTT",
        "CGTTTC",
        "TGCCCC",
    ]

    return DNAMatrix(matrix)


@pytest.fixture
def empty_matrix() -> DNAMatrix:
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
def diagonal_matrix_lower() -> DNAMatrix:
    matrix = [
        "TCCTTT",
        "ATTCCC",
        "GATTCT",
        "TGATTT",
        "TTGACC",
        "TTTGCC",
    ]

    return DNAMatrix(matrix)


@pytest.fixture
def diagonal_matrix_upper() -> DNAMatrix:
    matrix = [
        "TTCTTT",
        "GTTCCC",
        "GGTTCT",
        "TGCTTC",
        "TTGATC",
        "TTTGCC",
    ]

    return DNAMatrix(matrix)


@pytest.fixture
def almost_mutant_horizontal_matrix() -> DNAMatrix:
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
def almost_mutant_vertical_matrix() -> DNAMatrix:
    matrix = [
        "TAGGGT",
        "TACAAT",
        "TACGCA",
        "GACGTC",
        "GTTGTA",
        "GTTCTA",
    ]

    return DNAMatrix(matrix)

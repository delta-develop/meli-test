import pytest
from app.scripts.dna_matrix import DNAMatrix


@pytest.fixture
def bad_matrix():
    matrix = [
        "_AAA__",
        "___A__",
        "___A__",
        "__A___",
        "_A_A__",
        "____A_",
    ]

    return DNAMatrix(matrix)


@pytest.fixture
def single_matrix():
    matrix = [
        "_AAAA_",
        "_A____",
        "AA____",
        "_A____",
        "__A___",
        "___A__",
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
        "______",
        "______",
        "_GA___",
        "_GA___",
        "_GA___",
        "_GA___",
    ]

    return DNAMatrix(matrix)


@pytest.fixture
def diagonal_matrix():
    matrix = [
        "_____A",
        "____A_",
        "___A_G",
        "__A_G_",
        "_A_G__",
        "A_G___",
    ]

    return DNAMatrix(matrix)


@pytest.fixture
def angled_matrix():
    matrix = [
        "______",
        "_AAAA_",
        "_G____",
        "_G____",
        "_G____",
        "_G____",
    ]

    return DNAMatrix(matrix)


@pytest.fixture
def empty_matrix():
    matrix = [
        "______",
        "______",
        "______",
        "______",
        "______",
        "______",
    ]

    return DNAMatrix(matrix)


@pytest.fixture
def diagonal_matrix_lower():
    matrix = [
        "______",
        "A_____",
        "GA____",
        "_GA___",
        "__GA__",
        "___G__",
    ]

    return DNAMatrix(matrix)


@pytest.fixture
def almost_mutant_horizontal_matrix():
    matrix = [
        "_AAAA_",
        "__CCC_",
        "_GGG__",
        "__TTT_",
        "______",
        "______",
    ]

    return DNAMatrix(matrix)


@pytest.fixture
def almost_mutant_vertical_matrix():
    matrix = [
        "_A____",
        "_AC___",
        "_ACG__",
        "_ACGT_",
        "___GT_",
        "____T_",
    ]

    return DNAMatrix(matrix)

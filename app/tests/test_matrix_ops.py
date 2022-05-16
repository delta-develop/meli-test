import pytest
from app.scripts.dna_matrix import DNAMatrix
from app.utils.helpers import print_matrix


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


def test_matrix_rotation(horizontal_matrix):
    rotated_matrix = ["ACGTAC", "ACGTAC", "ACGTAC", "ACGTAC", "ACGTAC", "ACGTAC"]

    horizontal_matrix.rotate_matrix_90_deg()

    assert horizontal_matrix.dna_sequences == rotated_matrix


def test_pattern_lookup(horizontal_matrix):
    first_sequence = horizontal_matrix.dna_sequences[0]
    second_sequence = horizontal_matrix.dna_sequences[1]

    first_result = horizontal_matrix.pattern_lookup(first_sequence)
    second_result = horizontal_matrix.pattern_lookup(second_sequence)

    assert first_result == False
    assert second_result == True


def test_convert_diagonal_to_string(horizontal_matrix):
    principal_diagonal = "ACGTAC"
    matrix_diagonal = horizontal_matrix.convert_diagonal_to_string(i=0, j=0)

    assert principal_diagonal == matrix_diagonal


def test_row_search(horizontal_matrix):

    assert horizontal_matrix.row_search() == True

    horizontal_matrix.rotate_matrix_90_deg()
    horizontal_matrix.coincidences = 0

    assert horizontal_matrix.row_search() == False


def test_diagonal_search(diagonal_matrix):

    assert diagonal_matrix.diagonal_search() == False

    diagonal_matrix.rotate_matrix_90_deg()

    assert diagonal_matrix.diagonal_search() == True


def test_diagonal_upper(diagonal_matrix_lower):

    assert diagonal_matrix_lower.diagonal_search() == True


def test_no_coincidences(bad_matrix):

    assert bad_matrix.row_search() == False

    assert bad_matrix.diagonal_search() == False

    bad_matrix.rotate_matrix_90_deg()

    assert bad_matrix.row_search() == False

    assert bad_matrix.diagonal_search() == False


def test_single_coincidence(single_matrix):

    assert single_matrix.row_search() == False
    single_matrix.coincidences = 0

    assert single_matrix.diagonal_search() == False
    single_matrix.coincidences = 0

    single_matrix.rotate_matrix_90_deg()

    assert single_matrix.row_search() == False
    single_matrix.coincidences = 0

    assert single_matrix.diagonal_search() == False

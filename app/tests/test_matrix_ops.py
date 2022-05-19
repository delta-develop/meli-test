from app.tests.fixtures import (
    bad_matrix,
    single_matrix,
    horizontal_matrix,
    diagonal_matrix,
    angled_matrix,
    empty_matrix,
    diagonal_matrix_lower,
)
import pytest


@pytest.mark.asyncio
async def test_matrix_rotation(horizontal_matrix):
    rotated_matrix = ["ACGTAC", "ACGTAC", "ACGTAC", "ACGTAC", "ACGTAC", "ACGTAC"]

    await horizontal_matrix.rotate_matrix_90_deg()

    assert horizontal_matrix.dna_sequences == rotated_matrix


@pytest.mark.asyncio
async def test_pattern_lookup(horizontal_matrix):
    first_sequence = horizontal_matrix.dna_sequences[0]
    second_sequence = horizontal_matrix.dna_sequences[1]

    first_result = await horizontal_matrix.pattern_lookup(first_sequence)
    second_result = await horizontal_matrix.pattern_lookup(second_sequence)

    assert first_result == False
    assert second_result == True


@pytest.mark.asyncio
async def test_convert_diagonal_to_string(horizontal_matrix):
    principal_diagonal = "ACGTAC"
    matrix_diagonal = await horizontal_matrix.convert_diagonal_to_string(i=0, j=0)

    assert principal_diagonal == matrix_diagonal


@pytest.mark.asyncio
async def test_row_search(horizontal_matrix):

    assert await horizontal_matrix.row_search() == True

    await horizontal_matrix.rotate_matrix_90_deg()
    horizontal_matrix.coincidences = 0

    assert await horizontal_matrix.row_search() == False


@pytest.mark.asyncio
async def test_diagonal_search(diagonal_matrix):

    assert await diagonal_matrix.diagonal_search() == False

    await diagonal_matrix.rotate_matrix_90_deg()

    assert await diagonal_matrix.diagonal_search() == True


@pytest.mark.asyncio
async def test_diagonal_upper(diagonal_matrix_lower):

    assert await diagonal_matrix_lower.diagonal_search() == True


@pytest.mark.asyncio
async def test_no_coincidences(bad_matrix):

    assert await bad_matrix.row_search() == False

    assert await bad_matrix.diagonal_search() == False

    await bad_matrix.rotate_matrix_90_deg()

    assert await bad_matrix.row_search() == False

    assert await bad_matrix.diagonal_search() == False


@pytest.mark.asyncio
async def test_single_coincidence(single_matrix):

    assert await single_matrix.row_search() == False
    single_matrix.coincidences = 0

    assert await single_matrix.diagonal_search() == False
    single_matrix.coincidences = 0

    await single_matrix.rotate_matrix_90_deg()

    assert await single_matrix.row_search() == False
    single_matrix.coincidences = 0

    assert await single_matrix.diagonal_search() == False

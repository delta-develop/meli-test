from app.tests.fixtures import (
    bad_matrix,
    single_matrix,
    diagonal_matrix,
    diagonal_matrix_lower,
    angled_matrix,
    empty_matrix,
    horizontal_matrix,
    almost_mutant_horizontal_matrix,
    almost_mutant_vertical_matrix,
    vertical_matrix,
)
from app.utils.helpers import configure_handlers
import pytest
from app.scripts.person import Person


@pytest.fixture
def main_handler():
    return configure_handlers()


@pytest.mark.asyncio
async def test_horizontal_matrix(horizontal_matrix, main_handler):
    p = Person(horizontal_matrix.dna_sequences)

    assert await p.is_mutant(main_handler) == True


@pytest.mark.asyncio
async def test_diagonal_matrix(diagonal_matrix_lower, main_handler):
    p = Person(diagonal_matrix_lower.dna_sequences)

    assert await p.is_mutant(main_handler) == True


@pytest.mark.asyncio
async def test_vertical_matrix(vertical_matrix, main_handler):
    p = Person(vertical_matrix.dna_sequences)

    assert await p.is_mutant(main_handler) == True


@pytest.mark.asyncio
async def test_inverted_diagonal_matrix(diagonal_matrix, main_handler):
    p = Person(diagonal_matrix.dna_sequences)

    assert await p.is_mutant(main_handler) == True


@pytest.mark.asyncio
async def test_not_mutant_matrix(bad_matrix, main_handler):
    p = Person(bad_matrix.dna_sequences)

    assert await p.is_mutant(main_handler) == False


@pytest.mark.asyncio
async def test_angled_matrix(angled_matrix, main_handler):
    p = Person(angled_matrix.dna_sequences)

    assert await p.is_mutant(main_handler) == True


@pytest.mark.asyncio
async def test_empty_matrix(empty_matrix, main_handler):
    p = Person(empty_matrix.dna_sequences)

    assert await p.is_mutant(main_handler) == False


@pytest.mark.asyncio
async def test_almost_mutant_horizontal_matrix(
    almost_mutant_horizontal_matrix, main_handler
):
    p = Person(almost_mutant_horizontal_matrix.dna_sequences)

    assert await p.is_mutant(main_handler) == False


@pytest.mark.asyncio
async def test_almost_mutant_vertical_matrix(
    almost_mutant_vertical_matrix, main_handler
):
    p = Person(almost_mutant_vertical_matrix.dna_sequences)

    assert await p.is_mutant(main_handler) == False

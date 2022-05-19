from app.scripts.dna_handlers import (
    ColumnHandler,
    LeftDiagonalHandler,
    RightDiagonalHandler,
    RowHandler,
)


def configure_handlers():
    row = RowHandler()
    right_diagonal = RightDiagonalHandler()
    left_diagonal = LeftDiagonalHandler()
    column = ColumnHandler()

    row.set_next(right_diagonal).set_next(column).set_next(left_diagonal)

    return row

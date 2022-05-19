from app.scripts.dna_handlers import (
    ColumnHandler,
    LeftDiagonalHandler,
    RightDiagonalHandler,
    RowHandler,
)


def configure_handlers():
    """Function to configure the order of the responsability chain-

    Returns:
        _type_: Inscance of the first chain link to start operating.
    """
    row = RowHandler()
    right_diagonal = RightDiagonalHandler()
    left_diagonal = LeftDiagonalHandler()
    column = ColumnHandler()

    row.set_next(right_diagonal).set_next(column).set_next(left_diagonal)

    return row

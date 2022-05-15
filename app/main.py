from fastapi import FastAPI, Response
from app.scripts.person import Person
from app.utils.helpers import generate_matrix, print_matrix
from app.scripts.dna_handlers import (
    RowHandler,
    RightDiagonalHandler,
    LeftDiagonalHandler,
    ColumnHandler,
)

app = FastAPI()

row = RowHandler()
right_diagonal = RightDiagonalHandler()
left_diagonal = LeftDiagonalHandler()
column = ColumnHandler()

row.set_next(right_diagonal).set_next(column).set_next(left_diagonal)


@app.post("/")
async def read_root(body: dict, response: Response):
    dna_matrix = generate_matrix(size=4)
    print("------  OOP -----")
    p = Person(dna_matrix)
    p.is_mutant(row)

    return {"is_mutant": False}

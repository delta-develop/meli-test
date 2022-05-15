from fastapi import FastAPI, Response
from app.scripts.is_mutant import is_mutant
from app.scripts.person import Person
from app.utils.helpers import generate_matrix

app = FastAPI()


@app.post("/")
def read_root(body: dict, response: Response):
    dna_matrix = generate_matrix(size=10000)
    print("------  OOP -----")
    p = Person(dna_matrix)
    p.is_mutant()
    print("\n\n------  Only functions -----")
    is_mutant(dna_matrix)
    print("------  Only functions -----\n\n")

    return {"is_mutant": False}

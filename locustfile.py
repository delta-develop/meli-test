from locust import task, FastHttpUser
from random import randint

MINIMUM_MATRIX_SIZE = 6
MAXIMUM_MATRIX_SIZE = 10


class HelloWorldUser(FastHttpUser):
    @task
    def is_mutant(self):
        matrix_size = generate_random_size(MINIMUM_MATRIX_SIZE, MAXIMUM_MATRIX_SIZE)
        self.client.post(
            "/mutant/",
            json={"dna": generate_dna(matrix_size)},
        )


def generate_dna(size):
    a = ["A", "C", "G", "T"]
    return ["".join([a[randint(0, 3)] for _ in range(size)]) for __ in range(size)]


def generate_random_size(min_size, max_size):
    return randint(min_size, max_size)

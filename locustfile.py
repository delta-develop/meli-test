from locust import task, FastHttpUser
from random import randint


class HelloWorldUser(FastHttpUser):
    @task
    def is_mutant(self):
        self.client.post(
            "/mutant/",
            json={"dna": generate_dna(randint(6, 8))},
        )


def generate_dna(size):
    a = ["A", "C", "G", "T"]
    return ["".join([a[randint(0, 3)] for _ in range(size)]) for __ in range(size)]

from locust import task, FastHttpUser
from random import randint


class HelloWorldUser(FastHttpUser):
    @task
    def is_mutant(self):
        self.client.post(
            "/mutant/",
            json={
                "dna": [
                    "AAAAAA",
                    "CCCCCC",
                    "GGGGGG",
                    "TTTTTT",
                    "AAAAAA",
                    "CCCCCC",
                ]
            },
        )


def generate_dna():
    a = ["A", "C", "G", "T"]
    return ["".join([a[randint(0, 3)] for _ in range(4)]) for __ in range(4)]
    # @task
    # def not_mutant(self):
    #     self.client.post(
    #         "/mutant/",
    #         json={"dna": ["ATGCGA", "CAGTTC", "TTATGC", "AGAAGG", "CCCTTA", "TCCCGG"]},
    #     )

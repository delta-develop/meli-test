from locust import task, FastHttpUser


class HelloWorldUser(FastHttpUser):
    @task
    def hello_world(self):
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

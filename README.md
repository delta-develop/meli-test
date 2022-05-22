# Software Development Engineer test for Mercado Libre

## The problem

Magneto want to recruit as many mutants as possible so he can fight the X-Men.

He has hired you to develop a project that detects if a human is mutant based on his DNA sequence.

For that he has asked you to create a program with a method or function with the following signature:

```python
is_mutant(dna: str) -> bool
```

Where you will receive as a parameter an array of Strings that represent each row of a table of (NxN)
with the DNA sequence. The characters of the Strings can only be: ```[A, T, C, G]``` which represents each
nitrogenous base of the DNA.

![example](/assets/example.png)

You will know if a humant is mutant, if you find more than a sequence of four letters equal, obliquely, horizontally
or vertically.

**Example (mutant case)**

```python
dna = {
    "ATGCGA",
    "CAGTGC",
    "TTATGT",
    "AGAAGG",
    "CCCCTA",
    "TCACTG"
    }
```
In this case the call to ```is_mutant(dna)``` function returns ```True```

---

## The challenges

1. Create a application which accomplish with the method requested by Magneto.
2. Create a REST API.
   1. Host that API in a free cloud computing.
   2. Create the ```/mutant/``` service where it can be detected if a human is a mutant by sending the DNA sequence via HTTP
   POST with a json which has the following format: <br>
   ```POST -> /mutant/ {"dna":["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]}```
   3. In case of verifying a mutant, it should return an ```HTTP 200-OK``` otherwise ```HTTP 403-Forbidden```
3. Attach a database, which saves the DNA's verified with the API.
   1. Only one record per DNA register.
   2. Expose an extra service ```/stats/``` which returns a json with the DNA verification statistics: <br>
   ```{"count_mutant_dna":40,"count_human_dna":100,"ratio":0.4} ```
   3. Keep in mind that the API cna receive aggresive traffic fluctuations (between 100 and 1 million requests per second).
   4. Unit tests coverage greater than 80%.

---

## The solution

### Dependences
- [Docker](https://docs.docker.com/engine/install/)
- [Poetry](https://python-poetry.org/docs/)
- [Python ^3.10](https://github.com/pyenv/pyenv) I recommend Pyenv
- .env file (.env.example is ready to be used)

### Understanding .env file
```sh
MONGO_HOST = "localhost" # Where is MongoDB running
MONGO_PORT = "27017" # MongoDB port
DBUSERNAME = "username" # MongoDB username
DBPASSWORD = "password" # MongoDB password

ENVIRONMENT = "PROD" # API environment, could be "PROD" or "DEV" and will write on different db
MAX_QUEUE_SIZE = 5 # The requests queue sie before being emptied (you'll undersant later)
EMPTYING_TIME = 20 # The time to wait until emptying the queue even if it is not full
MINIMUM_COINCIDENCES = 3 # Minimum coincidences to consider a human, mutant.,„„„„„„„„„„„„„„„„,,,,,,,,,,,,,,,,,,

WORKER_CLASS = "uvicorn.workers.UvicornWorker" # Worker class for gunicorn to run the app
```

### Running the application
Once the depencences are installed and the .env file is properly configured, there are two ways to run the application, one using only `make` command for MongoDB, Mongo Express and FastAPI, and the other running FastAPI independently.


- Using only `make` for `docker compose`, this will create three containers for FastAPI, MongoDB and Mongo Express, ensure port 8000, 8081 and 27017 are not busy.
 ```sh
 # Afer downloading the repo
$ cd /path/to/the/downloaded/repo/meli-test
$ make up
 ```

- Using docker only for database and database interface. For this case its neccesary first install project dependences.

```sh
# Afer downloading the repo
$ cd /path/to/the/downloaded/repo/meli-test

# Initialize virtual env and install dependences
$ poetry shell
$ poetry install

# Set up MongoDB
$ make up_only_db

# Using uvicorn (--workers is optional)
$ uvicorn app.app:app --host 127.0.0.1 --port 8000 --workers 2

# Using gunicorn
$ gunicorn app.app:app 0.0.0.0:8000 --workers 2 --worker-class uvicorn.workers.UvicornWorkers --threads 2

# --workers --worker-class and --threads are optional but if
# you use it, at least --workers must be with --worker-class
# Just use one of them.
```

### Runining the Unit Tests

```sh
# With the virtual environment activated.

$ make run_tests
```

### Runining the Test Coverage Report

```sh
# With the virtual environment activated.

$ make coverage_report
```

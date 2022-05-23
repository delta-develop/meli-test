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

# API URL: http://ec2-54-160-205-255.compute-1.amazonaws.com/

---
## The solution

### Dependences
- [Docker](https://docs.docker.com/engine/install/)
- [Poetry](https://python-poetry.org/docs/)
- [Python ^3.10](https://github.com/pyenv/pyenv) I recommend Pyenv
- .env file (.env.example is ready to be used)

### Understanding .env file
```sh
# AWS Config
MONGO_HOST = "ec2-54-92-200-9.compute-1.amazonaws.com"
DBPASSWORD = "mongo_server_password" # MongoDB password
ENVIRONMENT = "PROD" # API environment, could be "PROD" or "DEV" and will write on different db
MAX_QUEUE_SIZE = 1000 # The requests queue sie before being emptied (you'll undersant later)
EMPTYING_TIME = 60 # The time to wait until emptying the queue even if it is not full

# Local Config
# MONGO_HOST = "127.0.0.1"  # Only for local configuration
# DBPASSWORD = "root"
# ENVIRONMENT = "DEV"
# MAX_QUEUE_SIZE = 500
# EMPTYING_TIME = 60

# Testing Config
# ENVIRONMENT = "TESTING"
# MAX_QUEUE_SIZE = 3
# EMPTYING_TIME = 20

# General configurations
MONGO_PORT = 27017 # MongoDB port
DBUSERNAME = "root" # MongoDB username

WORKER_CLASS = "uvicorn.workers.UvicornWorker" # Worker class for gunicorn to run the app
MINIMUM_COINCIDENCES = 3 # Minimum coincidences to consider a human, mutant
```

## Note:
In case you need to run the application in localhost, please uncomment the `Local Config` section and comment the `AWS Config` and `Testing Config` sections. Otherwise, the application may not work properly.

<br>

---

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

Last coverage report

```
Name                                    Stmts   Miss  Cover   Missing
---------------------------------------------------------------------
app/__init__.py                             0      0   100%
app/app.py                                 24      5    79%   27, 33-34, 45-46
app/db/__init__.py                          0      0   100%
app/db/operations.py                       19      6    68%   14-15, 60-61, 64-65
app/models/__init__.py                      0      0   100%
app/models/dna_matrix.py                    4      0   100%
app/orchestator/__init__.py                 0      0   100%
app/orchestator/orchestator.py             26      0   100%
app/routes/__init__.py                      0      0   100%
app/routes/mutant_router.py                 9      0   100%
app/routes/stats_router.py                  7      0   100%
app/scripts/__init__.py                     0      0   100%
app/scripts/dna_handler_definition.py      19      2    89%   19, 28
app/scripts/dna_handlers.py                29      0   100%
app/scripts/dna_matrix.py                  51      0   100%
app/scripts/person.py                       9      0   100%
app/settings/__init__.py                    0      0   100%
app/settings/settings.py                   39      8    79%   40-43, 57-58, 63-64
app/tests/__init__.py                       0      0   100%
app/tests/conftest.py                       8      0   100%
app/tests/fixtures.py                      50      0   100%
app/tests/test_handlers.py                 47      0   100%
app/tests/test_integration.py              35      0   100%
app/tests/test_matrix_ops.py               62      0   100%
app/tests/test_orchestator.py              39      0   100%
app/tests/test_queue.py                    33      0   100%
app/utils/__init__.py                       0      0   100%
app/utils/helpers.py                        8      0   100%
app/utils/queue.py                         26      0   100%
---------------------------------------------------------------------
TOTAL                                     544     21    96%
```

Theres an additional mini documentation which give the opportunnity to tests some endpoints, it could be accesed using `/docs/` endpoints.

## Author: Leonardo Daniel Hernández García
### contact: leohg.ipn@gmail.com

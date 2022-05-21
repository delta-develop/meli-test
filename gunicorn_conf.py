from multiprocessing import cpu_count

# Socket Path
bind = "unix:/home/meli-test/gunicorn.sock"

# Worker Options
workers = cpu_count() + 1
worker_class = "uvicorn.workers.UvicornWorker"

# Logging Options
loglevel = "debug"
accesslog = "/home/meli-test/access_log"
errorlog = "/home/meli-test/error_log"

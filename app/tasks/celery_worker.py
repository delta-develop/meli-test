from operator import is_
from celery import Celery
from app.scripts.person import Person
from app.utils.helpers import configure_handlers

celery = Celery("tasks", broker="redis://127.0.0.1:6379")
default_config = "app.tasks.celeryconfig"
celery.config_from_object(default_config)
main_handler = configure_handlers()


@celery.task
def test(data):

    return data

from huey import MemoryHuey

from src.tasks import schedule_tasks


def test_schedule_tasks(seed_data):
    # We want to make sure that this doesn't raise an exception... with respect to the
    # actual running of the tasks, well, I hope the server is correctly configured!
    huey = MemoryHuey()
    schedule_tasks(huey)

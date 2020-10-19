from huey.contrib.mini import MiniHuey

from backend.tasks import schedule_and_start


def test_schedule_and_start():
    # We want to make sure that this doesn't raise an exception... with respect to the
    # actual running of the tasks, well, I hope the server is correctly configured!
    huey = MiniHuey()
    schedule_and_start(huey)
    huey.stop()

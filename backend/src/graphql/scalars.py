import calendar
from datetime import datetime

from ariadne import ScalarType

posix_time_scalar = ScalarType("PosixTime")


@posix_time_scalar.serializer
def serialize_posix_time(value: datetime) -> int:
    return calendar.timegm(value.timetuple())

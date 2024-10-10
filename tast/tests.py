from repository.accident_repository import get_accidents_by_beat,find_by_date
from services.service import get_time


def test_get_accidents_by_beat():
    result = get_accidents_by_beat(411)
    assert result['accident_count'] == 84


def test_get_accidents_by_date():
    beat = "1654"
    time_period = 'month'
    start_date = '12/09/2021'
    start_date, end_date = get_time(time_period, start_date)
    result = find_by_date(beat,start_date, end_date)
    assert result['total_accidents'] == 20


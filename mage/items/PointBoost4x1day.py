import datetime

from mage.items.PointBoost import PointBoost


class PointBoost4x1day(PointBoost):
    name = "PointBoost(4x1day)"
    is_enabled = True
    price = 50
    BOOST_FACTOR = 4
    TIMEDELTA = datetime.timedelta(days=1)


    def __init__(self, *args, **kwargs):
        super(PointBoost, self).__init__(*args, **kwargs)
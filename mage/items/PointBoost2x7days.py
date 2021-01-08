import datetime

from mage.items.PointBoost import PointBoost


class PointBoost2x7days(PointBoost):
    name = "PointBoost(2x7days)"
    is_enabled = True
    price = 100
    BOOST_FACTOR = 2
    TIMEDELTA = datetime.timedelta(days=7)


    def __init__(self, *args, **kwargs):
        super(PointBoost, self).__init__(*args, **kwargs)
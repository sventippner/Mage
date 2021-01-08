import datetime

from mage.items.PointBoost import PointBoost


class PointBoost2x30days(PointBoost):
    name = "PointBoost(2x30days)"
    is_enabled = True
    price = 300
    BOOST_FACTOR = 2
    TIMEDELTA = datetime.timedelta(days=30)


    def __init__(self, *args, **kwargs):
        super(PointBoost, self).__init__(*args, **kwargs)
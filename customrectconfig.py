from PyQt4.QtGui import QPen
from PyQt4.Qt import Qt
from sloth.items import RectItem


class CustomRectItem(RectItem):
    # display values of x and y as text inside the rectangle
    defaultAutoTextKeys = ['x', 'y', 'width', 'height']

    def __init__(self, *args, **kwargs):
        RectItem.__init__(self, *args, **kwargs)

        # set drawing pen to red with width 2
        self.setPen(QPen(Qt.red, 2))

LABELS = (
    {
        'attributes': {
            'label': 'red_rect',
            'class': 'red_rect',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item': CustomRectItem,  # use custom rect item instead of sloth's standard item
        'text': 'RedLight',
    },
    {
        'attributes': {
            'label': 'orange_rect',
            'class': 'orange_rect',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item': CustomRectItem,  # use custom rect item instead of sloth's standard item
        'text': 'OrangeLight',
    },
    {
        'attributes': {
            'label': 'green_rect',
            'class': 'green_rect',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item': CustomRectItem,  # use custom rect item instead of sloth's standard item
        'text': 'GreenLight',
    },
)

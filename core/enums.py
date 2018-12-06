from enum import Enum

DIRECTION_X_CHOICES = (
    ('E', 'East'),
    ('W', 'West'),
)

DIRECTION_Y_CHOICES = (
    ('N', 'North'),
    ('S', 'South'),
)

POLYGON_CHOICES = (
    ('SQUARE', 'Square'),
    ('CIRCLE', 'Circle'),
    ('RECTAN', 'Rectangle'),
    ('COLOR', 'Color'),
)

COLOR_CHOICES = (
    ('100,150,0|140,255,255', 'BLUE'),
    ('0,0,0|180,255,30', 'BLACK'),
    ('0,0,200|180,255,255', 'WHITE'),
    ('170,50,50|180,255,255', 'RED'),
)
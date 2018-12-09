import threading
from unipath import Path
from datetime import datetime, date
from json import dumps
from math import sqrt

def check_diagonal_distance(dX, dY, radius):
	return sqrt(dX **2 + dY ** 2) <= float(radius)

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

'''

	def set_status(self, is_danger):
		self.is_danger = is_danger
		db = firebase.database()
		db.child('danger').set(is_danger)

	def set_passed_point(self, name):
		db = firebase.database()
		my_obj = {'name': name, 'date': dumps(datetime.now(), default=json_serial)}
		db.child('point').set(my_obj)
'''

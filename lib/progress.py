
progressDict = {'name': "unnamed", 'bi_bob': 0, 'bi_pickle': 0, 'bi_library': 1}


def set_progress(kind, status):
	global progressDict
	progressDict[kind] = status


def get_progress(kind):
	global progressDict
	return progressDict[kind]

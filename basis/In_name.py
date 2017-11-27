#存储多个姓名方便搜索
def store(data, *full_names):
	init(data)
	for full_name in full_names:
		names = full_name.split()
		if len(names) == 2: names.insert(1, '')
		labels = 'first', 'middle', 'last'
		for label, name in zip(labels, names):
			people = lookup(data, label, name)
			if people:
				people.append(full_name)
			else:
				data[label][name] = [full_name]

def init(data):
	data['first']  = {}
	data['middle'] = {}
	data['last']   = {}

def lookup(data, label, name):
	return data[label].get(name)

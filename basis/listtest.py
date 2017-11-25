#检查首字母是否匹配，需要检查每个可能的配对，效率不高
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold','bob']
print ([b+'+'+g for b in boys for g in girls if b[0] == g[0]])
#检查首字母是否匹配,不用尝试所有的组合
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold','bob']
lettergirls = {}
for girl in girls:
	lettergirls.setdefault(girl[0],[]).append(girl)
print ([b+'+'+g for b in boys for g in lettergirls[b[0]]])

def Num_list(In_list):
	dic_num = {}
	for num in In_list:
		number = In_list.count(num)  #对重复的元素进行计数
		dic_num[num] = number #以字典的形式进行存储
	return dic_num

from collections import Counter

def Num_list2(In_list):
	return Counter(In_list)

def dicTolist(dic_num): #将字典转化为列表
	list_num = [key for key in dic_num]
	return list_num

if __name__ == "__main__":
	In = ['a','a','b','c','c','b','d','b','c']
	D = Num_list(In)
	print (D)
	print(Num_list2(D))
	Out_list = dicTolist(D)
	print(Out_list)

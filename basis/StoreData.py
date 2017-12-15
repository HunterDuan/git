'''#一副扑克牌的输出
values = range(1,11) + 'Jack Queen King'.split()
suits = 'diamonds clubs hearts spades'.split()
deck = ['%s of %s'%(v, s) for v in values for s in suits]
'''
#数据库的应用实例
import shelve
def StorePerson(db):
	Pid = str(input('Enter unique ID number: '))
	Person = {}
	Person['name'] = input('Enter name: ') #需输入字符串
	Person['age'] = input('Enter age: ')
	Person['phone'] = input('Enter phone: ')
	db[Pid] = Person

def LookUp(db):
	Pid = str(input('Enter ID number: '))
	field = input('What whould you like to know ?(name, age, phone): ') #需输入字符串
	field = field.strip().lower()
	print('%s : %s'%(field.capitalize(), db[Pid][field]))

def PrintHelp():
	print('The available commands are: ') 
	print('store : Stores information about a person')
	print('lookup : Looks up a person from ID number')
	print('quit : Save changes and exit')
	print('? : Prints this message')

def EnterCommand():
	cmd = input('Enter command (? for help): ') #需输入字符串
	cmd = cmd.strip().lower()
	return cmd

def main():
	database = shelve.open('test.dat') #shelve.open()返回一个shelf对象，可当作普通的字典，但是键一定要作为字符串
	try:
		while True:
			cmd = EnterCommand()
			if cmd == 'store':
				StorePerson(database)
			elif cmd == 'lookup':
				LookUp(database)
			elif cmd == '?':
				PrintHelp()
			elif cmd == 'quit':
				return
	finally:
		database.close()

if __name__ == '__main__': main()



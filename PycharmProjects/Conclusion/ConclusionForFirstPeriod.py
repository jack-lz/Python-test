# Filename = ConclusionForFirstPeriod
# coding = utf-8


# Single line comments start with a hash
# 单行注释有一个#号开头

""" Multi-line strings can be written
	using three "'s, and are often used
	as comments
	三个双引号（或单引号）之间可以写多行字符串，
	通常用来写注释
"""

####################################################
## 1. Primitive Datatypes and Operators
## 1. 基本数据类型和操作符
####################################################

# You have numbers
# 数字就是数字
3 #=> 3

# Match is what you would expect
# 四则运算也是你所期望的那样
1 + 1 #=> 2
8 - 1 #=> 7
10 * 2 #=> 20
35 / 5 #=> 7

# Division is a bit tricky. It is integer division and floors the results
# automatically.
# 除法有一点棘手。
# 对于整体除法来说，计算结果会自动取整。
5 / 2 #=> 2

# To fix division we need to learn about floats.
# 为了修正除法的文体，我们需要先学习浮点数
2.0			# This is a float
11.0 / 4.0  #=> 2.5

# Enforce precedence with parentheses
# 使用小括号来强制计算的优先顺序
(1 + 3) * 2 #=> 8

# Boolean values are primitives
# 布尔值也是基础数据类型
True
False

# negate with not
# 使用 not 来取反
not True #=> True
not False #=> False

# Equality is ==
# 等式判断使用==
1 == 1 #=> True
2 == 1 #=> False

# Inequaality is !=
# 不等式判断是用 ！=
1 != 1 #=> False
2 != 1 #=> True

# More comparisons
# 还有更多的比较运算
1 < 10 #=> True
1 > 10 #=> False
2 <= 2 #=> True
2 >= 2 #=> True


# Comparisons can be chained
# 居然可以把比较运算符连起来使用
1 < 2 < 3 #=> True
2 < 3 < 2 #=> False

# Strings are created with " or '
# 使用 " 或是 ' 来创建字符串
"This is a string."
'This is a string.'

# Strings can be added too!
# 字符串也可以相加
"Hello" + "world!" #=> "Hello world!"

# A string can be treated like a list of characters
# 一个字符串可以视为一个字符的列表
"This is a string"[0]  #=> 'T'

# % can be used to format stings, like this
# % 可以被用来格式化字符串，就像这样
"%s can be %s" % ("string", "interpolated")

# A new way to format strings is the format method.
# This method is the preferred way
# 后来又有一种格式化字符串的新方法：format 方法。
# 我们推荐使用这种方法
"{0} can be {1}".format("string", "formatted")

# You can use keywords if you don't want to count
# 如果你不喜欢数数的话，可以使用关键词（变量）。
"{name} wants to eat {food}".format(name="Bob", food="lasagna")

# None is an object
# None 是一个对象
None #=> None

# Don't use the equality '==' symbol to compare objects to None
# Use 'is' instead
# 不要使用相等符号 '==' 来把对象和 None 进行比较，
# 要使用 'is'
"etc" is None #=>False
None is None  #=>True

# The 'is' operator tests for object identity.This isn't very useful
# when dealing with primitive values, but is very useful when dealing
# with objects.
# 'is' 操作符用于比较两个对象比较好用，基本数据类型就永不上了

# None, 0, and empty strings/lists all evaluate to False.
# All other values are True
# None , 0 以及空字符串和空列表都等于False。
# 除此之外的所有值都等于True
0 == False #=> True
"" == False #=> True




#############################################################
## 2. Variables and Collections
## 2. 变量和集合
#############################################################

# Printing is pretty easy
# 打印输出很简单
print("I'm Python. Nice to meet you !")

# No need to declare variables before assigning to them.
# 在赋值给变量之前不需要声明
some_var = 5	# Conventions is to use lower_case_with_underscores
				# 变量名的约定是使用下划线分隔的小写单词

# Accessing a previously unassigned variable is an exception.
# See Control Flow to learn more about exception handling.
# 访问一个未赋值的变量会产生一个异常
# 进一步了解异常处理机制，可以参见下节《控制流》。


# if can be used as an expression
# if 可以作为表达式来使用
"yahoo!" if 3 > 2 else 2 #=> "yahool"

# lists store sequences
# 列表用于存储序列
li = []

# You can start with a prefilled list
# 我们先尝试一个预先填充好的列表
other_li = [4, 5, 6]

# Add stuff to the end of a list with append
# 使用 append 方法把元素添加到列表的尾部
li.append(1)   # li is now [1]
li.append(2)   # li is now [1, 2]
li.append(3)   # li is now [1, 2, 3]


# Remove from the end with pop
# 使用 pop 来移除最后一个元素
li.pop()


# Access a list like you would any array
# 像访问其他语言的数组那样访问列表
li[0]  #=> 1
# Look at the last element
# 查询最后一个元素
li[-1] #=> 3


# You can look an ranges with slice syntax.
# (It's a closed/open range for you mathy types.)
# 你可以使用切片语法来查询列表的一个范围
# （这个范围相当于数学中的左闭右开区间,即不包含结尾。
# 其中第一个数表示开始位置，第二个表示结束位置，第三个表示间隔
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
li[1:6:2] #=> [2, 4]

# Remove arbitrary elements from a list with del
# 使用 del 来删除列表中的任意元素
del li[2]  # 删除序列为2的元素

# You can add lists
# 可以把列表相加
li + other_li


# Concatenate lists with extend
# 使用 extend 来合并列表
li.extend(other_li)

# Check for existence in a list with in
# 用 in 来检查是否存在于某个列表中
1 in li #=> 6

# Examine the length with len
# 用len 来检测列表的长度
len(li)


# Tuples are like lists but are immutable
# 元组很像列表，但它是”不可变“的
tup = (1, 2, 3)
tup + (4, 5, 6)
tup[1:6:2]
2 in tup #=> True

# You can unpack tuples (or lists) into variables
# 你可以把元组（或列表）中的元素解包赋值给多个变量
a, b, c = (1, 2, 3) #=> a is now 1, b is now 2, c is now 3

# Tuples are created by default if you leave out the parentheses
# 如果你省去了小括号，那么元组会自动被创建
d, e, f = 4, 5, 6

# Now look how easy it is to swap two values
# 再来看看交换两个值是多么简单
e, d = d, e    #=> d is now 5 and e is now 4


# Dictionaries store mappings
# 字典用于存储映射关系
empty_dict = {}
# Here is a prefilled dictionary
# 这是一个预先填充的字典
filled_dict = {"one": 1, "two": 2, "three": 3}

# Look up values with []
# 使用[]来查询键值
filled_dict["one"] #=> 1

# Get all keys as a list
# 将字典的所有键名获取为一个列表
filled_dict.keys() #=> ["three", "two", "one"]
# Note - Dictionary key ordering is not guaranteed
# Your results might not match this exactly.
# 请注意：无法保证字典键名的顺序如何排列。
# 你得到的结果可能跟上面的示例不一致

# Get all values as a list
# 将字典的所有键值获取未一个列表
filled_dict.values()
# Note - Some as above regarding key ordering,
# 请注意：顺序的问题和上面一样

# Check for existence of keys in a dictionary with in
# 使用 in 来检验一个字典是否包含某个键值
"one" in filled_dict   #=> True
1 in filled_dict      #=>False

# Looking up a non-existing key is a KeyError
# 查询一个不存在的键名灰产生一个键值名错误
filled_dict["four"] # KeyError

# Use get method to avoid the KeyError
# 所以要使 get 方法来避免键名错误
filled_dict.get("one") #=> 1
filled_dict.get("four") #=> None
# This get method supports a default argument when the value is missing
# get 方法支持传入一个默认值参数，将在娶不到值时返回
filled_dict.get("one", 4) #=> 1
filled_dict.get("four", 4) #=> 4

# Setdefault method is a safe way to add new key-value pair into dictionary
# Setdefault 方法可以安全的把新的名值对添加到字典里,只能用来设置默认值
filled_dict.setdefault("five", 5) #filled_dict["five"] = 5
filled_dict.setdefault("five", 6) #filled_dict["five"] = 5 不会改变


# Set store ... well sets
# set 用于保存集合
empty_set = set()
# Initialize a set  with a bunch of values
# 使用一堆值来初始化一个集合
some_set = set([1,2,2,3,4]) #=> some_set is now set({1,2,3,4})
# 集合是种无序不重复的元素集，因此重复的2被过滤了

# Since Python 2.7, {} can be used to declare a set
filled_set = {1, 2, 2, 3, 4} # => {1, 2, 3, 4}

# add more items to a set
filled_set.add(5)  # filled_set is now {1, 2, 3, 4, 5}

# Do set intersection with &
other_set = {3, 4, 5, 6}
filled_set & other_set #=> {1, 2, 3, 4, 5, 6}

# Do set union with |
filled_set | other_set #=> {1, 2, 3, 4, 5, 6}

# Do set difference with -
{1,2,3,4} - {2,3,5} #=> {1, 4}

# Check for existence in a set with in
2 in filled_set #=> True
10 in filled_set #=> False


######################################################################
## 3. Control Flow
## 3. 控制流
######################################################################

# Let‘s just make a varible
some_var = 5

# Here is an if statement
if some_var > 10:
	print "some_var is totally bigger than 10."
elif some_var < 10:
	print "some_var is smaller than 10."
else:
	print "some_var is indeed 10."


"""
For loops iterate over lists
for 循环可以遍历列表
prints：
如果要打印出：
	dog is a mammal
	cat is a mammal
	mouse is a mammal
"""

for animal in ["dog", "cat", "mouse"]:
	print "%s is a mammal" % animal



"""'range(number)' returns a list of numbers
from zero to the given number
'range(number)' 会返回一个数字列表，
这个列表将包含从零到给定的数字。
prints:
如果需要打印出：
	0
	1
	2
	3
"""

for i in range(4):
	print i

"""
While loops go until a condition is no longer met.
while 循环灰一直继续，直到条件不再满足。
prints：
如果需要打印出：
	0
	1
	2
	3
"""

x = 0
while x < 4:
	print x
	x += 1  #=> x = x + 1

# Hanle exceptions with a try/except block
# 使用try/except 模块来处理异常

# Works on Python 2.6 and up
# 试用于 Python 2.6 及以上版本
try：
	# Use raise to raise an error
	# 使用raise来抛出一个错误
	raise IndexError("This is an index error")

except IndexError as e:
	pass



####################################################################
## 4. Functions
## 4. 函数
####################################################################

# Use def to create new functions
# 使用 def 来创建新函数
def add(x, y):
	print("x is %s and y is %s", x, y)
	return x+y


# Calling functions with parameters
# 调用函数并传入参数
add(5, 6)

# Another way to call functions is with keyword arguments
# 调用函数的另一个方法是传入关键字参数
add(y=5, x=6)


# You can define functions that take a variable number of
# possitional arguments
# 你可以定义一个函数，并让它接受可变书来的定位参数
def varargs(*args)
	return  args

varargs(1, 2, 3) #=> (1, 2, 3)


# You can define functions that take a variable number of
# keyword arguments, as well
# 你也可以定义一个函数，并让它接受可变数量的关键字参数
def keyword_args(**kwargs):
	return kwargs

# Let's call it to see what happens
# 我们试试调用它，看看会发生些什么
keyword_args(big="foot", loch = "ness") #=> {"big":"foot", "loch":"ness"}



# You can do both at once, if you like
# 你还可以同时使用这两类参数，只要你愿意
def all_the_args(*args, **kwargs):
	print args
	print kwargs

"""
all_the_args(1, 2, a=3, b=4) prints:
	(1, 2)
	{"a":3, "b":4}
"""


# When calling functions， you can do the opposite of varargs/kwargs！
# Use × to expand tuples and use ** to expand kwargs.
# 在调用函数时，定位参数和关键字参数还可以反过来用
# 使用× 来展开元祖，使用×× 来站来关键字参数
args = (1,2,3,4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args)            #=> 相当于 all_the_args（1,2,3,4）
all_the_args(**kwargs)         #=> 相当于 all_the_args（a=3,b=4）
all_the_args(*args, **kwargs)  #=> 相当于 all_the_args（1,2,3,4,a=3,b=4）


# Python has first class functions
# 函数在Python 中是一等公民
def create_adder(x):
	def adder(y):
		return x+y
	return adder
add_10 = create_adder(10)
add_10(3) #=>13


# There are also anonymous functions
# 还有匿名函数
(lambda x: x > 2)(3) #=> True

# There are built-in higher order functions
# 还有一些内建的高阶函数
map(add_10,[1,2,3]) #=> [11,12,13]
filter(lambda x: x > 5, [3,4,5,6,7]) #=> [6,7]

# We can use list comprehensions for nice maps and filters
# 我们可以使用列表推导式来模拟 map 和 filter
[add_10(i) for i in [1,2,3]] #=> [11,12,13]
[x for x in [3,4,5,6,7] if x > 5]  #=> [6,7]


###################################################################################
## 5. Classes
## 5. 类
###################################################################################

# We subclass from object to get a class.
# 我们可以从对象中继承，来得到一个类

class Human(object):

	# A class attribute. It is shared by all instances of this class
    # 下面是一个类属性，它将被这个类的所有实例共享
	species = "H. sapiens"

	# Bassic initializer
    # 基本的初始化函数
	def __init__(self, name):
		self.name = name

	def say(self, msg):
		return "%s: %s" % (self.name, msg)

	# A class method is shared among all instances
	# They are called with the calling class as the first  argument
	# 类方法灰被所有实例共享
	# 类方法在调用时，会将类本身作为第一个函数传入
	@classmethod
	def get_species(cls):
		return cls.species

	# A static method is called without a class or instance reference
	# 静态方法在调用时，不会传入类或实例的引用。
	@staticmethod
	def grunt():
		return "*grunt"


# Instantiate a class
# 实例化一个类
i = Human(name="Ian")
print(i.say("hi"))

j = Human("Joel")
print(j.say("hello"))


# Call our class method
# 调用我们的类方法
i.get_species()  #=> "H. sapiens"

# Change the shared attribute
# 修改共享属性
Human.species = "H. neanderthalensis"
i.get_species() #=> "H. neanderthalensis"
j.get_species() #=> "H. neanderthalensis"

# Call the static method
# 调用静态方法
Human.grunt() #=> "*grunt"


#############################################################################
## 6. Modules
## 6. 模块
#############################################################################

# You can import modules
# 你可以导入模块
import math
print(math.sqrt(16)) #=>4


# You can get specific functions from a module
# 也可以从一个模块中获取指定的函数
from math import ceil, floor
print(ceil(3.7)) #=> 4.0
print(floor(3.7)) #=> 3.0

# You can import all functions from a module.
# Warning: this is not recommended
# 你可以从一个模块中导入所有函数
# 警告：不建议使用这种方式
from math import *

# You can shorten module names
# 你可以缩短模块的名称
import math as m
math.sqrt(16) == m.sqrt(16) #=> Ture

# Python modules are just ordinary python files. You
# can write your own, and import them. The name of the
# module is the same as the name of the file.
# Python 模块就是普通的Python 文件
# 你可以编写你自己的模块，然后导入它们
# 模块的名称和文件名相同


# You can find out which functions and attributes
# defines a module.
# 你可以查出一个模块里有哪些函数和属性
import math
dir(math)























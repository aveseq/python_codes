Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x1=set('1234')
>>> x1
{'3', '1', '2', '4'}
>>> x1.add('alot')
>>> x1
{'1', 'alot', '4', '3', '2'}
>>> s1={1,2,3,4}
>>> s2={1,5,3,6}
>>> s3=s1|s2
>>> s3
{1, 2, 3, 4, 5, 6}
>>> clrsr
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    clrsr
NameError: name 'clrsr' is not defined
>>> clrscr
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    clrscr
NameError: name 'clrscr' is not defined
>>> s1={'apple','ball','car'}
>>> s1
{'ball', 'apple', 'car'}
>>> s2={'two','ball','toy'}
>>> s3=s1&s2
>>> s3
{'ball'}
>>> s4=s1|s2
>>> s4
{'ball', 'car', 'apple', 'toy', 'two'}
>>> s5=s1-s2
>>> s5
{'car', 'apple'}
>>> x1={1,2,3,4}
>>> x1={1,2,3,4,5}
>>> x2={1,3,4}
>>> x1-x2
{2, 5}
>>> x2-x1
set()
>>> x3=x1>{1,3}
>>> x3
True
>>> x3=x1>x2
>>> x3
True
>>> x3=x1>{1,2,3,4,5,6}
>>> x3
False
>>> x2=x1-{1,2,3,4}
>>> x2
{5}
>>> {1,2,3,4}-{1,2,4}
{3}
>>> {1,2,3}|[4,5]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    {1,2,3}|[4,5]
TypeError: unsupported operand type(s) for |: 'set' and 'list'
>>> {1,2,3,4,5}&{1,2,3,8}
{1, 2, 3}
>>> s1=set([3,4,5])
>>> s1
{3, 4, 5}
>>> {1,2,3}.union({3,4})
{1, 2, 3, 4}
>>> {1,2,3}.union([5,4])
{1, 2, 3, 4, 5}
>>> s={1.23}
>>> s
{1.23}
>>> s.add({'a':1})
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    s.add({'a':1})
TypeError: unhashable type: 'dict'
>>> s.add((1,2,3))
>>> a
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> s
{1.23, (1, 2, 3)}
>>> s.add((4,5,6,5))
>>> s
{1.23, (1, 2, 3), (4, 5, 6, 5)}
>>> s|{(4,5,6),(7,8,9)}
{1.23, (4, 5, 6), (7, 8, 9), (1, 2, 3), (4, 5, 6, 5)}
>>> (4,5,6) in s
False
>>> (1,2,3) in s
True
>>> cities={"chennai","delhi","mumbai"}
>>> cities
{'delhi', 'chennai', 'mumbai'}
>>> cities.clear()
>>> cities
set()
>>> add_cities={'bangalore','kolkata'}
>>> add_cities
{'kolkata', 'bangalore'}
>>> b_cities=add_cities()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    b_cities=add_cities()
TypeError: 'set' object is not callable
>>> b_cities=add_cities.copy()
>>> b_cities
{'kolkata', 'bangalore'}
>>> cities=b_cities.coppy()
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    cities=b_cities.coppy()
AttributeError: 'set' object has no attribute 'coppy'
>>> b_cities.clear()
>>> b_cities
set()
>>> b_cities=add_cities
>>> b_cities
{'kolkata', 'bangalore'}
>>> add_cities=add_cities|{'vellore'}
>>> add_cities
{'kolkata', 'bangalore', 'vellore'}
>>> b_cities
{'kolkata', 'bangalore'}
>>> x={a,b,c,d,e}
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    x={a,b,c,d,e}
NameError: name 'a' is not defined
>>> x={'a','b','c','d','e'}
>>> x.discard('e')
>>> x
{'c', 'b', 'a', 'd'}
>>> x.remove('c')
>>> x
{'b', 'a', 'd'}
>>> x.append(c)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    x.append(c)
AttributeError: 'set' object has no attribute 'append'
>>> y={'e','f'}
>>> x.issubset(y)
False
>>> x>=y
False
>>> x<y
False
>>> x.ifsuperset(y)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    x.ifsuperset(y)
AttributeError: 'set' object has no attribute 'ifsuperset'
>>> x.issuperset(y)
False
>>> x1={1,2,3,4,5}
>>> x2={1,2,3}
>>> x1.issubset(x2)
False
>>> x2.issubset(x1)
True
>>> x1.issuperset(x2)
True
>>> x1.pop(5)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    x1.pop(5)
TypeError: pop() takes no arguments (1 given)
>>> x.pop(a)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    x.pop(a)
NameError: name 'a' is not defined
>>> x={"aveseq"}
>>> x
{'aveseq'}
>>> y=set(x)
>>> y
{'aveseq'}
>>> x=aveseq
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    x=aveseq
NameError: name 'aveseq' is not defined
>>> x=(aveeq)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    x=(aveeq)
NameError: name 'aveeq' is not defined
>>> cities
set()
>>> cities={'kolkata','bangalore','chennai'}
>>> cities.add("mumbai")
>>> cities
{'kolkata', 'bangalore', 'chennai', 'mumbai'}
>>> cities
{'kolkata', 'bangalore', 'chennai', 'mumbai'}
>>> cities=frozenset(["mandi","goa"])
>>> cities
frozenset({'mandi', 'goa'})
>>> cities.add('delhi')
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    cities.add('delhi')
AttributeError: 'frozenset' object has no attribute 'add'
>>> cities=cities|{'delhi}
	       
SyntaxError: EOL while scanning string literal
>>> cities = cities | {"delhi"}
>>> 
>>> cities
frozenset({'delhi', 'mandi', 'goa'})
>>> cities.pop()
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    cities.pop()
AttributeError: 'frozenset' object has no attribute 'pop'
>>> 
>>> {x for x in 'spam'}
{'m', 's', 'p', 'a'}
>>> x.pop(a)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    x.pop(a)
NameError: name 'a' is not defined
>>> s
{1.23, (1, 2, 3), (4, 5, 6, 5)}
>>> s1
{3, 4, 5}
>>> s={}
>>> s={c*4 for c in 'spam'}
>>> s
{'pppp', 'aaaa', 'mmmm', 'ssss'}
>>> s|{'mmm','xxx'}
{'ssss', 'xxx', 'mmm', 'pppp', 'aaaa', 'mmmm'}
>>> s & {'mmm','rrr'}
set()
>>> s
{'pppp', 'aaaa', 'mmmm', 'ssss'}
>>> s & {'ccc','iii'}
set()
>>> print(a)



                   

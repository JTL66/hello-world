Last login: Tue Sep  1 19:09:30 on ttys000
(base) JTdeMacBook-Pro:~ jtliu$ python
Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> ###Questions:
>>> #1.Which of the following variable assignments are valid?
>>> x = 6
>>> _x=10.5
>>> 20people=20
  File "<stdin>", line 1
    20people=20
      ^
SyntaxError: invalid syntax
>>> my_33cows=33
>>> big$exit=105
  File "<stdin>", line 1
    big$exit=105
       ^
SyntaxError: invalid syntax
>>> #2.Come up with 3 invalid variable names
>>> Var=8
>>> _myData=8
>>> _my20teams=8
>>> #3.What are the outputs of:
>>> #a.True and False or True
>>> a=True
>>> b=False
>>> a and b or a
True
>>> #b.True and False or not True
>>> a and b or not a 
False
>>> #c.True or False or not True
>>> a or b or not a 
True
>>> #4.What is the output of 
>>> bool("False")
True
>>> #4.What is the output of bool("False")
>>> bool("False")
True
>>> #5.Which of the following string declarations are valid?  ???string declarations are valid below???
>>> my_string="foo"
>>> my_string='bar'
>>> my_string='foo\tbar'
>>> my_string='''boo le an'''
>>> my_string
'boo le an'
>>> my_string="foo"
>>> my_string
'foo'
>>> my_string='bar'
>>> my_string
'bar'
>>> my_string='foo\tbar'
>>> my_string
'foo\tbar'
>>> #6.I'm trying to print"Hello World" on 2 lines, such that output looks like this:
>>> str="""
... Hello
... World"""
>>> print(str)

Hello
World
>>> #7.What is printed?
>>> str="hello"
>>> len(str)
5
>>> #5 is printed.
>>> #8.What is printed?
>>> str="Hello"
>>> str[-1]
'o'
>>> #"o"is printed.
>>> #9.What is printed?
>>> str="Hello"
>>> str[1]
'e'
>>> #“e" is printed.
>>> #10.I create digital arts.I want to make my art background using a very long string....
>>> str="Hello"
>>> str*320
'HelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHello'
>>> #11.What is the output?
>>> "Hello"+6
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> #12.Given 2 variable A and B
>>> #write conditionals that would:
>>> #a.evaluate to True if A is smaller than B
>>> #a.evaluate to True if A is equal to B         ??? How can 'A equal to B' be true at the same time???
>>> #c.evaluate to True if A is not equal to B
>>> A=20
>>> B=30
>>> A==B
False
>>> A!=B
True
>>> A<B
True
>>> A=30
>>> B=3
>>> B=30
>>> A==B
True
>>> #13.What is the output
>>> bool(5)
True
>>> #14.What is the output
>>> bool(0)
False
>>> #15.I have my oython script stored in a file named foo.py and I am in the terminal in the same directory the file is located in, how do I run the python script in the file?
>>> #(base) JTdeMacBook-Pro:~ jtliu$ python
>>> #(base) JTdeMacBook-Pro:~ jtliu$ pwd
>>> #(base) JTdeMacBook-Pro:~ jtliu$ cd Campus/python/lecture1/
>>> #(base) JTdeMacBook-Pro:~ jtliu$ ls
>>> #(base) JTdeMacBook-Pro:~ jtliu$ foo.py

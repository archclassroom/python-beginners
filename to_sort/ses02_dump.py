# coding: utf-8

get_ipython().run_line_magic('pinfo', 'str.format')
'{} {}'.format('one', 'two')
'{}||{}'.format('one', 'two')
'{{{}}}||{{}}'.format('one', 'two')
'{{{}}}||{{{}}}'.format('one', 'two')
'{{{1}}}||{{{0}}}'.format('one', 'two')
get_ipython().run_line_magic('pinfo', 'isinstance')
isinstance(5, int)
isinstance(5.1, int)
if 'value' is in {'key':'value'}
'value' is in {'key':'value'}
'value' in {'key':'value'}
'key' in {'key':'value'}
{'key':'value'}.values()
'value' in {'key':'value'}.values()
not False
verbose = False
if verbose:
    print('more info')
    
if not verbose:
    print('more info')
    
if not verbose:
    print('less info')
else:
    print('more info')
    
verbose = True
if not verbose:
    print('less info')
else:
    print('more info')
    
while True:
    print('verbose')
    
count = 100
while False:
    print(count)
    
count > 0
0 > 0
0 => 0
0 >= 0
while count > 0:
    #count = count - 1
    count -= 1
    print(count)
count = 100;while count > 0:
    #count = count - 1
    print(count)
    count -= 1

    
while count > 0:
    #count = count - 1
    print(count)
    count -= 1

    
count = 100
while count > 0:
    #count = count - 1
    print(count)
    count -= 1

    
while count > 0:
    #count = count - 1
    if count is 50:
        continue
    print(count)
    count -= 1

    
count = 100
while count > 0:
    #count = count - 1
    if count is 50:
        continue
    print(count)
    count -= 1

    
while count > 0:
    count = count - 1
    if count is 50:
        continue
    print(count)

    
    
count = 100
while count > 0:
    count = count - 1
    if count is 50:
        continue
    print(count)

    
    
while count > 0:
    count = count - 1
    if count is 50:
        break
    print(count)

    
    
    
count = 100
while count > 0:
    count = count - 1
    if count is 50:
        break
    print(count)

    
    
    
count = 100
while count > 0:
    count = count - 1
    if count is 50:
        break
    print(count)
else:
    print('finished')

    
    
    
    
while count > 0:
    count = count - 1
    if count is 50:
        continue
    
    print(count)
else:
    print('finished')

    
    
    
    
get_ipython().set_next_input("'albert'.replace");get_ipython().run_line_magic('pinfo', 'replace')
get_ipython().run_line_magic('pinfo', 'replace')
'albert'
a = 'albert'
get_ipython().run_line_magic('pinfo', 'a.replace')
import this
import datetime
get_ipython().run_line_magic('pinfo2', 'datetime.datetime')
get_ipython().run_line_magic('pinfo2', 'datetime')
datetime.__file__
datetime.__docs__
datetime.__doc__
datetime.__dict__
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cd', 'git/_personal/python-beginners/')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cat', 'new_file.txt')
get_ipython().run_line_magic('cat', 'new_file.txt')
get_ipython().run_line_magic('pinfo2', 'all')
get_ipython().run_line_magic('pinfo2', 'any')
target_file = input('Give a name of file:' )
target_file
target_file = input('Give a name of file:' )
target_file = input('Give a name of file: ')
target_file
with open(target_file) as iowrap:
    print(iowrap.readline())
    
try:
    with open(target_file) as iowrap:
        print(iowrap.readline())
except FileNotFoundError:
    print('{} is not found'.format(target_file))
    
    
target_file = input('Give a name of file:' )
try:
    with open(target_file) as iowrap:
        print(iowrap.readline())
except FileNotFoundError:
    print('{} is not found'.format(target_file))
    
    
target_file = input('Give a name of file:' )
try:
    with open(target_file) as iowrap:
        print(iowrap.readline())
except FileNotFoundError as error:
    print('{} is not found'.format(target_file))
    print(error)
    
    
    
dir(error)
try:
    with open(target_file) as iowrap:
        print(iowrap.readline())
except FileNotFoundError as error:
    print('{} is not found'.format(target_file))
    print(dir(error))
    
    
    
    
try:
    with open(target_file) as iowrap:
        print(iowrap.readline())
except FileNotFoundError as error:
    print('{} is not found'.format(target_file))
    print(error.filename)
    
    
    
    
try:
    with open(target_file) as iowrap:
        print(iowrap.readline())
except FileNotFoundError as error:
    print('{} is not found'.format(target_file))
    print(error.errno)
    
    
    
    
    
def open_and_readline():
    with open(target_file) as iowrap:
        print(iowrap.readline())
        
try:
    open_and_readline()
except FileNotFoundError as error:
    print('{} is not found'.format(target_file))
    print(error.errno)
    
    
    
    
    
target_file = 'README.md'
try:
    open_and_readline()
except FileNotFoundError as error:
    print('{} is not found'.format(target_file))
    print(error.errno)
    
    
    
    
    
def open_and_readline(target_file):
    with open(target_file) as iowrap:
        print(iowrap.readline())
        
        
try:
    open_and_readline()
except FileNotFoundError as error:
    print('{} is not found'.format(target_file))
    print(error.errno)
    
    
    
    
    
target_file
try:
    open_and_readline('whateverfile')
except FileNotFoundError as error:
    print('{} is not found'.format(target_file))
    print(error.errno)
    
    
    
    
    
try:
    open_and_readline('whateverfile')
except FileNotFoundError as error:
    print('{} is not found'.format(error.filename))
    
    
    
    
    
target_file
while count > 0:
    count = count - 1
    if count is 50:
        continue
    
    print(count)
else:
    print('finished')

    
    
    
    
count
def count_from_int_down():
    while count > 0:
        count = count - 1
        if count is 50:
            continue
    
        print(count)
    else:
        print('finished')

        
    
    
    
    
def count_from_int_down(count):
    while count > 0:
        count = count - 1
        if count is 50:
            continue
    
        print(count)
    else:
        print('finished')

        
    
    
    
    
get_ipython().run_line_magic('pinfo', 'count_from_int_down')
get_ipython().run_line_magic('pinfo2', 'count_from_int_down')
count_from_int_down(10)
count_from_int_down(500)
def count_from_int_down(count):
    """counts from count down one by one
    if count is exactly 50, return True
    otherwise return False
    """
    while count > 0:
        count = count - 1
        if count is 50:
            return True
        print(count)
    else:
        print('finished')
    return False
count_from_int_down(30)
count_from_int_down(50)
count_from_int_down(51)
count_from_int_down(100)
try:
    open_and_readline('whateverfile')
except FileNotFoundError as error:
    print('{} is not found'.format(target_file))
    print(error.errno)
    
    
    
    
    
try:
    open_and_readline('whateverfile')
except FileNotFoundError as error:
    print('{} is not found'.format(target_file))
    print(error.errno)
finally:
    print('I tried to open file', target_file)
    
    
    
    
    
    
try:
    open_and_readline('README.md')
except FileNotFoundError as error:
    print('{} is not found'.format(target_file))
    print(error.errno)
finally:
    print('I tried to open file', target_file)
    
    
    
    
    
    
'albert' + 'jofrey
'albert' + 'jofrey'
'albert' + ' jofrey'
aa = 'albert' + ' jofrey'
aa = '{} {}'.format('albert' + ' jofrey')
'{} {}'.format('albert' + ' jofrey')
aa = '{} {}'.format('albert', ' jofrey')
aa
'aa' + 5
fruits
fruits = 'melon, pear, apple'.split(',')
fruits
type(fruits)
id(fruits)
fruits.append('yum')
id(fruits)
fruits
copy_of_fruits = fruits[:]
id fruits
id(fruits)
id(copy_of_fruits)
fruits.append('yum')
fruits
copy_of_fruits
copy_of_fruits.remove('yum')
copy_of_fruits
link_of_fruits = fruits
link_of_fruits.pop('pear')
get_ipython().run_line_magic('pinfo', 'link_of_fruits.pop')
link_of_fruits.pop(2)
link_of_fruits
fruits
id(fruits)
id(link_of_fruits)
link_of_fruits is fruits
fruits is not copy_of_fruits
fruits is copy_of_fruits
fruits
copy_of_fruits
fruits.remove('yum')
fruits
fruits.remove('yum')
fruits.remove('yum')
fruits
copy_of_fruits.(' apple')
copy_of_fruits.append(' apple')
copy_of_fruits
fruits
fruits.append(' apple')
copy_of_fruits in ' apple'
' apple' in copy_of_fruits
while ' apple' in copy_of_fruits:
    copy_of_fruits.remove(' apple')
    
copy_of_fruits
fruits
copy_of_fruits.append(' apple')
copy_of_fruits == fruits
copy_of_fruits is fruits
get_ipython().run_line_magic('pwd', '')

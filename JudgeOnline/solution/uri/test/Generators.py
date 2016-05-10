'''
Created on May 5, 2016

@author: christoffer
'''

'''
https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
http://anandology.com/python-practice-book/iterators.html
https://wiki.python.org/moin/Generators
http://www.pydanny.com/python-yields-are-fun.html
'''


# exemplo citado pelo Vini
def buildSampleGenerator():
    _list = range(10)
    for i in _list:
        yield i*i

sampleGen = buildSampleGenerator()

'''
http://stackoverflow.com/questions/3023503/how-can-i-check-if-an-object-is-an-iterator-in-python
'''

def isIterator(it):
    if(
        hasattr(it, '__iter__') and
        hasattr(it, 'next') and
        callable(it.__iter__) and
        it.__iter__() is it
    ):
        return True
    else:
        return False

isIterator(sampleGen)


def isIterable(it):
    try:
        iter(it)
    except TypeError : return False
    return True


def iterate(it):
    if(isIterable(it)):
        for i in it:
            print(i)

#iterate(sampleGen)

#http://anandology.com/python-practice-book/iterators.html
def iteratorMap():
    for item in {"x": 1, "y": 2}:
        print(item)

iteratorMap()

if __name__ == '__main__':
    pass
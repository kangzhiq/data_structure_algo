# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 11:09:55 2019

@author: zhiqi
@ copyright reserved by Data structures and Algorithms in Python of Zongyan PEI
"""

'''
Define a linked list with class LNode which allows some basic operation
'''


def length(head):
    n = 0
    p = head
    while p is not None:
        n += 1
        p = p.next
    return n

'''
Define the structure of node
'''
class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_
        
'''
Construct a singly linked list based on LNode
'''
class LList:
    def __init__(self):
        self._head = None
        
    def is_empty(self):
        return self._head is None
    
    def prepend(self, elem):
        self._head = LNode(elem, self._head)
        
    def pop(self):
        if self._head is None:
            raise ValueError("Empty list")
        res = self._head.elem
        self._head = self._head.next
        return res
    
    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)
        
    def pop_last(self):
        if self._head is None:
            raise ValueError("Empty list")
        p = self._head
        if p.next is None:
            res = self._head.elem
            self._head = None
            return res
        while p.next.next is not None:
            p = p.next
        res = p.elem
        p.next = None
        return res
    
    def for_each(self, proc):
        p = self._head
        while p is not None:
            p.elem = proc(p.elem)
            p = p.next
    
    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(',', end='')
            p = p.next
        print('')
    
    # Generator
    def elements(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next
    
l = LList()
for i in range(10):
    l.prepend(i)
l.printall()
l.for_each(lambda a: a+1)
for i in l.elements():
    print(i)
    
    
'''
Adding a reference to the rear node in the singular linked list
'''    
class LList1(LList):
    def __init__(self):
        LList.__init__(self)
        self._rear = None
        
    '''
    It is important to stay consistent in dealing the sample event/fonctionality
    in the same class.
    '''
    def prepend(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)
    
    '''
    This is the main improvement compared with LList 
    '''
    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next
    
    def pop_last(self):
        if self._head is None:
            raise ValueError("Empty list")
        p = self._head
        if p.next is None:
            res = p.elem
            self._head = None
            return res
        while p.next.next is not None:
            p = p.next
        res = p.next.elem
        p.next = None
        return res
        
    
l1 = LList1()
l1.prepend(99)
l1.printall()
for i in range(1, 10):
    l1.append(i)
l1.printall()


'''
Circular linked lists
Unlike singular linked list, this structure allows the apend/pop(n) to be O(1)
'''
class LCList:
    def __init__(self):
        self._rear = None
        
    def is_empty(self):
        return self._rear is None
    
    def prepend(self, elem):
        p = LNode(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p
    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next
        
    def pop(self):
        if self._rear is None:
            raise ValueError("Empty list")
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem

    def printall(self):
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p = p.next

l = LCList()
for i in range(10):
    l.prepend(i)
l.printall()


'''
Reverse the linked list
'''
class RevLList(LList):
    def __init__(self):
        super(RevLList, self).__init__()
    
    def rev(self):
        p = None
        while self._head is not None:
            q = self._head
            self._head = q.next
            q.next = p
            p = q
        self._head = p
        
rev = RevLList()
for i in range(1, 10):
    rev.append(i)  
rev.printall()
rev.rev()
rev.printall()


'''
Sorting a list
'''
def list_sort(lst):
    for i in range(1, len(lst)):
        x = lst[i]
        j = i
        while j > 0 and lst[j-1] > x:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = x
    return lst
        
         
a = [1, 4, 9, 0, 2, 3]
list_sort(a)

'''
Sorting a linked list by moving all elements after x  
'''
class SortLList1(LList):
    def sort1(self):
        if self._head is None:
            return
        crt = self._head.next
        while crt is not None:
            x = crt.elem
            p = self._head
            while p is not crt and p.elem <= x:
                p = p.next
            while p is not crt:
                y = p.elem
                p.elem = x
                x = y
                p = p.next
            crt.elem = x
            crt = crt.next

a = [1, 4, 9, 0, 2, 3]
sl = SortLList1()
for i in a:
    sl.append(i)
sl.printall()
sl.sort1()
sl.printall()
            
'''
Sorting a linked list by changing the links
'''
class SortLList2(LList):
    def sort2(self):
        p = self._head
        if p is None or p.next is None：:
            return
        
        rem = p.next
        p.next = None
        while rem is not None:
            p = self._head
            q = None
            while p is not None and p.elem <= rem.elem:
                q = p
                p = p.next
            if q is None:
                self._head = rem
            else:
                q.next = rem
            q = rem
            rem = rem.next
            q.next = p
            
        
# -*- coding: utf-8 -*-

from linkedlist import LinkedList

myList = LinkedList()
# print(myList.getLast()) ==> gives assert error

myList.insertFirst(2)
print(myList.getFirst().val)
# ==> 2

print(myList.getSize())
# ==> 1

myList.insertFirst(1)
print(myList.getFirst().val)
# ==> 1

print(myList.getSize())
# ==> 2

myList.insertLast(3)
print(myList.getLast().val)
# ==> 3

myList.removeFirst()
print(myList.getFirst().val)
# ==> 2

myList.removeLast()
print(myList.getLast().val)
# ==> 2

print(myList.getSize())
# ==> 1

myList.clear()
print(myList.getSize())
# ==> 0

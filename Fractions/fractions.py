# -*- coding: utf-8 -*-


class Fraction:
    # constructor defines the way in which data objects are created
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    # override shallow equality
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    # override str method
    def __str__(self):
        return str(self.num) + " / " + str(self.den)

    # override add method
    def __add__(self, other):
        newnum = (self.num) * other.den + (other.num) * self.den
        newden = self.den * other.den
        common = self.gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    def __sub__(self, other):
        newnum = self.num*other.den - other.num*self.den
        newden = self.den * other.den
        common = self.gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        common = self.gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        common = self.gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    def gcd(self, m, n):
        while m % n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm % oldn
        return n

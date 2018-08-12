# -*- coding: utf-8 -*-

import random

class Codec:

    def __init__(self):
        self.baseurl = "http://tinyurl.com/"
        self.short2long = {}
        self.long2short = {"":""}
        self.chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"

    def encode(self, longUrl):
        if longUrl in self.long2short:
            return self.baseurl + self.long2short[longUrl]
        else:
            encoding = ""
            for i in range(6):
                encoding += random.choice(self.chars)
            if encoding in self.short2long:
                self.encode(longUrl)
            self.long2short[longUrl] = encoding
            self.short2long[encoding] = longUrl
            shorturl = self.baseurl + encoding
            return shorturl

    def decode(self, shortUrl):
        return self.short2long[shortUrl[-6:]]

codec = Codec()
print(codec.encode("http://facebook.com"))
print(codec.decode(codec.encode("http://facebook.com")))
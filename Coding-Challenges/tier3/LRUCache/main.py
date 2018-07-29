from LRUCache import LRUCache

capacity = 10
obj = LRUCache(capacity)

key, value = 0, 1
obj.put(key, value)
userid = obj.get(key)

key, value = "user_name", "n-kimberly"
obj.put(key, value)
username = obj.get(key)

print("Kimberly's user id is %s \nHer username is %s," % (userid, username))

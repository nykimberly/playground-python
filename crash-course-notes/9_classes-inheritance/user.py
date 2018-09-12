#!/home/nykimberly/anaconda3/bin/python3

class User():
    """Represent a user on a forum"""
    user_count = 0 

    def __init__(self, name, pw):
        """Initialize user with name and unencrypted password"""
        self.name = name
        self.pw = pw
        User.user_count += 1
        print("Welcome,", self.name.title())

    def read_post(self, post_id):
        """Fetch post of post_id for user to read"""
        print("Reading post, id=%d" % post_id)

    def create_post(self, content):
        """Create post for user"""
        print("Creating post")

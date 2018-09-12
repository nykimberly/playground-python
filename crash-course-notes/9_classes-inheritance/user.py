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


class Admin(User):
    """Represent an admin on a forum"""

    def __init__(self, name, pw, engineer_pw):
        super().__init__(name, pw)
        self.engineer_pw = engineer_pw
        print("There are %d users as of today." % User.user_count)

    def delete_post(self, post_id):
        """Deletes post of post_id"""
        print("Deleting post, id=%d" % post_id)

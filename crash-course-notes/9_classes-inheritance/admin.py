#!/home/nykimberly/anaconda3/bin/python3
from user import User

class Admin(User):
    """Represent an admin on a forum"""

    def __init__(self, name, pw, engineer_pw):
        super().__init__(name, pw)
        self.engineer_pw = engineer_pw
        print("There are %d users as of today." % User.user_count)

    def delete_post(self, post_id):
        """Deletes post of post_id"""
        print("Deleting post, id=%d" % post_id)

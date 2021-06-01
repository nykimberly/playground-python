from django.db import models

class Topic(models.Model):
    """Topic that user follows"""
    # Define some attributes
    # CharField good for small amount of text
    text = models.CharField(max_length=200)
    # auto_now_add=True automatically sets this to current datetime of init
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return string representation of the model"""
        return self.text

class Entry(models.Model):
    """Something specific learned about a topic"""
    # pulls from Topic model and if Topic model is deleted, so is this entry
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # holds extra info about model
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model"""
        return self.text[:50] + "..."

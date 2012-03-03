from django.db import models


class Zombie(models.Model):
	name = models.CharField(max_length=20)
	cementery = models.CharField(max_length=40)


class Tweet(models.Model):
	status = models.CharField(max_length=140)
	zombie = models.ForeignKey('Zombie', related_name='tweettime')
	created_at = models.DateTimeField(auto_now_add=True)
	

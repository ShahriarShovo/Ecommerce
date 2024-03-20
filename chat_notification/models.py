from django.db import models

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

# Create your models here.
# 1. 👇 Add the following line
class Notification(models.Model):
    
	message = models.TextField(blank=True, null=True)
    
	created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True )
    
	class Meta:
		ordering = ['-created_at']
	
	def __str__(self) -> str:
		return self.message


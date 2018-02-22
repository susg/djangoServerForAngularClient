from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True)
	location = models.CharField(max_length=30, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	# social = JSONField(blank=True, null=True)
	fcm_token = models.TextField(max_length=32, blank=True)
	avatar = models.ImageField(upload_to='static/uploads/avatar/', null=True, blank=True)
	contact_no = models.CharField(max_length=10, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

class Page(models.Model):
	user = 	models.ForeignKey(Profile, on_delete=models.CASCADE)
	title = models.TextField(max_length=500, blank=True)
	publish_date = models.DateField()

class Post(models.Model):
	page = models.ForeignKey(Page, on_delete=models.CASCADE)
	title = models.TextField(max_length=500, blank=True)
	content = models.TextField(max_length=5000, blank=True)
	publish_date = models.DateField() 	
from django.db import models
from django.contrib.auth.models import User

# Models for profiles

# class Profile(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	bio = models.TextField(max_length=500, blank=True)
# 	pic = models.ImageField(upload_to='uploads/')

# 	@receiver(post_save, sender=User)
# 	def create_user_profile(sender, instance, created, **kwargs):
# 	    if created:
# 	        Profile.objects.create(user=instance)

# 	@receiver(post_save, sender=User)
# 	def save_user_profile(sender, instance, **kwargs):
# 	    instance.profile.save()
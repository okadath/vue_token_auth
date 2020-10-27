from django.db import models  
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	# country = CountryField(blank=True, null=True)
	# state = models.CharField(max_length=149, blank=True, null=True)
	# es necesario permitir este campo como nulo o la señal impide crear usuarios sin perfil
	# local_site = models.ForeignKey(LocalSite, related_name='Speaker_session', on_delete=models.CASCADE, null=True)
	# picture = models.FileField(upload_to='pics/', blank=True, null=True)
	picture = models.FileField(upload_to='pics/', blank=True, null=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	description = models.TextField(blank=True, null=True)
	# banner_1 = models.FileField(upload_to='banners/', blank=True, null=True, default="banners/default.jpeg")
	# preferred_language = models.ForeignKey(Language, on_delete=models.CASCADE, default=2)
	# lang=models.ForeignKey(Language, related_name='Language',on_delete=models.CASCADE)
	# country=models.ForeignKey(Country, related_name='Country',on_delete=models.CASCADE)
	# code = models.CharField(max_length=40, blank=True, null=True)
	# code=models.ForeignKey(Code, related_name='Code_account',on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return self.user.username
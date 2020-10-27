from django.apps import AppConfig


class UserAccountConfig(AppConfig):
    name = 'user_account'
    def ready(self):
		# señal para la creacion del profile automaticamente  al crear un usuario 
    	import user_account.signals

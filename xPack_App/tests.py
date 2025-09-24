from django.test import TestCase
# Create your tests here.
from django.conf import settings
from django.test import TestCase

class SettingsTests(TestCase):
	def test_required_apps_installed(self):
		required_apps = [
			'django.contrib.admin',
			'django.contrib.auth',
			'django.contrib.contenttypes',
			'django.contrib.sessions',
			'django.contrib.messages',
			'django.contrib.staticfiles',
			'xPack_App',
			'xPack_Registrar',
		]
		for app in required_apps:
			self.assertIn(app, settings.INSTALLED_APPS)


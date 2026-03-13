import os
from pathlib import Path

from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-default-key')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', '*']
INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'courses',
	'home',
	]
MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'whitenoise.middleware.WhiteNoiseMiddleware',  # Place right below SecurityMiddleware
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	]
ROOT_URLCONF = 'MikroLearning.urls'
TEMPLATES = [
	{
		'BACKEND':  'django.template.backends.django.DjangoTemplates',
		'DIRS':     [BASE_DIR / 'templates'],
		'APP_DIRS': True,
		'OPTIONS':  {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				'MikroLearning.context_processors.popular_courses',  # Add this
				],
			},
		},
	]
WSGI_APPLICATION = 'MikroLearning.wsgi.application'
DATABASES = {
	'default': {
		'ENGINE':   'django.db.backends.mysql',
		'NAME':     os.environ.get('DB_NAME', 'mikrolearning'),
		'USER':     os.environ.get('DB_USER', 'mikrolearning'),
		'PASSWORD': os.environ.get('DB_PASS', 'RealLongPassword#1010'),
		'HOST':     os.environ.get('DB_HOST', 'db'),
		'PORT':     '3306',
		},
	}
AUTH_PASSWORD_VALIDATORS = [
	{ 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator' },
	{ 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator' },
	{ 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator' },
	{ 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator' },
	]
LANGUAGE_CODE = 'en-us'  # Engleza
TIME_ZONE = 'Europe/Bucharest'
USE_I18N = True
USE_TZ = True
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
# AUTH
LOGIN_REDIRECT_URL = 'course_list'
LOGOUT_REDIRECT_URL = 'course_list'
LOGOUT_REDIRECT_URL = 'login'
# EMAIL (course requirement)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import os
from pathlib import Path
import environ # 1. استيراد environ

# ----------------- BASE SETUP -----------------

env = environ.Env(DEBUG=(bool, False))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Read .env file (يجب أن يحتوي على DATABASE_URL)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# ----------------- SECURITY & CORE -----------------

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')


# ----------------- APPLICATIONS -----------------
# **NOTE: هذه التطبيقات الافتراضية يجب أن تكون موجودة لحل جميع أخطاء Admin E4xx.**
INSTALLED_APPS = [
    # 1. تطبيقات Django الافتراضية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 2. تطبيقات الطرف الثالث
    'rest_framework',
    'corsheaders',
    'drf_yasg',
    
    # 3. تطبيقات المشروع
    'listings.apps.ListingsConfig',
    # ...
]


# ----------------- MIDDLEWARE -----------------
# FIXES: admin.E408, E409, E410
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    
    # Required for Admin/Auth/Sessions
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    
    # Other middleware
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]


# ----------------- TEMPLATES -----------------
# FIXES: admin.E403
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ----------------- DATABASE -----------------
# يسحب إعدادات MySQL من ملف .env
DATABASES = {
    'default': env.db()
}


# ----------------- OTHER SETTINGS -----------------

# CORS settings
CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS', default=[])
CORS_ALLOW_ALL_ORIGINS = DEBUG


# REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
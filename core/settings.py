from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-o8pu8ce*@sl0v665&en%#5qc%zho2#&6zm61m)9sk2b&s66+uy"

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "storages",  # django-storages
    "authentication",
    "storage",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "solid",
        "USER": "admin",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": 5432,
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [
    BASE_DIR / "locale",
]

AUTH_USER_MODEL = "authentication.User"

STATIC_URL = "/static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = None

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

AWS_ACCESS_KEY_ID = "admin"
AWS_SECRET_ACCESS_KEY = "password"
AWS_STORAGE_BUCKET_NAME = "solid"
AWS_S3_ENDPOINT_URL = "http://localhost:9000"
AWS_S3_REGION_NAME = "us-east-1"
AWS_S3_SIGNATURE_VERSION = "s3v4"
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERIFY = False
AWS_S3_ADDRESSING_STYLE = "path"

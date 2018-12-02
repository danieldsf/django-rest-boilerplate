from decouple import Csv, config

SECRET_KEY = config('SECRET_KEY', default='Th1515Uns3cur3', cast=str)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=Csv())

CORS_ORIGIN_ALLOW_ALL = config('CORS_ORIGIN', default=True, cast=bool)

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
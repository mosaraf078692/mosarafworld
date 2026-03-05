Nginx handle the static file before the request ever reaches Django. If you use Nginx, you don't strictly need WhiteNoise, but some developers keep it as a "backup" (a "belt and suspenders" approach).

let's set up WhiteNoise. It only takes 3 lines of code.

1. pip install whitenoise
2. Add 'whitenoise.middleware.WhiteNoiseMiddleware', to your MIDDLEWARE in settings.py.
3. Run python manage.py collectstatic.








EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = '<your smtp host>'
EMAIL_PORT = 587
EMAIL_HOST_USER = '<your email user>'
EMAIL_HOST_PASSWORD = '<your email password>'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'noreply@yourrestaurant.com'
RESTAURANT_ADMIN_EMAIL = 'admin@yourrestaurant.com'
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': {
        'rest_framework.authentication.SessionAuthentication',  # OAuth,JWT
        # 'rest_framework.authentication.BasicAuthentication',
    },
    'DEFAULT_PERMISSION_CLASSES': {
        'rest_framework.permissions.IsAuthenticated',
    },
}

import config.api_keys as keys

def authenticate_user(api_key):
    return api_key in keys.user_api_keys

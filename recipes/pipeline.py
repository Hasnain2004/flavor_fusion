from social_core.pipeline.partial import partial

def set_user_role(backend, user, response, *args, **kwargs):
    """
    Set default 'user' role for social auth users.
    This function is meant to be used in SOCIAL_AUTH_PIPELINE.
    """
    # Only set role if it's a new user or role is not already set
    if user and (kwargs.get('is_new', False) or not user.role):
        user.role = 'user'
        user.save()
    return {'user': user} 

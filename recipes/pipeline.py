from social_core.pipeline.partial import partial

def set_user_role(backend, user, response, *args, **kwargs):

    if user and (kwargs.get('is_new', False) or not user.role):
        user.role = 'user'
        user.save()
    return {'user': user} 

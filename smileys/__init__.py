VERSION = (0, 1, 0, 'rc2')

def version():
    return '%s.%s.%s-%s' % VERSION

def get_version():
    return 'django-smileys %s' % version()

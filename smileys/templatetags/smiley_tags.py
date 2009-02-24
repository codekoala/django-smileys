from django import template
from smileys.models import Smiley
import re

register = template.Library()

def gen_smileys(value, type):
    """
    Replaces all occurrences of the active smiley patterns in `value` with a
    tag that points to the image associated with the respective pattern.

    Hoorah!
    """

    for smiley in Smiley.objects.filter(is_active=True):
        # come up with the <img> tag
        if type == 'html':
            img = '<img class="smiley" src="%s" alt="%s" height="%i" width="%i" />' % (smiley.image.url, smiley.description, smiley.image.height, smiley.image.width)
        elif type == 'textile':
            img = '!%s!' % smiley.image.url

        if smiley.is_regex:
            # regex patterns allow you to use the same Smiley for multiple
            # ways to type a smiley
            value = re.sub(smiley.pattern, img, value)
        else:
            # this is the stupid (strict) way
            value = value.replace(smiley.pattern, img)

    return value

# register the filters
register.filter('smileys', lambda v: gen_smileys(v, 'html'))
register.filter('textile_smileys', lambda v: gen_smileys(v, 'textile'))

from django import template
from smileys.models import Smiley
import re

register = template.Library()

def smileys(value):
    """
    Replaces all occurrences of the active smiley patterns in `value` with a
    tag that points to the image associated with the respective pattern.

    Hoorah!
    """

    for smiley in Smiley.objects.filter(is_active=True):
        # come up with the <img> tag
        img = '<img clas="smiley" src="%s" alt="%s" height="%i" width="%i" />' % (smiley.image.url, smiley.description, smiley.image.height, smiley.image.width)

        if smiley.is_regex:
            # regex patterns allow you to use the same Smiley for multiple
            # ways to type a smiley
            value = re.sub(smiley.pattern, img, value)
        else:
            # this is the stupid (strict) way
            value = value.replace(smiley.pattern, img)

    return value

register.filter(smileys)
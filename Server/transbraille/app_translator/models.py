from django.db import models

BRAILLE_TEXT_TYPE = [
    ('letter', 'Letter'),
    ('number', 'Number'),
    ('word', 'Word')
]

class BrailleText(models.Model):
    text = models.CharField(max_length=100)
    braille = models.CharField(max_length=50)
    text_type = models.CharField(max_length=50, choices=BRAILLE_TEXT_TYPE)
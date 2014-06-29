from django.db import models

class Story(models.Model):
    name = models.CharField(max_length=100)
    plus = models.IntegerField()
    minus = models.IntegerField()

    def __unicode__(self):
        return self.name

class Line(models.Model):
    story = models.ForeignKey(Story)
    line_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    index = models.IntegerField()
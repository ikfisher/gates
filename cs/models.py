from django.db import models

class author(models.Model):
    name = models.CharField(max_length=64)
    country = models.CharField(max_length=32)
  
    def __unicode__(self):
	return self.name

class paper(models.Model):
    title = models.CharField(max_length=128)
    authors= models.ManyToManyField(author)
    topic=models.CharField(max_length=128, default='')

    def __unicode__(self):
	return self.title

class remark(models.Model):
    message=models.CharField(max_length=128, default='')
    who = models.ForeignKey(author, null=True)
    source = models.ForeignKey(paper, null=True)

    def __unicode__(message):
   	return self.message


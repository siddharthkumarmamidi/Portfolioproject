from django.db import models
#create a blog model
#create a title
#publication_date
#body or summary
#image

class Blog(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pretty_pub_date(self):
        return self.pub_date.strftime('%b %e %Y')
# Create your models here.

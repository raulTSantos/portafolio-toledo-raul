from django.db import models
from django.utils import timezone

# Create your models here.

class ProjectItem(models.Model):
    title = models.CharField('titulo', max_length=80, unique=True)
    description = models.TextField('Descripcion',max_length=255)
    url_github = models.TextField('URL',max_length=255)
    image = models.ImageField('Imagen',upload_to='images/')
    tags = models.CharField('Tags',max_length=100)
   # create_at =  models.DateTimeField(default=timezone.now())
   
    def delete(self,using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete(using, keep_parents)
    class Meta:  
        db_table = "proyect_item"  


class VisitorIP(models.Model):
    ip_address= models.GenericIPAddressField()
    create_at = models.DateTimeField(null=True,editable=False)
    last_visit = models.DateTimeField(null=True)

    class Meta:  
        db_table = "visitor_ip" 

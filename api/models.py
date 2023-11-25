from django.db import models
from django.core.validators import RegexValidator
from ckeditor_uploader.fields import RichTextUploadingField
from django.dispatch import receiver
# Create your models her
from django.db.models.signals import pre_save
import requests

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Adventage(models.Model):
    title =  models.CharField(max_length=100)
    poster = models.ImageField(upload_to="images/")
    tags =  models.ManyToManyField(Tag)
    body = RichTextUploadingField()

    def __str__(self):
        return self.title
    

class Course(models.Model):
    name = models.CharField(max_length=200)
    body = RichTextUploadingField()
    order = models.IntegerField(default=1)
    image = models.ImageField(upload_to="images/")

    class Meta:
        ordering = ('order', )

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Author(models.Model):
    full_name  = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name



class Article(models.Model):
    poster = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT) # PROTECT-saqlash 
    tags = models.ManyToManyField(Tag) #
    body = RichTextUploadingField()
    created_at = models.DateField(auto_now_add=True)
    author  = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
    

class Gallery(models.Model):
    title  = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/")
   

    def __str__(self):
        return self.title
    

class Way2Job(models.Model):
    title  = models.CharField(max_length=100)
    body = RichTextUploadingField()
   

    def __str__(self):
        return self.title
    
class ApplicationForm(models.Model):
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50,
                                     validators=[RegexValidator(r'^\+998\d{9}$')])

    def __str__(self):
        return f"{self.full_name} - {self.phone_number}"
    
@receiver( pre_save, sender=ApplicationForm)
def sent_to_telegram_bot(sender,instance,**kwargs):
    TOKEN = "6448240141:AAHmrXZzyyaf3Jfzibzmq8Sidd_oUJE51Z8"
    CHAT_ID = 1731912005

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    text = f"""
    Arizachining ismi: {instance.full_name}\n
    Telefon raqami: {instance.phone_number}
    """

    params = {
        "chat_id": CHAT_ID,
        "text": text
    }


    requests.post(url=url, params=params)

from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from user.models.user_model import CustomUserModel
from base.models.helpers.adress_model import AdressModel
from django.template.defaultfilters import  slugify
# Create your models here.

class PersonModel(DateTimeModel):
    GENDER_CHOICES = (
        ('M','MALE'),
        ('F','FEMALE'),
        ('O','OTHER'),
     )
    
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, related_name='%(class)s_profile')
    adress = models.OneToOneField(AdressModel, on_delete=models.CASCADE, related_name='%(class)s_address')
    
    birthday = models.DateTimeField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    url_picture = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    slug = models.SlugField(default="",blank=True)

    class Meta:
        abstract = True
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(f'{self.last_name} {self.first_name}')
        super(PersonModel, self).save(*args, **kwargs)
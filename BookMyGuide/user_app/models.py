from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

class GuideRegisterModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    bio_desc = models.TextField(max_length=225)
    email = models.EmailField()
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_OTHERS = 2
    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHERS, 'Others'),
    ]
    gender = models.IntegerField(choices=GENDER_CHOICES)
    address = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    user_img = models.ImageField(upload_to='UserImg', blank=True, null=True)
    citizenship_img = models.ImageField(upload_to='Citizenship')
    Liscence_img = models.ImageField(upload_to='LiscenceImg')
    LANGUAGES = (
        ('Nepali', 'Nepali'),
        ('English', 'English'),
        ('Spanish', 'Spanish'),
        ('Hindi', 'Hindi'),
        ('Chinese', 'Chinese'),
    )
    languages = MultiSelectField(choices=LANGUAGES)
    L_CHOICES = (
        ('Kathmandu', 'Kathmandu'),
        ('Bhaktapur', 'Bhaktapur'),
        ('Lalitpur', 'Lalitpur'),
        ('Everest Base Camp', 'Everest Base Camp'),
        ('Annapurna Base Camp', 'Annapurna Base Camp'),
    )
    locations = MultiSelectField(choices=L_CHOICES)
    is_guide = models.BooleanField(default=1)

    def __str__(self):
        return(self.username)
    
class TouristRegisterModel(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_OTHERS = 2
    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHERS, 'Others'),
    ]
    gender = models.IntegerField(choices=GENDER_CHOICES)
    is_tourist = models.BooleanField(default=1)

    def __str__(self):
        return(self.username)


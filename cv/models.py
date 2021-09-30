from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class CVmaker(models.Model):
    title = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'CVmaker'

class Employee(models.Model):
    Format = (
        ('Fancy', 'Fancy'),
        ('Casual', 'Casual'),
        ('Modern', 'Modern'),
        ('Classic', 'Classic'),
        ('Banking', 'Banking'),
        ('Neat', 'Neat'),
    )
    sex = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    CV_format = models.CharField(
        max_length=100, 
        blank=False, 
        choices=Format,
        help_text="Choose CV format in drop down list.")
    name = models.CharField(max_length=200, blank=True)
    date_of_birth = models.DateTimeField(null=True, default="yyyy-mm-dd" )
    gender = models.CharField(max_length=20, blank=True, choices=sex)
    Home_address = models.CharField(max_length=200, blank=True)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=200, blank=True)
    BSc = models.CharField(max_length=2000, blank=True, help_text="BSc title, University name.")
    BSc_start_date = models.DateTimeField(blank=True, null = True )
    BSc_end_date = models.DateTimeField(blank=True, null = True )
    MSc = models.CharField(
        max_length=2000, 
        blank=True,
        help_text= "Skip if you don't have one.")
    MSc_start_date = models.DateTimeField(blank=True, null = True )
    MSc_end_date = models.DateTimeField(blank=True, null = True )
    training = models.CharField(
        max_length=2000, 
        blank=True,
        help_text="Skip if you don't have one.")
    training_start_date = models.DateTimeField(blank=True, null = True )
    training_end_date = models.DateTimeField(blank=True, null = True )
    work_experience = models.CharField(
        max_length=2000, 
        blank=True,
        help_text="Skip if you don't have one.")
    organization = models.CharField(max_length=200, blank=True)
    work_exp_start_date = models.DateTimeField(blank=True, null = True)
    work_exp_end_date = models.DateTimeField(blank=True, null = True )
    computer_skills = models.CharField(
        max_length=500, 
        blank = True,
        help_text="List all skills from higher to lower.")
    other_skills = models.CharField(
        max_length=1000, 
        blank = True,
        help_text="Your personal qualities other than proffesional skills?")
    references = models.CharField(
        max_length=2000, 
        blank = True,
        help_text="Name email address and phone.")
    photo = models.FileField(blank=True, help_text="Recomended but not mandatory.")
    cvmaker = models.ManyToManyField(
        CVmaker,
        help_text = "By selecting RATIFY I hereby declare that the information provided is true and correct.",
        blank = False
    )
   

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Employee'


    


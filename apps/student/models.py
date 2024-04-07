from django.db import models
from apps.core.models import TimestampedModel



# Create your models here.
class Student(TimestampedModel):
    class SubjectType(models.TextChoices):
        MATHEMATICS  = 'mathematics' , 'Mathematics'
        PSYCHOLOGY   = 'psychology'  , 'Psychology'
        CHEMISTRY    = 'chemistry'   , 'Chemistry'
        MICROBIOLOGY = 'microbiology', 'Microbiology '
        BOTANY       = 'botany' , 'Botany'
        ANATOMY      = 'anatomy', 'Anatomy'
        GEOLOGY      = 'geology', 'Geology'

    class GenderType(models.TextChoices):
        MALE   = 'male'  , 'Male'
        FEMALE = 'female', 'Female'
        OTHER  = 'other' , 'Other'

    name  = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    gender = models.CharField(
        max_length=10, choices=GenderType.choices, null=True, blank=True
    )
    image = models.ImageField(upload_to='Student/Images/', null=True, blank=True)
    cv    = models.FileField(upload_to='Student/CV/', null=True, blank=True)
    dob   = models.DateField(null=True, blank=True)
    city  = models.ForeignKey()

    # roll = models.IntegerField(unique=True)
    roll = models.IntegerField()
    subject = models.CharField(max_length=250, choices=SubjectType.choices, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    
    class Meta:
        # managed = False
        db_table = 'students'

    def __str__(self):
        return self.name
    



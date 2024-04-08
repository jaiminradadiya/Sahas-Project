from django.db import models

# Create your models here.
class Gallery(models.Model):
    image_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image_path = models.ImageField(upload_to='gallery/')
    image_info = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Member(models.Model):
    member_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='member_photos/', blank=True, null=True)
    working_role = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Volunteer(models.Model):
    volunteer_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='volunteer_photos/', blank=True, null=True)
    aadhaarcard = models.CharField(max_length=20, unique=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Inquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    contact_no = models.CharField(max_length=20)
    subject = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.subject
        
class NGORegistration(models.Model):
    image = models.ImageField(upload_to='ngo_images/', blank=True, null=True)
    name = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=20)
    email = models.EmailField()
    key_issues = models.TextField()
    pan_no = models.CharField(max_length=20)
    registration_certificate_no = models.CharField(max_length=50)
    eighty_g_twelve_a_no = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class AddNGO(models.Model):
    reg_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    web_url = models.URLField(blank=True)
    pan_no = models.CharField(max_length=20)
    registration_certificate_no = models.CharField(max_length=50)
    eighty_g_twelve_a_no = models.CharField(max_length=50)
    image = models.ImageField(upload_to='ngo_images/', blank=True, null=True)

    def __str__(self):
        return self.name
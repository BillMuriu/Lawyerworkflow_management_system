from django.db import models
from django.contrib.auth.models import User

# Create your models here.




# class Task(models.Model):
#     task_name = models.CharField(max_length=100)
#     assigned_to = models.ManyToManyField(User, blank=True)
#     task_description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.task_name



class Matter(models.Model):
    TYPE_CHOICES = (
        ('Commercial', 'Commercial'),
        ('Litigation', 'Litigation'),
        ('Conveyancing', 'Conveyancing'),
    )

    CATEGORY_CHOICES = (
        ('Active', 'Active'),
        ('Closed', 'Closed'),
    )
    type = models.CharField(max_length=200, choices=TYPE_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES, default='Active')
    ref_code = models.CharField(max_length=200, blank=True)
    open_date = models.DateField()
    close_date = models.DateField(blank=True, null=True)
    original_lawyer = models.CharField(max_length=200)
    current_lawyer = models.CharField(max_length=200)
    assigned_to = models.CharField(max_length=200, default='string') # this should be a user
    private = models.BooleanField(default=False)
    client = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title





class Task(models.Model):
    STATUS_CHOICES = (
        ('Upcoming', 'Upcoming'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )

    PRIORITY_CHOICES = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )

    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default='Upcoming')
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=200, choices=PRIORITY_CHOICES, default='Low')
    matter = models.ForeignKey(Matter, on_delete=models.CASCADE)
    assigned_to = models.ManyToManyField(User, blank=True) # this should be a user
    private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title





class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    priority = models.CharField(max_length=200)
    matter = models.ForeignKey(Matter, on_delete=models.CASCADE)
    assigned_to = models.CharField(max_length=200) # this should be a user
    private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Document(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    matter = models.ForeignKey(Matter, on_delete=models.CASCADE)
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.name




class Note(models.Model):
    TYPE_CHOICES = (
        ('General', 'General'),
        ('Client', 'Client'),
        ('Matter', 'Matter'),
        ('Task', 'Task'),
        ('Event', 'Event'),
        ('Document', 'Document'),
    )
    category = models.CharField(max_length=200, choices=TYPE_CHOICES)
    subject = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    private = models.BooleanField(default=False)
    matter = models.ForeignKey(Matter, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject



class Client(models.Model):
    TYPE_CHOICES = (
        ('Individual', 'Individual'),
        ('Business', 'Business'),
    )

    type = models.CharField(max_length=200, choices=TYPE_CHOICES)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    primary_phone = models.CharField(max_length=200)
    secondary_phone = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200)
    website = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
   

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    website = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
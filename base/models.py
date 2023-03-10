from django.db import models
from django.contrib.auth.models import User

# Create your models here.





class Lawyer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
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


class IndividualClient(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(unique=True)
    primary_phone = models.CharField(max_length=200)
    secondary_phone = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200)
    website = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    def save(self, *args, **kwargs):
        if not self.pk:
            # create a new user for the client
            user = User.objects.create_user(username=self.email, email=self.email)
            user.set_password('defaultpassword')
            user.save()
            self.user = user
        super().save(*args, **kwargs)



class BusinessClient(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    primary_phone = models.CharField(max_length=200)
    secondary_phone = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200)
    website = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            # create a new user for the client
            user = User.objects.create_user(username=self.email, email=self.email)
            user.set_password('defaultpassword')
            user.save()
            self.user = user
        super().save(*args, **kwargs)




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
    original_lawyer = models.ForeignKey(Lawyer, related_name='original_lawyer', on_delete=models.CASCADE)
    current_lawyer = models.ForeignKey(Lawyer, related_name='current_lawyer', on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='matters', blank=True)
    private = models.BooleanField(default=False)
    individual_client = models.ManyToManyField(IndividualClient, blank=True)
    business_client = models.ForeignKey(BusinessClient, on_delete=models.CASCADE, blank=True, null=True)
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
    matter = models.ForeignKey(Matter, on_delete=models.CASCADE, blank=True, null=True)
    assigned_to = models.ManyToManyField(User, blank=True) # this should be a user
    created_by = models.ForeignKey(User, related_name='created_tasks', on_delete=models.CASCADE)
    modified_by = models.ForeignKey(User, related_name='modified_tasks', on_delete=models.CASCADE, blank=True, null=True)
    private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title





class Event(models.Model):

    PRIORITY_CHOICES = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )

    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    priority = models.CharField(max_length=200, choices=PRIORITY_CHOICES, default='Low')
    matter = models.ForeignKey(Matter, on_delete=models.CASCADE, blank=True, null=True)
    assigned_to = models.ManyToManyField(User, blank=True, related_name='assigned_events')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_events', blank=True, null=True)
    private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name




class Document(models.Model):

    CATEGORY_CHOICES = (
        ('Statutes', 'Statutes'),
        ('Letters', 'Letters'),
        ('Case Law', 'Case Law'),
    )

    name = models.CharField(max_length=200)
    link = models.URLField( blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    matter = models.ForeignKey(Matter, on_delete=models.CASCADE, blank=True, null=True)
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES)
    file = models.FileField(upload_to='documents/', blank=True, null=True)

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
    matter = models.ForeignKey(Matter, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.subject


class FirmDetails(models.Model):
    name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    website = models.URLField()
    address = models.TextField()
    currency_code = models.CharField(max_length=200)
    tax_pin = models.CharField(max_length=200)
    physical_address = models.TextField()
    bank = models.CharField(max_length=200)
    bank_account_name = models.CharField(max_length=200)
    bank_account_number = models.CharField(max_length=200)
    bank_branch = models.CharField(max_length=200)

    def __str__(self):
        return self.name

   
class FeeNote(models.Model):
    matter = models.ForeignKey(Matter, on_delete=models.CASCADE, blank=True, null=True)
    individual_client = models.ForeignKey(IndividualClient, on_delete=models.CASCADE, blank=True, null=True)
    business_client = models.ForeignKey(BusinessClient, on_delete=models.CASCADE, blank=True, null=True)
    billed_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    due_date = models.DateField()
    date_billed = models.DateField()
    billable = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return self.name

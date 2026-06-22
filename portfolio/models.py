from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=120)
    short_description = models.TextField()
    icon = models.CharField(max_length=8, default='✦')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=80)
    percentage = models.PositiveIntegerField(default=80)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=120, default='Web Development')
    description = models.TextField()
    tech_stack = models.CharField(max_length=250, help_text='Example: Django, Python, HTML, CSS')
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    live_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=25, blank=True)
    interest = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} - {self.email}'

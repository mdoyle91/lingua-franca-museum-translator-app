from django.db import models
from django.urls import reverse
#from django.contrib.auth.models import User

class Institution(models.Model):
    name = models.TextField(max_length=25)
    location = models.TextField(max_length=25)
    # user = models.ForeignKey(User) Add this once the User has been created.
    # Will I want more locations here such as location_english, Location_spanish, location_portugues, so I can render them conditionally based on selected language?
     #user_id = models.ForeignKey(User, on_delete=models.CASCADE) #I think I don't want the on delete Cascade here as that would eliminate the institution if I delete the user, and this is ideally going to be a many-to-many relationship.

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('institution-detail', kwargs={'institution_id: self.id'})

class Exhibit(models.Model):
    institution_id = models.ForeignKey(Institution, on_delete=models.CASCADE) #Required, look up what to add to ensure it's included
    name = models.CharField(max_length=1000) #Required, look up what to add to ensure it's included
    exhibit_number = models.IntegerField() #Required, look up what to add to ensure it's included
    exhibit_image = models.TextField(max_length=1000) #Optional
    original_language_text = models.TextField(max_length=1000) #Required, look up what to add to ensure it's included
    english_language_text = models.TextField(max_length=1000)  #Optional
    spanish_language_text = models.TextField(max_length=1000)  #Optional
    portuguese_language_text = models.TextField(max_length=1000)  #Optional

    def __str__(self):
        return self.name

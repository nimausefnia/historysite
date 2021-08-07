from django.db import models

class Entry(models.Model):
  
  text=models.TextField()
  date_posted=models.DateTimeField(auto_now_add=True)


  class Meta:

      verbose_name_plural='Entries'

  def __str__(self):

   return "Entry #{}" .format(self.id)




   
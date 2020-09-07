from django.db import models

# Create your models here.

"""ARTISTS = {
    'jean-claude': {'name':'Jean-Claude'},
    'jeanne': {'name':'Jeanne d\'arc'},
    'nathalie': {'name':'Nathalie'},
    'sese': {'name':'Sebastine'},
}

ALBUMS = [
    {'name':"La fin du monde", 'artists':[ARTISTS['jeanne']]},
    {'name':"L'homme est mort", 'artists':[ARTISTS['jean-claude']]},
    {'name':"Le désert", 'artists':[ARTISTS['sese']]},
    {'name':"Vivons enssemble", 'artists':[ARTISTS['jeanne'], ARTISTS['sese']]},
    {'name':"L'amour", 'artists':[ARTISTS['sese']]},
    {'name':"Diament", 'artists':[ARTISTS['jean-claude'], ARTISTS['nathalie']]},
    {'name':"Qui suis je", 'artists':[ARTISTS['nathalie']]},
    {'name':"Pour toi", 'artists':[ARTISTS['nathalie']]},
    {'name':"Le dernier", 'artists':[ARTISTS['jean-claude']]},
    {'name':"Vent", 'artists':[ARTISTS['sese']]},
]"""

class Artist(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name

class Album(models.Model):
    ref = models.IntegerField(null=True)
    title = models.CharField(max_length=200)
    avalible = models.BooleanField(default=True)
    picture = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    artists = models.ManyToManyField(Artist, related_name='albums', blank=True)

    def __str__(self):
        return self.title

class Boocking(models.Model):
    contacted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    album = models.OneToOneField(Album, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.contact.name
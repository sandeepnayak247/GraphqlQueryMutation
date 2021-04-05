from django.contrib import admin
from .models import Actor,Director,Movie,Movie_Cast,Reviewer,Generes,Movie_Genres

# Register your models here.
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Movie_Cast)
admin.site.register(Reviewer)
admin.site.register(Generes)
admin.site.register(Movie_Genres)
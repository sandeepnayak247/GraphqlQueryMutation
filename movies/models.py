from django.db import models

# Create your models here.
class Actor(models.Model):
    act_id=models.IntegerField(null=True)
    act_fname=models.CharField(max_length=20)
    act_lname=models.CharField(max_length=20)
    act_gender=models.CharField(max_length=1)

    def __str__(self):
        return str(self.act_id)

class Director(models.Model):
    dir_id=models.IntegerField(null=True)
    dir_fname=models.CharField(max_length=20)
    dir_lname=models.CharField(max_length=20)
    
    def __str__(self):
        return self.dir_fname

class Movie(models.Model):
    mov_id=models.IntegerField(null=True)
    mov_name=models.CharField(max_length=20)
    mov_year=models.IntegerField(null=True)
    mov_dt_rel=models.DateField(null=True)
    mov_rel_country=models.CharField(max_length=20)
    mov_time=models.IntegerField(null=True)

    def __str__(self):
        return self.mov_name

class Movie_Cast(models.Model):
    act_id=models.ForeignKey(Actor,default=1,on_delete=models.DO_NOTHING)
    role=models.CharField(max_length=20)

    def __str__(self):
        return self.role

class Reviewer(models.Model):
    rev_id=models.IntegerField(null=True)
    rev_name=models.CharField(max_length=20)

    def __str__(self):
        return self.rev_name

class Generes(models.Model):
    gen_id=models.IntegerField(null=True)
    gen_title=models.CharField(max_length=20)

    def __str__(self):
        return self.gen_title

class Movie_Genres(models.Model):
    mov_id=models.ForeignKey(Movie,default=1,on_delete=models.DO_NOTHING)
    gen_id=models.ForeignKey(Generes,default=1,on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return str(self.mov_id)
        
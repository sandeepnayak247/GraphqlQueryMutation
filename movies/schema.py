import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from .models import Actor,Director,Movie,Movie_Cast,Reviewer,Generes,Movie_Genres

class ActorsType(DjangoObjectType):
    class Meta:
        model=Actor
        fields=("act_id","act_fname","act_lname","act_gender")

class ActorByIdType(DjangoObjectType):
    class Meta:
        model=Actor


class DirectorsType(DjangoObjectType):
    class Meta:
        model=Director
        fields=("dir_id","dir_fname","dir_lname")

class MoviesType(DjangoObjectType):
    class Meta:
        model=Movie
        fields=("mov_id","mov_name","mov_year","mov_dt_rel", "mov_rel_country","mov_time")

class Movie_CastType(DjangoObjectType):
    class Meta:
        model=Movie_Cast
        fields=("act_id","role")

class ReviewerType(DjangoObjectType):
    class Meta:
        model=Reviewer
        fields=("rev_id","rev_name")

class GeneresType(DjangoObjectType):
    class Meta:
        model=Generes
        fields=("gen_id","gen_name")

class Query(graphene.ObjectType):
    all_actors=DjangoListField(ActorsType)
    all_directors=DjangoListField(DirectorsType)
    all_movies=DjangoListField(MoviesType)
    all_movie_cast=DjangoListField(Movie_CastType)
    all_review=DjangoListField(ReviewerType)
    all_generes=DjangoListField(GeneresType)
    
    actor = graphene.Field(ActorByIdType,id=graphene.Int())

    def resolve_all_actors(root,info):
        return Actor.objects.all()

    def resolve_actor(root, info, id):
        return Actor.objects.get(pk=id)
        
    def resolve_all_directors(root,info):
        return Director.objects.all()

    def resolve_all_movies(root,info):
        return Movie.objects.all()

    def resolve_movie_cast(root,info):
        return Movie_Cast.objects.all()

    def resolve_all_review(root,info):
        return Reviewer.objects.all()

    def resolve_all_generes(root,info):
        return Generes.objects.all()


class CreateActorMutation(graphene.Mutation):

    class Arguments:
        act_id=graphene.Int(required=True)
        act_fname=graphene.String(required=True)
        act_lname=graphene.String(required=True)
        act_gender=graphene.String(required=True)
    
    actor=graphene.Field(ActorsType)

    @classmethod
    def mutate(cls,root,info,act_id,act_fname,act_lname,act_gender):
        actor=Actor(act_id=act_id,act_fname=act_fname,act_lname=act_lname,act_gender=act_gender)
        # actor=Actor()
        actor.save()
        return CreateActorMutation(actor=actor)



class UpdateActorMutation(graphene.Mutation):

    class Arguments:
        act_id=graphene.ID()
        act_fname=graphene.String(required=True)
        act_lname=graphene.String(required=True)
        act_gender=graphene.String(required=True)
    
    actor=graphene.Field(ActorsType)

    @classmethod
    def mutate(cls,root,info,act_id,act_fname,act_lname,act_gender):
        actor=Actor.objects.get(act_id=act_id)
        actor.act_fname=act_fname
        actor.act_lname=act_lname
        actor.act_gender=act_gender
        actor.act_id=act_id
        # actor=Actor()
        #actor=Actor(act_fname=act_fname,act_lname=act_lname,act_gender=act_gender)
        actor.save()
        return UpdateActorMutation(actor=actor)

class DeleteActorMutation(graphene.Mutation):

    class Arguments:
        act_id=graphene.ID()
        
    
    actor=graphene.Field(ActorsType)

    @classmethod
    def mutate(cls,root,info,act_id):
        actor=Actor.objects.get(act_id=act_id)
        
        # actor=Actor()
        #actor=Actor(act_fname=act_fname,act_lname=act_lname,act_gender=act_gender)
        actor.delete()
        return DeleteActorMutation(actor=actor)



class CreateDirMutation(graphene.Mutation):
    class Arguments:
        dir_id=graphene.Int(required=True)
        dir_fname=graphene.String(required=True)
        dir_lname=graphene.String(required=True)
        
    director=graphene.Field(DirectorsType)

    
    @classmethod
    def mutate(cls,root,info,dir_id,dir_fname,dir_lname):
        director=Director(dir_id=dir_id,dir_fname=dir_fname,dir_lname=dir_lname)
        # actor=Actor()
        director.save()
        return CreateDirMutation(director=director)
      

class UpdateDirMutation(graphene.Mutation):

    class Arguments:
        dir_id=graphene.ID()
        dir_fname=graphene.String(required=True)
        dir_lname=graphene.String(required=True)
        
    
    director=graphene.Field(DirectorsType)

    @classmethod
    def mutate(cls,root,info,dir_id,dir_fname,dir_lname):
        director=Director.objects.get(dir_id=dir_id)
        director.dir_fname=dir_fname
        director.dir_lname=dir_lname
        director.dir_id=dir_id
        # actor=Actor()
        #actor=Actor(act_fname=act_fname,act_lname=act_lname,act_gender=act_gender)
        director.save()
        return UpdateDirMutation(director=director)


class DeleteDirMutation(graphene.Mutation):

    class Arguments:
        dir_id=graphene.ID()
        
    
    director=graphene.Field(ActorsType)

    @classmethod
    def mutate(cls,root,info,dir_id):
        director=Director.objects.get(dir_id=dir_id)
        
        # actor=Actor()
        #actor=Actor(act_fname=act_fname,act_lname=act_lname,act_gender=act_gender)
        director.delete()
        return DeleteDirMutation(director=director)


class CreateMovMutation(graphene.Mutation):
    class Arguments:
        mov_id=graphene.Int(required=True)
        mov_name=graphene.String(required=True)
        mov_year=graphene.Int(required=True)
        mov_rel_country=graphene.String(required=True)

               
    movie=graphene.Field(MoviesType)

    
    @classmethod
    def mutate(cls,root,info,mov_id,mov_name,mov_year,mov_rel_country):
        director=Director(mov_id=mov_id,mov_name=mov_name,mov_year=mov_year,mov_rel_country=mov_rel_country)
        # actor=Actor()
        movie.save()
        return CreateMovMutation(movie=movie)


class UpdateMovMutation(graphene.Mutation):

    class Arguments:
        mov_id=graphene.ID()
        mov_name=graphene.String(required=True)
        mov_year=graphene.Int(required=True)
        mov_rel_country=graphene.String(required=True)

        
    
    movie=graphene.Field(MoviesType)

    @classmethod
    def mutate(cls,root,info,mov_id,mov_name,mov_year,mov_rel_country):
        movie=Movie.objects.get(mov_id=mov_id)
        movie.mov_name=mov_name
        movie.mov_year=mov_year
       
        movie.mov_rel_country=mov_rel_country
        # actor=Actor()
        #actor=Actor(act_fname=act_fname,act_lname=act_lname,act_gender=act_gender)
        movie.save()
        return UpdateMovMutation(movie=movie)

class DeleteMovMutation(graphene.Mutation):

    class Arguments:
        mov_id=graphene.ID()
        
    
    movie=graphene.Field(ActorsType)

    @classmethod
    def mutate(cls,root,info,mov_id):
        movie=Movie.objects.get(mov_id=mov_id)
        
        # actor=Actor()
        #actor=Actor(act_fname=act_fname,act_lname=act_lname,act_gender=act_gender)
        movie.delete()
        return DeleteMovMutation(movie=movie)


class CreateRevMutation(graphene.Mutation):
    class Arguments:
        rev_id=graphene.Int(required=True)
        rev_name=graphene.String(required=True)
        
        
    reviewer=graphene.Field(ReviewerType)

    
    @classmethod
    def mutate(cls,root,info,rev_id,rev_name):
        director=Director(rev_id=rev_id,rev_name=rev_name)
        # actor=Actor()
        reviewer.save()
        return CreateRevMutation(reviewer=reviewer)
      

class UpdateRevMutation(graphene.Mutation):

    class Arguments:
        rev_id=graphene.ID()
        rev_name=graphene.String(required=True)
        
        
    
    reviewer=graphene.Field(ReviewerType)

    @classmethod
    def mutate(cls,root,info,rev_id,rev_name):
        reviewer=Reviewer.objects.get(rev_id=rev_id)
        reviewer.rev_name=rev_name
        reviewer.rev_id=rev_id
        # actor=Actor()
        #actor=Actor(act_fname=act_fname,act_lname=act_lname,act_gender=act_gender)
        reviewer.save()
        return UpdateRevMutation(reviewer=reviewer)


class DeleteRevMutation(graphene.Mutation):

    class Arguments:
        rev_id=graphene.ID()
        
    
    reviewer=graphene.Field(ActorsType)

    @classmethod
    def mutate(cls,root,info,rev_id):
        reviewer=reviewer.objects.get(rev_id=rev_id)
        
        # actor=Actor()
        #actor=Actor(act_fname=act_fname,act_lname=act_lname,act_gender=act_gender)
        reviewer.delete()
        return DeleteRevMutation(reviewer=reviewer)


class CreateMovieCastMutation(graphene.Mutation):
    class Arguments:
        act_id=graphene.ID(ActorsType,required=True)
        role=graphene.String(required=True)
        
        
    movieCast=graphene.Field(Movie_CastType)

    
    @classmethod
    def mutate(cls,root,info,act_id,role):
        movieCast=Movie_Cast(act_id=act_id,role=role)
        # actor=Actor()
        movieCast.save()
        return CreateMovieCastMutation(movieCast=movieCast)
      

class Mutation(graphene.ObjectType):
    create_act=CreateActorMutation.Field()
    update_act=UpdateActorMutation.Field()
    delete_act=DeleteActorMutation.Field()
    create_dir=CreateDirMutation.Field()
    update_dir=UpdateDirMutation.Field()
    delete_dir=DeleteDirMutation.Field()
    create_mov=CreateMovMutation.Field()
    update_mov=UpdateMovMutation.Field()
    delete_mov=DeleteMovMutation.Field()
    create_rev=CreateRevMutation.Field()
    update_rev=UpdateRevMutation.Field()
    delete_rev=DeleteRevMutation.Field()
    create_movieCast=CreateMovieCastMutation.Field()


schema=graphene.Schema(query=Query,mutation=Mutation)
from graphene_django.views import GraphQLView
from movies.schema import schema
from django.urls import path

urlpatterns = [
    path('graphql',GraphQLView.as_view(graphiql=True,schema=schema)),
]
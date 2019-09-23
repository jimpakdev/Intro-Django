from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import Note

from graphene_django.filter import DjangoFilterConnectionField

class NoteType(DjangoObjectType):

    class Meta:
        model = Note
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'content': ['exact', 'icontains'],
        }


class Query(graphene.ObjectType):
    notes = DjangoFilterConnectionField(NoteType)

    # notes = graphene.List(NoteType)

    # def resolve_notes(self, info):
    #     return Note.objects.all()


class CreateNote(graphene.Mutation):

    class Arguments:
        title = graphene.String()
        content = graphene.String()

    note = graphene.Field(NoteType)
    ok = graphene.Boolean()

    def mutate(self, info, title, content):
        new_note: Note(title=title, content=content)
        new_note.save()

        return CreateNote(note=new_note, ok=True)


class Mutation(graphene.ObjectType):
    create_note = CreateNote.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

# connecting to graphene
schema = graphene.Schema(query=Query)

from rest_framework import serializers, viewsets
from .models import PersonalNote

# which models we want to expose
class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')

    def create(self, validated_data):
        user = self.context['request'].user
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note

# which rows we want to see
class PersonalNoteViewSet(viewsets.ModelViewSet):
    # which serializer to use
    serializer_class = PersonalNoteSerializer
    # which rows to return
    queryset = PersonalNote.objects.none()

    def get_queryset(self):
        # import pdb; pdb.set_trace()

        logged_in_user = self.request.user

        if logged_in_user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=logged_in_user)
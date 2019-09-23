from django.contrib import admin

# tell admin interface which tables we want to see
from .models import Note
from .models import PersonalNote


# to get read-only fields to show up in interface
class NoteAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')

#### Register your models here.

# register the Note model with admin site
admin.site.register(Note, NoteAdmin)
admin.site.register(PersonalNote)


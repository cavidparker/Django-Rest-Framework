from django.contrib import admin
from .models import Play,Poem

# Register your models here.

@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    list_display = ['id','genre', 'title', 'pages']


@admin.register(Poem)
class PoemAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'style', 'lines', 'stanzas']

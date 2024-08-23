from django.contrib import admin
from .models import *

admin.site.register(Autor)
admin.site.register(Postagem)
admin.site.register(Tag)
admin.site.register(Comentario)

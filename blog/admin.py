from django.contrib import admin
from .models import Post
from django_summernot.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')



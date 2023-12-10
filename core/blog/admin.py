from django.contrib import admin
from .models import Category,Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','category','created_date','status']
    list_filter = ['status','created_date']
    search_fields = ['title','content']
    class Meta:
        model = Post
        
admin.site.register(Category)
admin.site.register(Post)

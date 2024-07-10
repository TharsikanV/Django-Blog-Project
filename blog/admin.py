from django.contrib import admin
from .models import Post,Category

# # Register your models here.
# admin.site.register(Post)
# admin.site.register(Category)

# customize admin interface
class PostAdmin(admin.ModelAdmin):
    list_display=('title','content')#enna field kaadanumnu sollalaam
    search_fields=('title','content')#search box ah uruvaakitharum antha fiels kku
    list_filter=('category','created_at')

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Category)

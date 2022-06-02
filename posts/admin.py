from django.contrib import admin


from .models import Post

# allows admin to view models in admin site
admin.site.register(Post)

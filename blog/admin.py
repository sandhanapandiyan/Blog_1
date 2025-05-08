from django.contrib import admin
from django import forms
from .models import Post, Tag

class PostAdminForm(forms.ModelForm):
    image = forms.ImageField(required=False, help_text="Upload an image for the post.")

    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'tags', 'is_published', 'image']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.cleaned_data.get('image'):
            image_file = self.cleaned_data['image']
            instance.image_binary = image_file.read()
        if commit:
            instance.save()
        return instance

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'author', 'created_at', 'is_published')
    list_filter = ('is_published', 'tags', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'content', 'image', 'author', 'tags')
        }),
        ('Status', {
            'fields': ('is_published',)
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
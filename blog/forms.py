from django import forms
from .models import Post, Tag

class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    image = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'tags', 'is_published']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        if 'image' in self.files:
            image_file = self.files['image']
            instance.image_binary = image_file.read()
        if commit:
            instance.save()
        return instance


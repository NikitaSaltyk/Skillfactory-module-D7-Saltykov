from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'postCategory',
            'categoryType',
            'author'
        ]

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        title = cleaned_data.get("title")

        if text == title:
            raise ValidationError(
                "Текст записи не должен быть идентичен названию."
            )

        return cleaned_data
from django import forms

from Ww_Learning.app.models import Course


class VideoForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'video_file')

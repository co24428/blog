from django import forms
from .models import Blog

#기존의 모델에서 일부를 발췌, 오라클의 테이블과 뷰같은 느낌인 듯
class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body']
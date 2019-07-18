from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .models import Blog2
#forms를 연결해준다.
from .forms import BlogPost

# Create your views here.

def home(request):
    blog2s = Blog2.objects
    blogs = Blog.objects
    #블로그 모든 글들을 대상으로
    blog_list=Blog.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list,3)
    #request된 페이지가 뭔지를 알아내고 ( request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)
    #경로 오류 나옴, 오류 뜨면 모든 blog를 home.html, home으로 바꿔줘야 한다.
    return render(request,'blog/home.html',{'blogs':blogs,'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog_detail})

def new(request):
    form = BlogPost()
    return render(request,'blog/new.html',{'form':form})

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

#POST일 때는 데이터만 불러온 후 타임 붙혀서 최종저장, 아닐때는 다시 쓰라고 함.
# 이것을 해주면 기존의 new와 create로 가던 글쓰기 버튼의 링크를 수정해주어야 함. ( 설명에는 없음 )
def blogpost(request):
    if request.method =='POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request,'blog/new.html',{'form':form}) 

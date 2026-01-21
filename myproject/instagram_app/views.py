from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import Post,Comment

def get_demo_user():
    return User.objects.first()
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request,'instagram_app/post_list.html',{"posts":posts})
def post_create(request):
    if request.method =="POST":
        user = get_demo_user()
        caption = request.POST.get("caption")
        image = request.FILES.get("image")
        Post.objects.create(
            user=user,caption=caption,image=image)
        return redirect("post_list")
    return render(request,"instagram_app/post_form.html")
def post_detail(request,id):
    post = get_object_or_404(Post,id=id)
    return render(request,"instagram_app/post_detail.html",{"post":post})

def add_comment(request,id):
    post = get_object_or_404(Post,id=id)
    if request.method =="POST":
        Comment.objects.create(
            post=post,
            user=get_demo_user(),
            text=request.POST.get("text")
        )
        return redirect("post_detail",id=id)
    return render(request,"instagram_app/comment_form.html",{"post":post})

def like_post(request,id):
    post = get_object_or_404(Post,id=id)
    user = get_demo_user()
    if user in post.likes.all():
       post.likes.remove(user)
    else:
        post.likes.add(user)
    return redirect("post_list")
from django.shortcuts import render, redirect, get_object_or_404
from .models import Diary6
# Create your views here.
def home(request):
    return render(request, 'home.html')

def list1(request):
    diaries = Diary6.objects.all()
    return render(request, 'list1.html', {'diaries':diaries})

def detail(request, id):
    diary = get_object_or_404(Diary6, pk = id)
    return render(request, 'detail.html', {'diary':diary})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_diary = Diary6()
    new_diary.title = request.POST['title']
    new_diary.body = request.POST['body']
    new_diary.save()
    return redirect('detail', new_diary.id)

def edit(request, id):
    edit_diary = Diary6.objects.get(id = id)
    return render(request, 'edit.html', {'diary': edit_diary})

def update(request, id):
    update_diary = Diary6.objects.get(id = id)
    update_diary.title = request.POST["title"]
    update_diary.body = request.POST['body']
    update_diary.save()
    return redirect('detail', update_diary.id)

def delete(request, id):
    delete_blog = Diary6.objects.get(id = id)
    delete_blog.delete()
    return redirect('list1')
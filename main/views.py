from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from main.models import Todo
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    todo_item = Todo.objects.all().order_by("-added_date")
    return render(request, 'main/index.html',{
      "todo_item": todo_item,
    })

@csrf_exempt
def add_todo(request):
  current_date = timezone.now()
  content = request.POST["content"]
  create_obj = Todo.objects.create(added_date=current_date, text=content)
  lf = Todo.objects.all().count

  return HttpResponseRedirect('/')

@csrf_exempt
def delete_todo(request, todo_id):
  Todo.objects.get(id=todo_id).delete()
  return HttpResponseRedirect('/')
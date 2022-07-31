import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import *
# from django.views.decorations.http import require_http_methods #이를 제외한 method에는 405 리턴
# import serialize
# Create your views here.
# @require_http_methods(['POST', "GET"])
def create_category(requests):
    if requests.method == "POST":

        body = json.loads(requests.body.decode('utf-8'))

        new_category = Category.objects.create(
            title = body['title'],
            view_auth = body['view_auth'],
            color = body['color']
        )

        new_category_json = {
            "id" : new_category.id,
            "title" : new_category.title,
            "view_auth" : new_category.view_auth,
            "color" : new_category.color,
            "pup_date" : new_category.pup_date,
        }

        return JsonResponse({
            "status": 200,
            "success" : True,
            "message": "생성 성공",
            "data": new_category_json
        })

    return JsonResponse({
        "status": 405,
        "success" : False,
        "message": "method error",
        "data": None
    })

def get_category_all(requests):
    if requests.method == "GET":
        category_all = Category.objects.all()

        category_json_all = []

        for category in category_all:
            category_json = {
                "id" : category.id,
                "title" : category.title,
                "view_auth" : category.view_auth,
                "color" : category.color,
                "pup_date" : category.pup_date,
            }

            category_json_all.append(category_json)
        
        return JsonResponse({
            "status": 200,
            "success" : True,
            "message": "생성 성공",
            "data": category_json_all
        })

def get_category(requests, id):
    if requests.method == "GET":
        
        category = get_object_or_404(Category, pk = id)

        category_json = {
                "id" : category.id,
                "title" : category.title,
                "view_auth" : category.view_auth,
                "color" : category.color,
                "pup_date" : category.pup_date,
            }

        return JsonResponse({
            "status": 200,
            "success" : True,
            "message": "읽기 성공",
            "data": category_json
        })

def update_category(request, id):
    if request.method == "PATCH":
        
        body = json.loads(request.body.decode('utf-8'))

        update_category = get_object_or_404(Category, pk = id)

        update_category.title = body['title']
        update_category.view_auth = body['view_auth']
        update_category.color = body['color']

        update_category.save()

        update_category_json = {
            "id": update_category.id,
            "title": update_category.title,
            "view_auth": update_category.view_auth,
            "color": update_category.color,
            "pup_date": update_category.pup_date,
        }

        return JsonResponse({
            'status': 200,
            'success': True,
            'message': '업데이트 성공!',
            'data': update_category_json
        })

    return JsonResponse({
                'status': 405,
                'success': False,
                'message': 'method error',
                'data': None
            })

def delete_category(request, id):


    if request.method == "DELETE":

        delete_category = get_object_or_404(Category, pk = id)

        delete_category.delete()
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': '삭제 성공!',
                'data': None    #삭제의 경우 성공해도 데이터를 줄게 없음
            })
            
    return JsonResponse({
                'status': 405,
                'success': False,
                'message': 'method error',
                'data': None
        })

def create_todo(request, category_id):
    if request.method == "POST":

        body = request.POST
        img = request.FILES['thumb_nail']

        new_todo = Todo.objects.create(
            category = get_object_or_404(Category, pk = category_id),
            content = body['content'],
            thumb_nail = img
        )

        new_todo_json = {
            "id" : new_todo.id,
            "content" : new_todo.content,
            "thumb_nail" : '/media/' + str(new_todo.thumb_nail),
            "pup_date" : new_todo.pup_date,
        }

        return JsonResponse({
            "status": 200,
            "success" : True,
            "message": "todo 생성 성공",
            "data": new_todo_json
        })

    return JsonResponse({
        "status": 405,
        "success" : False,
        "message": "method error",
        "data": None
    })

def get_todo(request):
    if request.method == "GET":

        todo_all = Todo.objects.all()

        todo_all_json = []

        for todo in todo_all:
            todo_json = {
                "id": todo.id,
                "content": todo.content,
                "thumb_nail": '/media/' + str(todo.thumb_nail),
                "pup_date": todo.pup_date,
            }

            todo_all_json.append(todo_json)

        return JsonResponse({
        "status": 200,
        "success" : True,
        "message": "todo 생성 성공",
        "data": todo_all_json
        })

    return JsonResponse({
        "status": 405,
        "success" : False,
        "message": "method error",
        "data": None
    })
    

    


import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import *

# Create your views here.
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
from django.shortcuts import render,get_object_or_404
from django.http.response import JsonResponse
from .models import *
import json

# Create your views here.
def create_profile(requests):

    if requests.method == "POST":

        body = json.loads(requests.body.decode('utf-8'))

        new_profile = Profile.objects.create(
            name = body['name'],
            age = body['age'],
            phone = body['phone']
        )

        new_profile_json = {
            "id": new_profile.id,
            "name": new_profile.name,
            "age": new_profile.age,
            "phone": new_profile.phone,
        }

        return JsonResponse({
            "status": 200,
            "success": True,
            "message": "생성 성공",
            "data": new_profile_json
        })

    return JsonResponse({
        "status": 405,
        "success" : False,
        "message": "method error",
        "data": None
    })

def get_profile_all(requests):

    if requests.method == "GET":
        
        create_all = Profile.objects.all()

        profile_json_all = []

        for profile in create_all:
            profile_json = {
                "id": profile.id,
                "name": profile.name,
                "age": profile.age,
                "phone": profile.phone,
            }

            profile_json_all.append(profile_json)

        return JsonResponse({
            "status": 200,
            "success": True,
            "message": "출력 완료",
            "data": profile_json_all
        })

    return JsonResponse({
        "status": 405,
        "success" : False,
        "message": "method error",
        "data": None
    })

def get_profile_one(request, id):
    if request.method == "GET":

        profile = get_object_or_404(Profile, pk = id)

        profile_json = {
            "id": profile.id,
            "name": profile.name,
            "age": profile.age,
            "phone": profile.phone,
        }

        return JsonResponse({
            "status": 200,
            "success": True,
            "message": "출력성공",
            "data": profile_json
        })

    return JsonResponse({
        "status": 405,
        "success" : False,
        "message": "method error",
        "data": None
    })

def update_profile(request, id):
    if request.method == "PATCH":

        body = json.loads(request.body.decode('utf-8'))

        update_profile = get_object_or_404(Profile, pk = id)

        update_profile.name = body['name']
        update_profile.age = body['age']
        update_profile.phone = body['phone']

        update_profile.save()

        update_profile_json = {
            "id": update_profile.id,
            "name": update_profile.name,
            "age": update_profile.age,
            "phone": update_profile.phone,
        }

        return JsonResponse({
            'status': 200,
            'success': True,
            'message': '업데이트 성공!',
            'data': update_profile_json
        })
    
    return JsonResponse({
                'status': 405,
                'success': False,
                'message': 'method error',
                'data': None
            })

def delete_profile(request, id):
    if request.method == 'DELETE':

        delete_profile = get_object_or_404(Profile, pk = id)

        delete_profile.delete()

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
        
def create_url(request, profile_id):
    if request.method == "POST":

        body = request.POST

        new_url = Url.objects.create(
            profile = get_object_or_404(Profile, pk = profile_id),
            title = body['title'],
            link = body['link']
        )

        new_url_json = {
            "id": new_url.id,
            "title": new_url.title,
            "link": new_url.link,
        }

        return JsonResponse({
            "status": 200,
            "success" : True,
            "message": "url 생성 성공",
            "data": new_url_json
        })

    return JsonResponse({
        "status": 405,
        "success" : False,
        "message": "method error",
        "data": None
    })

def get_url(requests):

    if requests.method == "GET":
        
        url_all = Url.objects.all()

        url_all_json = []

        for url in url_all:
            url_json = {
                "id": url.id,
                "title": url.title,
                "link": url.link,
            }

            url_all_json.append(url_json)

        return JsonResponse({
            "status": 200,
            "success" : True,
            "message": "url 보기 성공",
            "data": url_all_json
        })

    return JsonResponse({
        "status": 405,
        "success" : False,
        "message": "method error",
        "data": None
    })
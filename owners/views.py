import email
import json
from unittest import result

from django.http import JsonResponse
from django.views import View

from owners.models import Owner, Dog

class OwnerView(View):
    def post(self, request):
        data = json.loads(request.body)
        Owner.objects.create(name =data['name'],
                             email=data['email'],
                             age  =data['age'])

        return JsonResponse({'message':'created'}, status=200)

    def get(self, request):
        owners = Owner.objects.all()
        results = []

        for owner in owners:
            results.append(
                {
                    'name'  : owner.name,
                    'email' : owner.email,
                    'age'   : owner.age 
                }
            )
        return JsonResponse({'result':results}, status=200)

class DogView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.get(name=data['owner'])
        Dog.objects.create(name =data['name'],
                           age  =data['age'],
                           owner=owner)

        return JsonResponse({'message':'created'}, status=200)

    def get(self, request):
        dogs = Dog.objects.all()
        results = []

        for dog in dogs:
            results.append(
                {
                    'name'  : dog.name,
                    'age'   : dog.age,
                    'owner' : dog.owner.name
                }
            )
        return JsonResponse({'result':results}, status=200)

class OwnerDogView(View):
    def get(self, request):
        owners  = Owner.objects.all()
        dogs    = Dog.objects.all()
        results = []
        for owner in owners:
            for dog in dogs:
                if owner.id == dog.owner.id: 
                    results.append(
                        {
                            'name'    : owner.name,
                            'email'   : owner.email,
                            'age'     : owner.age,
                            'dogname' : dog.name,
                            'dogage'  : dog.age,            
                        }
                    )
    
        return JsonResponse({'result':results}, status=200)

from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
def INDEX(request):
    return render(request, 'index.html')


def Student(request, id):
    return JsonResponse({'Hello': id})

def random(request, slug):
    return JsonResponse({'hello' : slug})



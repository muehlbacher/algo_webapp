import random
import json
from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    # Generate random coordinates
    points = [{'x': random.randint(0, 800), 'y': random.randint(0, 600), 'size': 10} for _ in range(5)]
    points_json = json.dumps(points)

    return render(request, 'algorithm_app/index.html', {'points': points_json})


def get_new_coordinates(request):
    points_json = [{'x': random.randint(0, 800), 'y': random.randint(0, 600), 'size': 10} for _ in range(5)]
    return JsonResponse({'points': points_json})
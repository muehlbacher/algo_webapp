import random
import json
from django.shortcuts import render
from django.http import JsonResponse
from .algorithms.particle import ParticleAlgo
from django.contrib.sessions.models import Session

# Initialize the particle algorithm
def get_particle_algo(request):
    if 'particle' not in request.session:
        print("New Particle")
        particle = None
        particle = ParticleAlgo(30, width=800, height=600)
        particle.create_particles()
        request.session['particle'] = particle.to_json()

    print("Before first request...")
    return request.session['particle']

def index(request):
    Session.objects.all().delete()

    particle = None
    #request.session['particle'] = None  
    # Generate random coordinates
    print("First index call")
    particle = get_particle_algo(request)

    particle = ParticleAlgo.from_json(particle)

    print(particle)
    #particle = ParticleAlgo.from_json(particle)
    #particle.create_particles()
    points = []
    for particle in particle.particles:
        points.append({'x': particle.x, 'y': particle.y, 'size': 10})
    #points = [{'x': random.randint(0, 800), 'y': random.randint(0, 600), 'size': 10} for _ in range(5)]
    points_json = json.dumps(points)
    print("Before render...")
    print(request.session['particle'])
    return render(request, 'algorithm_app/index.html', {'points': points_json})


def get_new_coordinates(request):
    print("Get new Coordinates...")
    particle = get_particle_algo(request)
    particle = ParticleAlgo.from_json(particle)
    print(particle.particles)
    particle.update()
    points = []
    for part in particle.particles:
        points.append({'x': part.x, 'y': part.y, 'size': 10})
    request.session['particle'] = particle.to_json()
    #points_json = [{'x': random.randint(0, 800), 'y': random.randint(0, 600), 'size': 10} for _ in range(5)]
    return JsonResponse({'points': points})
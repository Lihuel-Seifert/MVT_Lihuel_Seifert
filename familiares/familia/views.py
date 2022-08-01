from django.shortcuts import render
from django.http import HttpResponse
from familia.models import Familias
from django.template import Template, Context, loader
from datetime import datetime #importe el datetime

# Create your views here.

def index(request):

    

    familiares = Familias.objects.all()

    familiares = {'familiares':familiares, 'datetame': datetime.now()} # Agrego al datetime  al dicionario

    plantilla = loader.get_template("index.html")

    documento = plantilla.render(familiares)

    return HttpResponse(documento)

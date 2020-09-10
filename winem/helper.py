import random
import string
from django.http import HttpResponse
import json
def generate_str(x=30):
    str =""
    for i in range(x):
        str += string.ascii_letters[random.randint(0,len(string.ascii_letters)-1)]
    return str
def status(leviation):
    return HttpResponse(json.dumps(leviation),content_type = "json")
def nstatus(**kwargs):
    return HttpResponse(json.dumps(kwargs),content_type = "json")

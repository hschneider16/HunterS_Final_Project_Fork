import csv
from django.shortcuts import render

def menu(request):
    with open('menu.csv', 'r') as file:
        csv_data = csv.reader(file)
        data = list(csv_data)
    
    return render(request, 'menu.html', {'data': data})

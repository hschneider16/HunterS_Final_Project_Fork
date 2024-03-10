import csv
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def menu(request):
    with open('menu.csv', 'r') as file:
        csv_data = csv.reader(file)
        data = list(csv_data)
    
    return render(request, 'menu.html', {'data': data})

@csrf_exempt
def checkout_submit(request):
    if request.method == 'POST':
        first_name = request.POST.get('myFName')
        last_name = request.POST.get('myLName')
        credit_card = request.POST.get('myCreditCard')

        # txt file output
        with open('checkout_data.txt', 'a') as file:
            file.write(f"Name: {first_name} {last_name}\n")
            file.write(f"Credit Card: {credit_card}\n")
            file.write('\n')

        return render(request, 'checkout_success.html')
    else:
        return render(request, 'checkout.html')

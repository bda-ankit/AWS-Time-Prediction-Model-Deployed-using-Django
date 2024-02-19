from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request, 'home.html')

def result(request):
    cls = joblib.load('linear_regression_model.joblib')
    listdata = []
    try:
        intInput = int(request.GET['predictValue'])
    except:
        intInput = int(request.POST['predictValue'])
    listdata.append(intInput)
    # print(listdata)
    predictionAns = cls.predict([listdata])
    return render(request, 'result.html', {'predictedValue' : round(predictionAns[0], 3), 'userInput': listdata[0]})

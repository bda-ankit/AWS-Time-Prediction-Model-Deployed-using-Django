from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request, 'index.html')

def result(request):
    cls = joblib.load('GBModel.h5')
    listdata = []

    fileCount = int(request.POST['fileCount'])
    allFileSize = float(request.POST['allFileSize'])
    listdata.append(fileCount)
    listdata.append(allFileSize)
    # print(listdata)
    predictionAns = cls.predict([listdata])
    return render(request, 'result.html', {'predictedValue' : round((predictionAns[0]*60), 3), 'userInput': listdata[0], 'predictedValueMinutes': round(predictionAns[0], 2)})

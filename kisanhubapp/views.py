import json
import urllib2

from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from kisanhubapp.models import Regions, DataType, DataDownloadLinks,Data



def index(request):
    return render(request, 'index01.html', {})


def data(request):
    regions = Regions.objects.filter(is_deleted=False)
    dataType = DataType.objects.filter(is_deleted=False)
    return render(request, 'data.html', {'regions': regions, 'dataType': dataType})


def download(request):
    try:
        print request.GET
        dataDownloadLinks=DataDownloadLinks.objects.get(region=request.GET.get('region'),datatype=request.GET.get('datatype'))
        print dataDownloadLinks.link
        try:
            Data.objects.filter(datadownload=dataDownloadLinks).delete()
        except Exception,e:
            pass
        req = urllib2.Request(dataDownloadLinks.link, headers={'User-Agent': "Magic Browser"})
        con = urllib2.urlopen(req)
        data = con.read()

        lines=data.split('\n')[8:]
        for line in lines[:5]:
            templist = []
            datapoints=line.split(' ')
            for datapoint in datapoints:
                if datapoint.strip():
                    templist.append(datapoint.strip())

            if len(templist)==18:
                Data(
                    datadownload=dataDownloadLinks,
                    year=templist[0],
                    jan=templist[1],
                    feb=templist[2],
                    mar=templist[3],
                    apr=templist[4],
                    may=templist[5],
                    jun=templist[6],
                    jul=templist[7],
                    aug=templist[8],
                    sep=templist[9],
                    oct=templist[10],
                    nov=templist[11],
                    dec=templist[12],
                    win=templist[13],
                    spr=templist[14],
                    sum=templist[15],
                    aut=templist[16],
                    ann=templist[17],
                ).save()
        data = {'success':'true','message':'data downloaded successfully'}
    except Exception,e:
        print 'Exception|download|view.py',e
        data = {'success': 'true','message':'servier error'}
    return HttpResponse(json.dumps(data), content_type='application/json')


def get_region_datalist(request):
    try:
        start = request.GET.get('start')
        length = int(request.GET.get('length')) + int(request.GET.get('start'))

        try:
            dataDownloadLinks = DataDownloadLinks.objects.get(region=request.GET.get('region'),
                                                          datatype=request.GET.get('datatype'))
        except Exception:
            dataList=[]
            data = {'iTotalRecords': 0, 'iTotalDisplayRecords': len(dataList), 'aaData': dataList}
            return HttpResponse(json.dumps(data), content_type='application/json')


        dataListQR=Data.objects.filter(datadownload=dataDownloadLinks)[start:length]

        print 'dataListQR',dataListQR
        total_record = Data.objects.filter(datadownload=dataDownloadLinks).count()
        dataList=[]
        for data in dataListQR:
            tempList = []
            tempList.append(data.year)
            tempList.append(data.jan)
            tempList.append(data.feb)
            tempList.append(data.mar)
            tempList.append(data.apr)
            tempList.append(data.may)
            tempList.append(data.jun)
            tempList.append(data.jul)
            tempList.append(data.aug)
            tempList.append(data.sep)
            tempList.append(data.oct)
            tempList.append(data.nov)
            tempList.append(data.dec)
            tempList.append(data.win)
            tempList.append(data.spr)
            tempList.append(data.sum)
            tempList.append(data.aut)
            tempList.append(data.ann)
            dataList.append(tempList)
        data = {'iTotalRecords': total_record, 'iTotalDisplayRecords': len(dataList), 'aaData': dataList}
        print 'data', data
        return HttpResponse(json.dumps(data), content_type='application/json')
    except Exception,e:
        print 'Exception|getlist|view.py', e

def LineChart(request):
    try:

        dataDownloadLinks = DataDownloadLinks.objects.filter(region=request.GET.get('region'))

        maxTemp = dataDownloadLinks.objects.filter(datatype=DataType.objects.get(datatype='Max temp')).first()
        minTemp = dataDownloadLinks.objects.filter(datatype=DataType.objects.get(datatype='Min temp')).first()
        #meanTemp = dataDownloadLinks.objects.filter(datatype=DataType.objects.get(datatype='Mean temp')).first()

        mamTempData = Data.objects.filter(datadownload=maxTemp).aggregate(Sum('jan'),Sum('feb'),Sum('mar'),Sum('apr'),Sum('may'),Sum('jun'),Sum('jul'),Sum('aug'),Sum('sep'),Sum('oct'),Sum('nov'),Sum('dec'))
        #for mean in mamTempData:



    except Exception,e:
        print 'Exception|getlist|view.py', e

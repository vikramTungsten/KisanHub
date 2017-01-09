import urllib2

from django.shortcuts import render

# Create your views here.
from kisanhubapp.models import Regions, DataType, DataDownloadLinks,Data

dict = {
    'UK-Max': 'http://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/date/UK.txt',
    'UK-Min': 'http://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmin/date/UK.txt',
    'UK-Mean': 'http://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmean/date/UK.txt',
    'UK-Sunshine': 'http://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Sunshine/date/UK.txt',
    'UK-Rainfall': 'http://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Rainfall/date/UK.txt',
    'England-Max': 'http://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/date/England.txt',
    'England-Min': 'http://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmin/date/England.txt',
    'England-Mean': 'http://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmean/date/England.txt',
    'England-Sunshine': 'http://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Sunshine/date/England.txt',
    'England-Rainfall': 'http://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Rainfall/date/England.txt',
    'Wales-Max': 'http://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/date/Wales.txt',
    'Wales-Min': 'http://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmin/date/Wales.txt',
    'Wales-Mean': 'http://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmean/date/Wales.txt',
    'Wales-Sunshine': 'http://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Sunshine/date/Wales.txt',
    'Wales-Rainfall': 'http://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Rainfall/date/Wales.txt',
    'Scotland-Max': 'http://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/date/Scotland.txt',
    'Scotland-Min': 'http://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmin/date/Scotland.txt',
    'Scotland-Mean': 'http://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmean/date/Scotland.txt',
    'Scotland-Sunshine': 'http://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Sunshine/date/Scotland.txt',
    'Scotland-Rainfall': 'http://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Rainfall/date/Scotland.txt'
}


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

        lines=data.split('\n')[7:]
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

    except Exception,e:
        print 'Exception|download|e',e
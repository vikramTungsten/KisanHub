import json
import pdb
import urllib2

from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from kisanhubapp.models import Regions, DataType, DataDownloadLinks, Data


def session_comparison(request):
    try:
        regions = Regions.objects.filter()

        uk = regions.filter(region='UK').first()
        england = regions.filter(region='England').first()
        wales = regions.filter(region='Wales').first()
        scotland = regions.filter(region='Scotland').first()

        ukDownloadLinks = DataDownloadLinks.objects.filter(region=uk,
                                                           datatype=DataType.objects.get(datatype='Mean temp')).first()
        englandDownloadLinks = DataDownloadLinks.objects.filter(region=england,
                                                                datatype=DataType.objects.get(
                                                                    datatype='Mean temp')).first()
        walesDownloadLinks = DataDownloadLinks.objects.filter(region=wales,
                                                              datatype=DataType.objects.get(
                                                                  datatype='Mean temp')).first()
        scotlandDownloadLinks = DataDownloadLinks.objects.filter(region=scotland,
                                                                 datatype=DataType.objects.get(
                                                                     datatype='Mean temp')).first()
        ukSessionData = getRainFall(ukDownloadLinks)
        englandSessionData = getRainFall(englandDownloadLinks)
        walesSessionData = getRainFall(walesDownloadLinks)
        scotlandSessionData = getRainFall(scotlandDownloadLinks)

        winter={'uk':ukSessionData[0],'england':englandSessionData[0],'wales':walesSessionData[0],'scotland':scotlandSessionData[0]}
        summer={'uk':ukSessionData[2],'england':englandSessionData[2],'wales':walesSessionData[2],'scotland':scotlandSessionData[2]}

        temp,i=0,0
        coolest_place=""
        for k,v in winter.items():
            if v:
                if i==0:
                    temp=v
                    coolest_place=k
                    i=i+1
                elif temp > v:
                    temp=v
                    coolest_place=k

        temp,i=0,0
        coolest_place=""
        for k,v in winter.items():
            if v:
                if i==0:
                    temp=v
                    coolest_place=k
                    i=i+1
                elif temp > v:
                    temp=v
                    coolest_place=k








        data = {'success': 'true', 'ukSessionData': ukSessionData, 'englandSessionData': englandSessionData,
                'walesSessionData': walesSessionData, "scotlandSessionData": scotlandSessionData}

        print 'data',data

        return HttpResponse(json.dumps(data), content_type='application/json')

        print 'maxTempList', maxTempList
    except Exception, e:
        print 'Exception|session comparison|Dashboard.py', e


def getRainFall(dataLink):
    try:
        year = 'All'
        sessions = ['win', 'spr', 'sum', 'aut']
        if year == 'All':
            sessionData = Data.objects.filter(datadownload=dataLink).aggregate(win=Sum('win'), spr=Sum('spr'),
                                                                               sum=Sum('sum'), aut=Sum('aut'))
        else:
            sessionData = Data.objects.filter(datadownload=dataLink, year=year).aggregate(win=Sum('win'),
                                                                                          spr=Sum('spr'),
                                                                                          sum=Sum('sum'),
                                                                                          aut=Sum('aut'))

        sessionList = [sessionData[session] for session in sessions]
        return sessionList
    except Exception, e:
        print 'Exception|getRainFall|Dashboard.py', e

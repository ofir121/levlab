from django.http import JsonResponse
from django.shortcuts import render
from dataVisualizer.models import AluHyper
from dataVisualizer.tables import SamplesTable
from django_tables2 import RequestConfig
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import View


def index(request):
    return render(request, 'dataVisualizer/index.html')


def table(request):
    table = SamplesTable(AluHyper.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'dataVisualizer/tableView.html', {'table': table})


def about(request):
    return render(request, 'dataVisualizer/about.html')


def get_data(request):
    data = serializers.serialize("json", AluHyper.objects.all())
    return JsonResponse(data, safe=False)


class HomeView(View):

    def get(self, request):
        return render(request, 'dataVisualizer/charts.html', {'table': table})


class ChartsData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = serializers.serialize("json", AluHyper.objects.all())
        return Response(data)

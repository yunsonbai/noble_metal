# coding=utf-8
from rest_framework.views import APIView
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from noble_metal.utils import data_draw


class GoldPrice(APIView):

    @csrf_exempt
    def get(self, request):
        return render(request, 'goldprice.html')

    @csrf_exempt
    def post(self, request):
        start_time = request.data.get('start_time')
        end_time = request.data.get('end_time')
        if not start_time or not end_time:
            return render(request, 'goldprice.html')
        picture_t = data_draw.get_picture(start_time, end_time)
        picture_p = data_draw.get_picture(
            start_time, end_time, ptype='price')
        data = {
            'start_time': start_time,
            'end_time': '{0}'.format(end_time),
            'picture_t': picture_t,
            'picture_p': picture_p
        }
        return render(request, 'goldprice.html', data)

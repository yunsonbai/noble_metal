# coding=utf-8
import base64
from rest_framework.views import APIView
from django.shortcuts import render
from yuntool.chart import plot
from noble_metal.models import GoldPrice as ModelGoldPrice
from noble_metal.enum import PriceType


class GoldPrice(APIView):

    def get(self, request):
        return render(request, 'goldprice.html')

    def post(self, request):
        start_time = request.data.get('start_time')
        end_time = request.data.get('end_time')
        if not start_time or not end_time:
            return render(request, 'goldprice.html')
        high_sdata = ModelGoldPrice.objects.filter(
            dtype=PriceType.high).filter(
            date__gte=start_time, date__lte=end_time).order_by(
            'date').values_list('date', 'time')
        low_sdata = ModelGoldPrice.objects.filter(
            dtype=PriceType.low).filter(
            date__gte=start_time, date__lte=end_time).order_by(
            'date').values_list('date', 'time')
        high_data = [
            [str(d[0]) for d in high_sdata],
            [str(d[1]) for d in high_sdata]]
        low_data = [
            [str(d[0]) for d in low_sdata],
            [str(d[1]) for d in low_sdata]]

        lx = [i for i in range(len(low_sdata))]
        hx = [i for i in range(len(high_sdata))]
        y = [
            [float(d[0:-3].replace(':', '.')) for d in high_data[1]],
            [float(d[0:-3].replace(':', '.')) for d in low_data[1]]]
        picture = plot.draw_curve(
            [hx, lx], [y[0], y[1]],
            xlabel=['date', 'date'],
            ylabel=['time', 'time'],
            title=['high_price_time', 'low_price_time'],
            xticklabels=[high_data[0], low_data[0]],
            yticklabels=[high_data[1], low_data[1]])

        data = {
            'start_time': start_time,
            'end_time': end_time,
            'picture': base64.b64encode(picture.read())
        }
        picture.close
        return render(request, 'goldprice.html', data)

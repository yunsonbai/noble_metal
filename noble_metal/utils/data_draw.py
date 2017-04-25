# coding=utf-8
import base64
from yuntool.chart import plot
from noble_metal.models import GoldPrice as ModelGoldPrice
from noble_metal.enum import PriceType
from django.conf import settings

DPI = 100


def _price_time(start_time, end_time):
    high_sdata = ModelGoldPrice.objects.filter(
        dtype=PriceType.high).filter(
        date__gte=start_time, date__lte=end_time).order_by(
        'date').values_list('date', 'time', 'situation')
    low_sdata = ModelGoldPrice.objects.filter(
        dtype=PriceType.low).filter(
        date__gte=start_time, date__lte=end_time).order_by(
        'date').values_list('date', 'time', 'situation')
    high_data = [
        [str(d[0]) for d in high_sdata],
        [str(d[1]) for d in high_sdata]]
    low_data = [
        [str(d[0]) for d in low_sdata],
        [str(d[1]) for d in low_sdata]]
    situation_dict = dict(settings.SITUATION)
    text = [
        [situation_dict[d[2]] for d in high_sdata],
        [situation_dict[d[2]] for d in low_sdata]]

    lx = [i for i in range(len(low_sdata))]
    hx = [i for i in range(len(high_sdata))]

    y = [
        [float(d[0:-3].replace(':', '.')) for d in high_data[1]],
        [float(d[0:-3].replace(':', '.')) for d in low_data[1]]]
    picture = plot.draw_curve(
        [hx, lx], [y[0], y[1]],
        xlabel=['date', 'date'],
        ylabel=['time', 'time'],
        xticks=[high_data[0], low_data[0]],
        stretch=8,
        title=['high_price_time', 'low_price_time'],
        draw_one=True, label=['high', 'low'],
        dpi=DPI, text=text, fontproperties=settings.FONT_DIR)
    picture_base64 = base64.b64encode(picture.read())
    picture.close()
    return picture_base64


def _price_price(start_time, end_time):
    high_sdata = ModelGoldPrice.objects.filter(
        dtype=PriceType.high).filter(
        date__gte=start_time, date__lte=end_time).order_by(
        'date').values_list('date', 'price')
    low_sdata = ModelGoldPrice.objects.filter(
        dtype=PriceType.low).filter(
        date__gte=start_time, date__lte=end_time).order_by(
        'date').values_list('date', 'price')
    high_data = [
        [str(d[0]) for d in high_sdata],
        [str(d[1]) for d in high_sdata]]
    low_data = [
        [str(d[0]) for d in low_sdata],
        [str(d[1]) for d in low_sdata]]

    lx = [i for i in range(len(low_sdata))]
    hx = [i for i in range(len(high_sdata))]

    y = [
        [float(d) for d in high_data[1]],
        [float(d) for d in low_data[1]]]
    picture = plot.draw_curve(
        [hx, lx], [y[0], y[1]],
        xlabel=['date', 'date'],
        ylabel=['price', 'price'],
        xticks=[high_data[0], low_data[0]],
        stretch=8,
        title=['high_price', 'low_price'],
        draw_one=True, label=['high', 'low'],
        dpi=DPI)
    picture_base64 = base64.b64encode(picture.read())
    picture.close()
    return picture_base64


def get_picture(start_time, end_time, ptype='time'):
    if ptype == 'time':
        return _price_time(start_time, end_time)
    elif ptype == 'price':
        return _price_price(start_time, end_time)
    return base64.b64encode('')

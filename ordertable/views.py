from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, View
from ordertable.models import Order, Table
from django.core.mail import send_mail


class IndexView(View):
    template_name = 'ordertable/index.html'

    def post(self, request):
        p = request.POST
        o = Order.objects.create(date=p.get('curdate'),
                                 name=p.get('name'),
                                 email=p.get('email')
                                 )
        for tt in p.get('table').split(','):
            o.table.add(Table.objects.get(pk=tt))
        o.save()
        # send_mail('Order table',
        #           'You ordered a table number ' + table + ' in our restaurant on ' + p.get(
        #               'curdate') + '. Have a nice evening!',
        #           'from@example.com', [p.get('email')], fail_silently=False)
        # email worked!
        curdate = datetime.now().strftime("%Y-%m-%d")
        table_list = Table.objects.all()
        curdate_order_list = Order.objects.filter(active=True).filter(date=curdate)
        av_table_list = Table.objects.exclude(order__in=curdate_order_list)
        context = {'table_list': table_list, 'av_table_list': av_table_list, 'curdate': curdate}
        return render(request, self.template_name, context)
        # return HttpResponse(request)

    def get(self, request):
        curdate = request.GET.get('date') if request.GET.get('date') else datetime.now().strftime("%Y-%m-%d")
        table_list = Table.objects.all()
        curdate_order_list = Order.objects.filter(active=True).filter(date=curdate)
        av_table_list = Table.objects.exclude(order__in=curdate_order_list)
        context = {'table_list': table_list, 'av_table_list': av_table_list, 'curdate': curdate}
        return render(request, self.template_name, context)

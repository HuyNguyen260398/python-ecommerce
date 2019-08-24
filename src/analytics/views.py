import datetime
import random

from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Sum, Avg
from django.utils import timezone

from orders.models import Order


class SalesAjaxView(View):
    def get(self, request, *args, **kwargs):
        data = {}
        if request.user.is_staff:
            qs = Order.objects.all().by_weeks_range(weeks_ago=5, number_of_weeks=5)
            if request.GET.get('type') == 'week':
                days = 7
                start_date = timezone.now().today() - datetime.timedelta(days=days-1)
                # date_list = [start_date + datime.timedelta(days=x) for x in range(0, days)] # another way
                datime_list = []
                labels = []
                salesItems = []
                for x in range(0, days):
                    new_time = start_date + datetime.timedelta(days=x)
                    datime_list.append(new_time)
                    labels.append(new_time.strftime("%a"))
                    new_qs = qs.filter(updated__day=new_time.day, updated__month=new_time.month)
                    day_total = new_qs.order_totals_data()['total__sum'] or 0
                    salesItems.append(day_total)
                data['labels'] = labels
                data['data'] = salesItems

            if request.GET.get('type') == '4weeks':
                current = 5
                salesItems = []
                for i in range(0, 5):
                    new_qs = qs.by_weeks_range(weeks_ago=current, number_of_weeks=1)
                    sales_total = new_qs.order_totals_data()['total__sum'] or 0
                    salesItems.append(sales_total)
                    current -= 1
                data['labels'] = ['Four Weeks Ago', 'Three Weeks Ago',
                                  'Two Weeks Ago', 'Last Week', 'This Week']
                data['data'] = salesItems
        return JsonResponse(data)


class SalesView(LoginRequiredMixin, TemplateView):
    template_name = 'analytics/sales.html'

    def dispatch(self, *args, **kwargs):
        user = self.request.user
        if not user.is_staff:
            return render(self.request, "400.html", {})
        return super(SalesView, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(SalesView, self).get_context_data(*args, **kwargs)
        qs = Order.objects.all().by_weeks_range(weeks_ago=10, number_of_weeks=10)
        # start_date = timezone.now().date() - datetime.timedelta(hours=24)
        # end_date = timezone.now().date() + datetime.timedelta(hours=12)
        # context['today'] = qs.by_range(
        #     start_date=start_date, end_date=end_date).get_sales_breakdown()
        context['today'] = qs.by_range(
            start_date=timezone.now().date()).get_sales_breakdown()
        context['this_week'] = qs.by_weeks_range(
            weeks_ago=1, number_of_weeks=1).get_sales_breakdown()
        context['last_four_weeks'] = qs.by_weeks_range(
            weeks_ago=5, number_of_weeks=5).get_sales_breakdown()

        print(context['last_four_weeks']['recent_order_data'])

        return context

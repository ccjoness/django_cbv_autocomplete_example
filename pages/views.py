from django.shortcuts import render
from pages.models import ProgrammingLanguage, Senator
from django.core import serializers
from django.views import generic
from django.utils import timezone
from django import http
from django.db.models import Q


# class AJAXListMixin(object):
#     def dispatch(self, request, *args, **kwargs):
#         if not request.is_ajax():
#             raise http.Http404("This is an ajax view, friend.")
#         return super(AJAXListMixin, self).dispatch(request, *args, **kwargs)
#
#     def get_queryset(self):
#         return (
#             super(AJAXListMixin, self)
#                 .get_queryset()
#                 .filter(name__contains=self.request.GET.get('name'))
#         )
#
#     def get(self, request, *args, **kwargs):
#         return http.HttpResponse(serializers.serialize('json', self.get_queryset()))


# class AjaxDestinationListView(AJAXListMixin, generic.ListView):
#     model = ProgrammingLanguage

class AjaxDestinationListView(generic.ListView):
    model = ProgrammingLanguage

    def dispatch(self, request, *args, **kwargs):
        if not request.is_ajax():
            raise http.Http404("This is an ajax view, friend.")
        return super(AjaxDestinationListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return (
            super(AjaxDestinationListView, self)
                .get_queryset()
                .filter(name__contains=self.request.GET.get('name'))
        )

    def get(self, request, *args, **kwargs):
        return http.HttpResponse(serializers.serialize('json', self.get_queryset()))


class SenatorNameAcView(generic.ListView):
    model = Senator

    def dispatch(self, request, *args, **kwargs):
        if not request.is_ajax():
            raise http.Http404("This is an ajax view, friend.")
        return super(SenatorNameAcView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        search = self.request.GET.get('name').split()
        if len(search) > 1:
            return (
                super(SenatorNameAcView, self)
                    .get_queryset()
                    .filter(
                    Q(first_name__contains=search[0]) | Q(last_name__contains=search[0]) |
                    Q(first_name__contains=search[1]) | Q(last_name__contains=search[1])
                )
            )
        return (
            super(SenatorNameAcView, self)
                .get_queryset()
                .filter(Q(first_name__contains=search[0]) | Q(last_name__contains=search[0]))
        )

    def get(self, request, *args, **kwargs):
        return http.HttpResponse(serializers.serialize('json', self.get_queryset()))


def home(request):
    return render(request, 'home.html')
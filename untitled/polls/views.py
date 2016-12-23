from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import View
from polls.models import TransactionModel
from django.views.generic import TemplateView
from polls.models import *


# Create your views here.
class AboutView(TemplateView):
    template_name = "about.html"

class TransactionListView(ListView):
    def get(self, request):
        transactions = TransactionModel.objects.all ()
        return render (request, 'transactions.html', {'transactions': transactions})
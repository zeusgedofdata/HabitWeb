from django.shortcuts import render
from django.http import HttpResponse
from .models import Activity, FitActivity, Category, MetaCategory
from .habit_visualization import weekly_report


# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to the meeting planner!")


def dashboard(request):
    return render(request, "dashboard/tracker.html",
                  {"activities": Activity.objects.all(), 'plot_div': weekly_report()})

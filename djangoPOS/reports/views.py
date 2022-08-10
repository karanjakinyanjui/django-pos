from django.shortcuts import render

# Create your views here.


def all_reports(request):
    return render(request, 'reports/reports.html')


def favourites(request):
    return render(request, 'reports/favourites.html')

def summary_appointments(request):
    return render(request, 'reports/summary_appointments.html')


def detailed_reports(request):
    return render(request, 'reports/detailed_reports.html')


def graphical_summary(request):
    return render(request, 'reports/graphical_summary_categories.html')


def summary_categories(request):
    return render(request, 'reports/summary_categories.html')


def generate_closeout(request):
    return render(request, 'reports/generate_closeout.html')


def closeout_condensed(request):
    return render(request, 'reports/closeout_condensed.html')


def detailed_search_reports(request):
    return render(request, 'reports/detailed_search_reports.html')


def detailed_commissions(request):
    return render(request, 'reports/detailed_commissions.html')


def graphical_summary_commissions(request):
    return render(request, 'reports/graphical_summary_commissions.html')


def summary_commissions(request):
    return render(request, 'reports/summary_commissions.html')










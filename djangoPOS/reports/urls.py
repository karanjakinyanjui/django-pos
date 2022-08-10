from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# app_name = 'reports'
urlpatterns = [
     path('', views.all_reports, name="reports"),
     path('summary/appointments', views.summary_appointments, name="summary_reports"),
     path('favourites/', views.favourites, name="favourites"),
     path('detailed/reports', views.detailed_reports, name="detailed reports"),
     path('graphical/summary/categories',views.graphical_summary, name="graphical summary"),
     path('summary/categories', views.summary_categories, name="summary categories"),
     path('closeout/condensed', views.closeout_condensed, name="closeout_condensed"),
     path('generate/closeout', views.generate_closeout, name="closeout"),
     path('detailed/search_reports', views.detailed_search_reports,name="detailed search reports"),
     path('detailed/commissions', views.detailed_commissions,name="detailed commissions"),
     path('graphical/summary/commissions', views.graphical_summary_commissions,name="graphical summary commissions"),
     path('summary/commissions', views.summary_commissions,name="summary commissions"),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

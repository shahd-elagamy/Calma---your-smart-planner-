from django.urls import path
from .views import planner_home, study_planner, ai_feedback_api,checkin_history,daily_checkin

urlpatterns = [
    path('', planner_home, name='home'),
    path('planner/', study_planner, name='study_planner'),
    path('checkin/', checkin_history, name='checkin_history'),
    path("checkin/", daily_checkin, name="checkin"),
    path("checkin/ai-feedback/", ai_feedback_api, name="ai_feedback_api"),


]

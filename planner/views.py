from django.shortcuts import render, redirect
from .models.mood_log import MoodLog

def daily_checkin(request):
    if request.method == 'POST':
        MoodLog.objects.create(
            user=request.user,
            mood=request.POST['mood'],
            energy=request.POST['energy'],
            note=request.POST.get('note', '')
        )
        return redirect('daily_checkin')

    return render(request, 'planner/daily_checkin.html')

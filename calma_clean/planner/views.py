from django.shortcuts import render,redirect

def planner_home(request):
    return render(request, 'planner/planner_home.html')

def study_planner(request):
    return render(request, 'planner/study_planner.html')

from django.shortcuts import render
from .models import DailyCheckin

def checkin_history(request):
    ai_feedback = None

    if request.method == 'POST':
        mood = int(request.POST.get('mood', 3))
        energy = int(request.POST.get('energy', 5))
        note = request.POST.get('note', '')

        DailyCheckin.objects.create(
            mood=mood,
            energy=energy,
            note=note
        )

        # AI Logic
        if mood <= 2 and energy <= 4:
            ai_feedback = "🌧️ It seems like today is heavy. Take it slow, even small steps matter."
        elif mood >= 4 and energy >= 7:
            ai_feedback = "🔥 You're full of positive energy today! This is a great time to focus and achieve."
        elif energy >= 7:
            ai_feedback = "⚡ You have good energy today. Try to channel it into one important task."
        else:
            ai_feedback = "🌿 You're doing okay. Stay balanced and be kind to yourself."

    last_entries = DailyCheckin.objects.order_by('-created_at')[:7]

    return render(request, 'planner/daily_checkin.html', {
        'last_entries': last_entries,
        'ai_feedback': ai_feedback
    })


# from django.http import JsonResponse
# from .utils import generate_ai_feedback

# def ai_feedback_api(request):
#     print(request.method, request.POST)
#     if request.method == "POST":
#         mood = int(request.POST.get("mood", 3))
#         energy = int(request.POST.get("energy", 5))
#         note = request.POST.get("note", "")
#         feedback = generate_ai_feedback(mood, energy, note)
#         return JsonResponse({"feedback": feedback})

#     return JsonResponse({"error": "Invalid request"}, status=400)


# import openai
# import os

# openai.api_key = os.getenv("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"
# )

# def daily_checkin(request):
#     ai_feedback = None
#     last_entries = DailyCheckin.objects.order_by('-created_at')[:7]

#     if request.method == "POST":
#         mood = int(request.POST.get("mood", 3))
#         energy = int(request.POST.get("energy", 5))
#         note = request.POST.get("note", "")

#         # حفظ البيانات
#         DailyCheckin.objects.create(mood=mood, energy=energy, note=note)

#         # إرسال البيانات لـ OpenAI API
#         prompt = f"User mood: {mood}, energy: {energy}, note: {note}. Give a short supportive and motivational feedback."

#         try:
#             response = openai.Completion.create(
#                 engine="text-davinci-003",
#                 prompt=prompt,
#                 max_tokens=60
#             )
#             ai_feedback = response.choices[0].text.strip()
#         except Exception as e:
#             ai_feedback = "🤖 AI service is unavailable now."

#         # لو AJAX
#         if request.is_ajax() or request.headers.get('x-requested-with') == 'XMLHttpRequest':
#             return JsonResponse({"feedback": ai_feedback})

#         return redirect('daily_checkin')

#     return render(request, "planner/daily_checkin.html", {
#         "last_entries": last_entries,
#         "ai_feedback": ai_feedback
#     })
from django.shortcuts import render
from django.http import JsonResponse
from .models import DailyCheckin
import openai
from django.conf import settings

# OpenAI key
openai.api_key = settings.OPENAI_API_KEY

def daily_checkin(request):
    last_entries = DailyCheckin.objects.order_by('-created_at')[:7]

    return render(request, "planner/daily_checkin.html", {
        "last_entries": last_entries
    })


def ai_feedback_api(request):
    if request.method == "POST":
        mood = request.POST.get("mood")
        energy = request.POST.get("energy")
        note = request.POST.get("note", "")

        # Save to DB
        DailyCheckin.objects.create(
            mood=int(mood),
            energy=int(energy),
            note=note
        )

        # OpenAI API call
        prompt = f"""
        User mood: {mood}, energy: {energy}, note: {note}.
        Write a short supportive and motivational message for this user.
        """

        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=60
            )
            ai_feedback = response.choices[0].text.strip()
        except Exception as e:
            ai_feedback = "🤖 Sorry, couldn't generate feedback. Try again."

        return JsonResponse({"feedback": ai_feedback})
    
    return JsonResponse({"error": "Invalid request"}, status=400)

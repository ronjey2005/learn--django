from django.shortcuts import render
from .models import Topic

def topicsListView(request):

    topics = Topic

    print(topics.objects.all())

    context = {
        "titles": topics.objects.all()
    }

    return render(request,'templates/learning_logs/topics.html', context)

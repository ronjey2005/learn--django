from django.shortcuts import render
from .models import Topic

def topicsListView(request):

    topics = Topic

    context = {
        "titles": topics.objects.all()
    }

    print(context)

    return render(request,'templates/learning_logs/topics.html', context)

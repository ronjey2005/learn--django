from django.shortcuts import render
from .models import Topic

def topicsListView(request):

    topics = Topic

    print(dir(topics.objects))

    context = {
        "dummy_context": "hello"
    }

    return render(request,'templates/learning_logs/topics.html', context)

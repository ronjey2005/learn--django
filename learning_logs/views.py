from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForm
from py_console import console, bgColor, textColor


def topicsListView(request):
    topics = Topic

    context = {
        "topics": topics.objects.all()
    }

    #print(context['topics'])

    return render(request, 'templates/learning_logs/topics.html', context)


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')

    console.warn("---")
    print(request)
    print(topic_id)
    console.warn("---")

    context = {
        "topic": topic,
        "entries": entries
    }

    return render(request, 'templates/learning_logs/topic.html', context)

def new_topic(request):
    """add a new topic"""

    form = TopicForm()

    context = {
        "": ''
    }

    return render(request, 'templates/learning_logs/new_topic.html', context)

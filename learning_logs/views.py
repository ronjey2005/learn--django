from django.shortcuts import render
from .models import Topic, Entry

def topicsListView(request):

    topics = Topic
    entries = Entry
    context = {
        "titles": [],
        "entries": []
    }

    for topic in topics.objects.all():
        context['titles'].append(topics.objects.get(id=topic.id))
        context['entries'].append(entries.objects.get(topic_id=topic.id))
        print(entries.objects(topic_id=topic.id))

    #print(context['entries'])



    return render(request,'templates/learning_logs/topics.html', context)

# def entryView(request):
#
#     entry = Entry
#
#     context = {
#
#     }

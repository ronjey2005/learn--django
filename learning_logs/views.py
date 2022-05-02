from django.shortcuts import render
from .models import Topic, Entry

def topicsListView(request):

    topics = Topic

    context = {
        "topics": topics.objects.all()
    }

    # for topic in topics.objects.all():
    #     e = topic.entry_set.all()
    #     print(e)

    print(context['topics'])

    return render(request, 'templates/learning_logs/topics.html', context)

# def entryView(request):
#
#     entry = Entry
#
#     context = {
#
#     }

from django.shortcuts import render


def topicsListView(request):

    context['some_data'] = 'This is just some data'
    return render(request,'templates/learning_logs/topics-list.html', context)

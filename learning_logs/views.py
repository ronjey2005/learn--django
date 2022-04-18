from django.shortcuts import render


def topicsListView(request):

    context = {
        "dummy_context": "hello"
    }

    return render(request,'templates/learning_logs/topics-list.html', context)

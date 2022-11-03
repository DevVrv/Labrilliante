from django.shortcuts import render

def page_not_found_view(request, exception):

    context = {
        'title': '404 Page not found'
    }

    return render(request, '404.html', context, status=404)

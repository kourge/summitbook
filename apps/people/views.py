import jingo


def index(request):
    return jingo.render(request, 'people/index.html', {
    })

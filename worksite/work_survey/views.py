# Create your views here.
from django.template import Context, loader
from work_survey.models import Poll
from django.http import HttpResponse

from django.http import HttpResponse

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    t = loader.get_template('work_survey/index.html')
    c = Context({
            'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(t.render(c))

def detail(request, poll_id):
    return HttpResponse("Hello, you're looking at poll %s" % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s" % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s" % poll_id)

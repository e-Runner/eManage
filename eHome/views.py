from django.shortcuts import render_to_response
from django.template import RequestContext


def eRunner(request):
    return render_to_response('eRunner1.html', context_instance = RequestContext(request))



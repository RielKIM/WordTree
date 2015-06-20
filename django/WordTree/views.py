from django.contrib.auth.decorators import login_required
from splunkdj.decorators.render import render_to

@render_to('WordTree:home.html')
@login_required
def home(request):
    return {
    	"app_name" : "WordTree"
    }
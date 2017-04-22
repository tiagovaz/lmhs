import re

def new_sort_url(request):
    new_url = re.sub("\&sort=.*", "", request.get_full_path())
    return { 'new_sort_url': new_url }

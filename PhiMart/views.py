from django.shortcuts import redirect



def api_root_view():
    return redirect('api-root')
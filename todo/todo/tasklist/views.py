from django.shortcuts import render


# Create your views here.



def index(request):
    return render(
        request,
        'tasklist/index.html',
        {
            #'var': param  
        }
        
        # ( {'Категории':Shop.objects.all() })
        
    )
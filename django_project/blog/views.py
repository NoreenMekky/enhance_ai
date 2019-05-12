from django.shortcuts import render
from .models import Post
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from uploads.core import super_resolve
from uploads.core import model


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        #super_resolve.predict('templates/core/14037.jpg')
        print("image name is :", filename)
        print("image path is in url:", uploaded_file_url)
        sr_image_url = 'media/sr_media/out_'+filename
        super_resolve.predict('media/'+filename, sr_image_url)

        for i in range (1,100):
            print(i)

        return render(request, 'blog/home.html', {
            'uploaded_file_url': uploaded_file_url,
            'super_resolved_file_url': sr_image_url
        })
    return render(request, 'blog/home.html', context)                                                                                                                                                                                                                                                                                  


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'blog/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'blog/simple_upload.html')

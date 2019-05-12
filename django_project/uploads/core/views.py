from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from uploads.core.models import Document
from uploads.core.forms import DocumentForm
from uploads.core import super_resolve
from uploads.core import model


def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        #super_resolve.predict('templates/core/14037.jpg')
        print("image name is :", filename)
        print("image path is in url:", uploaded_file_url)
        super_resolve.predict('media/'+filename, 'out_'+filename)

        for i in range (1,100):
            print(i)
        #super_resolve.predict(uploaded_file_url)

        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })

    return render(request, 'core/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })

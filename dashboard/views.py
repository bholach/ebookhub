from django.shortcuts import render
from .models import Category, Ebooks
from skycloud import settings
from django.http import HttpResponse, FileResponse
from django.contrib.auth.decorators import login_required
# @login_required(redirect_field_name='my_redirect_field')


@login_required(login_url='/signin/')
def home(req):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(req, 'dashboard/home.html', context)


@login_required(login_url='/signin/')
def view_category(request, category_id=None):
    if not category_id == None:
        obj = []
        category = Category.objects.filter(pk=category_id)
        if Ebooks.objects.filter(category_id=category_id):
            # get(category_id=1)
            obj = list(Ebooks.objects.filter(category_id=category_id))

        context = {
            'category_name': category[0].name,
            'ebooks': obj
        }
        # response = render(request, 'dashboard/ebooks_page.html', context)
        # response['Content-Disposition'] = 'Inline'
        return render(request, 'dashboard/ebooks_page.html', context)

    # Content-Disposition: Inline
    # return response
    return render(request, 'dashboard/home.html')


@login_required(login_url='/signin/')
def pdf_view(request, ebook_id=None):
    if not ebook_id == None:
        ebook = ['']
        if Ebooks.objects.filter(id=ebook_id):
            ebook = Ebooks.objects.filter(id=ebook_id)
            url = settings.MEDIA_ROOT+'\\' + \
                str(ebook[0].pdf_file).replace('/', '\\')
        # path = os.path.join(settings.MEDIA_ROOT, 'docs\\' + fname)  # 4
            response = FileResponse(
                open(url, 'rb'), content_type="application/pdf")
            response["Content-Disposition"] = "filename={}".format('fname')
            return response
    return render(request, 'dashboard/home.html')

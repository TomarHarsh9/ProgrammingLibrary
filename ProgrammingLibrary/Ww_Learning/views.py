# In the Django framework, views are Python functions or classes that receive a web request and return a web response.
#  The response can be a simple HTTP response, an HTML template response, or an HTTP redirect response that redirects a user to another page.
# after create views.py import in urls.py and give path
from django.shortcuts import redirect, render
from app.models import Categories,CategoriesMCA,Course,CoursePage,Author

# create BASE name Function & request as an argument
def BASE(request):
    return render(request, 'base.html')




def HOME(request):
    category = Categories.objects.all().order_by('id')[0:5]
    Categoriesmca = CategoriesMCA.objects.all().order_by('id')
    course = Course.objects.filter(status='PUBLISH').order_by('-id')
    coursePage = CoursePage.objects.all().order_by('id')


    context = {
        'category': category,
        'Categoriesmca': Categoriesmca,
        'course': course,
        'coursePage': coursePage,
    }

    return render(request, 'main/home.html', context)

def CONTACT_US(request):
    return render(request, 'main/contact_us.html')


def ABOUT_US(request):
    return render(request, 'main/about_us.html')


def COURSESINGLE(request):
    course = Course.objects.filter(status='PUBLISH').order_by('id')
    author = Author.objects.all().order_by('id')

    context = {
        
        'course': course,
        'author ': author,

    }
    return render(request, "main/course-single-v5.html", context)



def COURSEPAGE(request):
    category = Categories.objects.all().order_by('id')[0:1]
    coursePage = CoursePage.objects.all().order_by('id')[0:1]
    categoriesmca = CategoriesMCA.objects.all().order_by('id')

    context = {
        'categoriesmca': categoriesmca,
        'category': category,
        'coursePage': coursePage
    }
    return render(request, "main/course-list-v6.html", context)


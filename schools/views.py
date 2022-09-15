from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required

from .models import School, Province
from .forms import SchoolForm


# Create your views here.


def ShowAllSchools(request):
    province = request.GET.get('province')

    if province == None:
        schools = School.objects.filter(is_published=True).order_by('-created_at')
    else:
        schools = School.objects.filter(province__province_name=province)

    page_num = request.GET.get("page")
    paginator = Paginator(schools, 8)

    try:
        schools = paginator.page(page_num)
    except PageNotAnInteger:
        schools = paginator.page(1)
    except EmptyPage:
        schools = paginator.page(paginator.num_pages)

    provinces = Province.objects.all()

    context = {
        'schools': schools,
        'provinces': provinces
    }

    return render(request, 'showSchools.html', context)


@login_required(login_url='accounts/login')
def SchoolData(request):
    table_data = School.objects.order_by('-created_at')

    number_of_schools = table_data.count()
    print('Total Number of Schools:', number_of_schools)

    page_num = request.GET.get("page")
    paginator = Paginator(table_data, 5)

    try:
        table_data = paginator.page(page_num)
    except PageNotAnInteger:
        table_data = paginator.page(1)
    except EmptyPage:
        table_data = paginator.page(paginator.num_pages)

    context = {
        'table_data': table_data,
        'number_of_schools': number_of_schools
    }

    return render(request, 'db_school.html', context)


def SchoolDetail(request, pk):
    province = request.GET.get('province')

    if province == None:
        schools = School.objects.filter(is_published=True).order_by('-created_at')
    else:
        schools = School.objects.filter(province__province_name=province)

    eachSchool = School.objects.get(id=pk)

    provinces = Province.objects.all()

    context = {
        'eachSchool': eachSchool,
        'provinces': provinces
    }

    return render(request, 'schoolDetail.html', context)

@login_required(login_url='accounts/login')
def addSchool(request):
    form = SchoolForm()

    if request.method == 'POST':
        form = SchoolForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('db_school')

    context = {
        "form": form
    }

    return render(request, 'addSchool.html', context)

@login_required(login_url='accounts/login')
def updateSchool(request, pk):
    school = School.objects.get(id=pk)
    form = SchoolForm(instance=school)

    if request.method == 'POST':
        form = SchoolForm(request.POST, request.FILES, instance=school)
        if form.is_valid():
            form.save()
            return redirect('db_school')

    context = {
        "form": form
    }

    return render(request, 'updateSchool.html', context)

@login_required(login_url='accounts/login')
def deleteSchool(request, pk):
    school = School.objects.get(id=pk)
    school.delete()
    return redirect('db_school')


def searchBar(request):
    if request.method == 'GET':
        search_q = request.GET.get('search_q')
        if search_q:
            schools = School.objects.filter(school_name__icontains=search_q)
            return render(request, 'searchBar.html', {'schools': schools})
        else:
            print("School not Found")
            return request(request, 'searchBar.html', {})


def error_404(request, exception):
    return render(request, 'not-found.html')
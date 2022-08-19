from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseRedirect,
)
from django.shortcuts import (
    render,
    redirect,
)
from django.contrib import messages
# from django.contrib.auth import is_authenticated 
# from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import FormView

#custom forms
from .forms import pontajForm
from .models import jobs

#console output
import logging
logger = logging.getLogger(__name__)

def homepage(request):
    # context = request.user.first_name
    return render(
        request,
        'homepage.html',
        # {'data': context.capitalize()}
    )

# @is_authenticated 
def pontaj(request):
    submitted = False
    if request.method == "POST":
        form = pontajForm(request.POST)
        if form.is_valid():
            # Return an object without saving to the DB
            obj = form.save(commit=False)
            # Add an author field which will contain current user's id
            obj.user_id = request.user.id
            # Save to database
            obj.save()
            # Redirect to webpage after submission
            return HttpResponseRedirect('/pontaj?submitted=True')
    else:
        form = pontajForm
        if 'submitted' in request.GET:
            submitted = True
        return render(
            request,
            'pontaj.html',
            {'form':form, 
             'submitted':submitted}
        )
            
def entries(request):
    objectList = jobs.objects.all()
    return render(
        request,
        'entries.html',
        {'objectList': objectList}
    )

def entries_all(request):
    objectList = jobs.objects.all()
    return render(
        request,
        'entries_all.html',
        {'objectList': objectList}
    )

def delete(request, id):
    object = jobs.objects.get(pk=id)
    object.delete()
    return render(
        request,
        'deletedEntry.html',
        {}
    )

from django.db import connection
def time_all(request):
    #cursor function: Return all rows from a cursor as a dict
    def dictfetchall(cursor):
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
    
    cursor1 = connection.cursor()
    cursor1.execute("""
select auth_user.first_name as name, auth_user.last_name as surname, extract(month from date) as month, sum(end_date-start_date) as time from application_jobs
INNER JOIN auth_user
ON auth_user.id = application_jobs.user_id 
where reason = 'Traveling'
group by month, name, surname                   
    """)
    travelTime = dictfetchall(cursor1)
    
    cursor2 = connection.cursor()
    cursor2.execute("""
select auth_user.first_name as name, auth_user.last_name as surname, extract(month from date) as month, sum(end_date-start_date) as time from application_jobs
INNER JOIN auth_user
ON auth_user.id = application_jobs.user_id 
where reason != 'Traveling'
group by month, name, surname               
    """)
    workTime = dictfetchall(cursor2)
    # print(objectList)
    # print(connection.queries)
    return render(
        request,
        'time_all.html',
        {'travelTime': travelTime,
        'workTime': workTime}    
    ) 

def time(request):
    #cursor function: Return all rows from a cursor as a dict
    def dictfetchall(cursor):
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
    
    user_id = request.user.id
    
    cursor1 = connection.cursor()
    cursor1.execute("""
select auth_user.first_name as name, 
	auth_user.last_name as surname, 
	extract(month from date) as month, 
	sum(end_date-start_date) as time 
from application_jobs
INNER JOIN auth_user
	ON auth_user.id = application_jobs.user_id 
where reason = 'Traveling' and auth_user.id = %s
group by month, name, surname                  
    """, [user_id])
    travelTime = dictfetchall(cursor1)
    print(travelTime)
    
    cursor2 = connection.cursor()
    cursor2.execute("""
select auth_user.first_name as name, 
	auth_user.last_name as surname, 
	extract(month from date) as month, 
	sum(end_date-start_date) as time 
from application_jobs
INNER JOIN auth_user
	ON auth_user.id = application_jobs.user_id 
where reason != 'Traveling' and auth_user.id = %s
group by month, name, surname                  
    """, [user_id])
    workTime = dictfetchall(cursor2)
    # print(objectList)
    # print(connection.queries)
    return render(
        request,
        'time.html',
        {'travelTime': travelTime,
        'workTime': workTime}    
    ) 


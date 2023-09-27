"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import render, redirect 
from django.contrib import messages
from app.models import student
from app.forms import studentform
from django.db import connection
from django.http import HttpResponse
from django.http import JsonResponse
import os
import time
import re
import json
import openllm






def get_student_data():
    queryset = student.objects.all()
    return queryset

def login_home(request):
 
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/user_login.html',
        {'form': studentform}
    )

def Slogin(request):
    if request.method == "POST":

        form = studentform(request.POST)
        username = request.POST.get('uname')
        password = request.POST.get('pswd')
        student_data = get_student_data()
        print(username)
        print(password)
        print(student_data[0].uname)
        print(student_data[0].pswd)
        print([1 if (stack.uname == username and stack.pswd==password) else 0 for stack in student_data])
        if (1 in [1 if (stack.uname == username and stack.pswd==password) else 0 for stack in student_data]):
            # Authentication successful, create session for the user
            print("shifas")
            request.session['username'] = username
            return redirect('profile')  # Redirect to the profile view
        else:
            # Authentication failed
            messages.error(request, 'Invalid username or password.')
            return render(request, 'app/user_login.html', {'form': form})
    else:
        form = studentform()
        return render(request, 'app/user_login.html', {'form': form})





def Profile(request):

    username_s = request.session.get('username')
   # Write the SQL query with the JOIN clause and specify the desired columns
    query = '''
        SELECT Final_HS.id, Final_HS.eid, Final_HS.uname, studenttb.mno, Final_HS.Course
        FROM Final_HS
        INNER JOIN studenttb ON Final_HS.eid = studenttb.eid;
    '''

    # Execute the query using Django's database connection
    with connection.cursor() as cursor:
        cursor.execute(query)

        # Fetch the results
        rows = cursor.fetchall()

        # Filter the rows based on the `uname` column
        
        rows = [row for row in rows if row[2] == username_s]

        # Print the filtered rows
        print(rows)
        columns = [col[0] for col in cursor.description]
    # Get the column names
    
    profile_url = username_s +".jpg"
    

    #Image exists:# Get the directory path where the image is stored
    image_directory = 'C:\\Users\\user\\source\\repos\\Django_mysql\\Django_mysql\\app\\static'
    # Get the list of files in the directory
    files = os.listdir(image_directory)
    # Check if the directory exists
    print(files)
    if any(file==profile_url  for file in files):
        image_exists = True
        

    else:
        # Directory does not exist, image does not exist
        image_exists = False


    return render(request, 'app/Profile.html', {'columns': columns, 'rows_values': rows, 'image_exists': image_exists,'profile_url': profile_url})


def upload_profile_photo(request):
    username_s = request.session.get('username')
    if request.method == 'POST':
        # Get the uploaded file
        profile_photo = request.FILES.get('profile_photo')

        # Handle the file validation and saving logic
        # (e.g., check file type, size, save to the server or database)

        # Example: Save the file to the server (media/uploads folder)
        if profile_photo:
            # Assuming you have a "uploads" folder in your media directory
            path = 'static/' + username_s +".jpg"
            with open('app/' + path, 'wb') as f:
                for chunk in profile_photo.chunks():
                    f.write(chunk)

            # Optionally, you can save the file path to the user's profile
            # profile.photo = path
            # profile.save()

      
        return redirect('profile')

  
    return redirect('profile')


def process_prompt(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prompt = data.get('prompt')

        client = prompt
        bot_response = prompt

        return JsonResponse(bot_response,safe=False)

    return JsonResponse({'error': 'Invalid request method.'})

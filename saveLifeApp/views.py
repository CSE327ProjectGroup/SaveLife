from django.core.files.storage import FileSystemStorage
import mysql.connector as sql
from django.contrib import messages
from django.shortcuts import render, redirect, reverse


def register(request):
    """
    This function will take inputs from the user and checks if the values are valid, if valid then it will write
    into database inside the register_form table. Else it will give an error message and reload the page.

    :param request: Takes a web request.

    :return: Returns a web response.
    """

    if request.method == "POST":

        m = sql.connect(host="localhost", user="root", password="", database='savelifeproject')
        cursor = m.cursor()
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        address = request.POST.get('address')
        number = request.POST.get('contactNum')
        nid = request.POST.get('nid')
        bGroup = request.POST.get('bGroup')
        identity = request.POST.get('identity')
        if password == confirmPassword:
            c = "insert into register_form Values('{}','{}','{}','{}','{}','{}','{}','{}')".format(username, password,
                                                                                                   email, address,
                                                                                                   number, nid, bGroup,
                                                                                                   identity)
            cursor.execute(c)
            m.commit()
            messages.success(request, "Congratulation! Account Created Successfully.")
            return redirect(reverse('login'))
        else:
            messages.success(request, "Password didn't match. Please try again!")
            return render(request, "register.html")
    return render(request, "register.html")


def getPassword():
    return password


def getConfirmPassword():
    return confirmPassword

def organRequest(request):
    """
    This function passes the taken inputs from the user, inserts into database table named organ_requests
    and returns to the same page.

    :param request: Takes a web request.

    :return: Returns a web response.
    """

    if request.method == "POST":
        name = request.POST.get('name')
        num = request.POST.get('Num')
        organ = request.POST.get('Organ')
        uploadedFile = request.FILES["filename"]
        fs = FileSystemStorage()
        fs.save(uploadedFile.name, uploadedFile)
        m = sql.connect(host="localhost", user="root", password="", database='savelifeproject')
        cursor = m.cursor()
        c = "insert into organ_requests Values('{}','{}','{}','{}')".format(name, num, organ, uploadedFile.name)
        cursor.execute(c)
        m.commit()
    return render(request, "organRequest.html")

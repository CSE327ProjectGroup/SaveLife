

def login(request):
    """
    This function will take inputs from the user and match with database, if it matches with database,
     it will show result . Otherwise, it will give an error

    :param request:takes a web request

    :return: returns a web response

    """
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", password="", database='savelifeproject')
        cursor = m.cursor()
        email = request.POST.get('email')
        password = request.POST.get('password')
        c = "select * from register_form where email = '{}' and pass = '{}'".format(email, password)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t == ():
            messages.error(request, "Wrong Credentials! Please Try Again.")
            return render(request, "login.html")
        else:
            c = "select identity from register_form where email = '{}' and pass = '{}'".format(email, password)
            cursor.execute(c)
            result = cursor.fetchall()
            for row in result:
                id = row[0]
            if id == "Patient":
                return redirect("patient")
            elif id == "Donor":
                return redirect("donor")
            elif id == "Volunteer":
                return redirect("volunteer")
    return render(request, "login.html")

def tpCenter(request):
    """
    This function show all the data

    :param request: takes a web request

    :return: returns a web response

    """
    return render(request, "tpcenter.html")

def tpCenterPatient(request):
    """
    This function show all the data

    :param request: takes a web request

    :return: returns a web response

    """
    return render(request, "tpcenterP.html")



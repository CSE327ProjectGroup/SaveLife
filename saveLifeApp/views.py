from django.core.files.storage import FileSystemStorage
import mysql.connector as sql
from django.contrib import messages
from django.shortcuts import render, redirect, reverse


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


global password, confirmPassword


def register(request):
    """
    This function will take inputs from the user and checks if the values are valid, if valid then it will write
    into database inside the register_form table. Else it will give an error message and reload the page.

    :param request: Takes a web request.
    :return:
         returns a web response.
            :if: redirects to login page.
            :else: redirects to register page.
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


def patient(request):
    return render(request, "patient.html")


def donor(request):
      """
      This function assigns the value of 'DonationType' sent from Donor.html by POST method  to variable DonationType
      then checks whether DonationType equals to Live Donation or After Death Donation or Money Donation and redirect to
      Donation.html, AfterDeathDonation.html , Payment.html respectively if the condition is true. Otherwise, it
      redirects to Donor.html

     :param request:

     :return redirect:
     :return render:

     """
    if request.method == "POST":
        donationeType = request.POST.get('donationType')
        if donationeType == "Live Donation":
            return redirect("donation")
        elif donationeType == "After Death Donation":
            return redirect("afterdeathdonation")
        elif donationeType == "Money Donation":
            return redirect("payment")
    return render(request, "donor.html")


def donation(request):
        """
        This function takes values from Donation.html  by POST method, then assigns those values into variables
        and store those variables in Donations datatable of the database by creating a connection with mysql. It
        also uses FileSystemStorage() and file.save(file.name, file) functions to save the uploaded file.

        :param request:
        :return redirect:
        :return render:
        """
    if request.method == "POST":
        donorName = request.POST.get('name')
        donorMail = request.POST.get('email')
        donorAddress = request.POST.get('address')
        donorNum = request.POST.get('contactNum')
        donorNID = request.POST.get('nid')
        donorBG = request.POST.get('bGroup')
        organ = request.POST.get('organ')
        uploaded_file = request.FILES["file"]
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        m = sql.connect(host="localhost", user="root", password="", database='savelifeproject')
        cursor = m.cursor()
        c = "insert into donations Values('{}','{}','{}','{}','{}','{}','{}','{}')".format(donorName, donorMail,
                                                                                           donorAddress, donorNum,
                                                                                           donorNID, donorBG, organ,
                                                                                           uploaded_file.name)
        cursor.execute(c)
        m.commit()
    return render(request, "donation.html")


def afterDeath(request):
        """
    This function takes values from AfterDeathDonation.html  by POST method, then assigns those values into variables
    and store those variables in After_Life_Donation datatable of the database by creating a connection with mysql. It
    also uses FileSystemStorage() and file.save(file.name, file) functions to save the uploaded files.

    :param request:

    :return redirect:
    :return render:
    """
    if request.method == "POST":
        donorName = request.POST.get('name')
        donorNum = request.POST.get('num')
        donorNID = request.POST.get('nid')
        organ = request.POST.get('Organ')
        uploaded_file = request.FILES["file"]
        uploaded_file1 = request.FILES["file2"]
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        fs.save(uploaded_file1.name, uploaded_file1)
        m = sql.connect(host="localhost", user="root", password="", database='savelifeproject')
        cursor = m.cursor()
        c = "insert into afterlifedonation Values('{}','{}','{}','{}','{}','{}')".format(donorName,
                                                                                         donorNum,
                                                                                         donorNID,
                                                                                         organ,
                                                                                         uploaded_file.name,
                                                                                         uploaded_file1.name)
        cursor.execute(c)
        m.commit()
        return redirect("donor")
    return render(request, "afterDeath.html")


def volunteer(request):
    """
    this functions will take input from the user and check, if the values are valid then it will write into database
    inside volunteer table otherwise it will give an error and reload the page

    :param request takes a web request

    :return: returns a web response
    """
    m = sql.connect(host="localhost", user="root", password="", database='savelifeproject')
    cursor = m.cursor()
    c = "SELECT Name, Address, Mobile_Number FROM cash_pay"
    cursor.execute(c)
    r = cursor.fetchall()
    list2 = []
    flag = ""
    for rows in r:
        for i in range(0, 3):
            print(rows[i])
            n = rows[i]
            flag = flag + str(n) + " || "
        list2.append(flag)
        flag = ""
    print(list2)
    return render(request, "volunteer.html", {'list1': list2})


def search(request):
    """"
    This function will take input from user and it checks the input with database,
    if it matches with the database it will show the results
    otherwise it will say no results found massage and reload the page

    :param request takes a web request

    :return: returns a web response

    """
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", password="", database='savelifeproject')
        cursor = m.cursor()
        data = request.POST.get('keyword')

        c = "select * from donor where Organ = '{}'".format(data)
        cursor.execute(c)
        r = cursor.fetchall()
        string = ""
        list2 = []
        for rows in r:
            for i in range(0, 3):
                print(rows[i])
                n = rows[i]
                string = string + str(n) + " || "
            list2.append(string)
            string = ""

        return render(request, "search.html", {'list1': list2})
    else:
        string = "No results found!"
        list2 = [string]
        return render(request, "search.html", {'list1': list2})


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
    return render(request, "tpcenterp.html")




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


def fundRaise(request):
    """
    This function takes the fundraising request.
    For fundraising user upload files and those files take into the uploadedFile , uploadedFile2 and uploadedFile2 variable.
    All the given files save in temp/media.
    """
    if request.method == "POST":
        uploaded_file = request.FILES["file"]
        uploaded_file1 = request.FILES["file1"]
        uploaded_file2 = request.FILES["file2"]
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        m = sql.connect(host="localhost", user="root", password="", database='savelifeproject')
        cursor = m.cursor()
        c = "insert into fund_raising Values('{}','{}','{}')".format(uploaded_file.name, uploaded_file1.name,
                                                                     uploaded_file2.name)
        cursor.execute(c)
        m.commit()
    return render(request, "fundRaising.html")


def forgetPass(request):
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", password="", database='savelifeproject')
        cursor = m.cursor()
        nid = request.POST.get('nid')
        password = request.POST.get('password')
        c = "UPDATE register_form SET pass = '{}' WHERE nid = '{}'".format(password, nid)
        cursor.execute(c)
        m.commit()
        return redirect("login")
    return render(request, "forgetpass.html")


def payment(request):
        """
    This function will select the payment type.
    payment assign in flag.
    check flag equal to cash payment.
    If flag equal to cashpayment then redirect to the cashpay else redirect to the paypal.
    """
    if request.method == "POST":

        flag = request.POST.get("payment")
        if flag == "Cash Payment":
            return redirect("cashpay")
        else:
            return redirect("paypal")
    return render(request, "payment.html")


def paymentPatient(request):
        """
    This function will select the payment type.
    payment assign in flag.
    check flag equal to cash payment.
    If flag equal to cashpayment then redirect to the cashpay else redirect to the paypal.
    """
    if request.method == "POST":

        flag = request.POST.get("payment")
        if flag == "Cash Payment":
            return redirect("cashpay")
        else:
            return redirect("paypal")
    return render(request, "paymentp.html")


def cashPayment(request):
        """
    Decleraing name variable for username.
    Decleraing address variable for address.
    Decleraing number variable for number.
    Decleraing patientid variable for id.
    All the given data write into the database.

    """
    if request.method == "POST":
        name = request.POST.get("username")
        address = request.POST.get("address")
        number = request.POST.get("number")
        patientID = request.POST.get("id")
        m = sql.connect(host="localhost", user="root", password="", database='savelifeproject')
        cursor = m.cursor()
        c = "insert into cash_pay Values('{}','{}','{}','{}')".format(name, address, number, patientID)
        cursor.execute(c)
        m.commit()
        return redirect("donor")
    return render(request, "CashPayment.html")


def about(request):
    return render(request, "about.html")


def aboutPatient(request):
    return render(request, "aboutp.html")


def contact(request):
    return render(request, "contact.html")


def contactPatient(request):
    return render(request, "contactp.html")


def patientList(request):
    m = sql.connect(host="localhost", user="root", password="", database='savelifeproject')
    cursor = m.cursor()
    c = "SELECT Name, Organ FROM organ_requests"
    cursor.execute(c)
    r = cursor.fetchall()
    list2 = []
    flag = ""
    for rows in r:
        for i in range(0, 2):
            print(rows[i])
            n = rows[i]
            flag = flag + str(n) + " || "
        list2.append(flag)
        flag = ""
    return render(request, "patientlist.html", {'list1': list2})


def paypal(request):
        """
    This function Check the amount and pass the amount into the paypal gateway.
    """
    if request.method == "POST":
        amount = request.POST.get("amount")
        content = {
            'amount': amount
        }
        return render(request, "paypal.html", content)
    return render(request, "paypal.html")

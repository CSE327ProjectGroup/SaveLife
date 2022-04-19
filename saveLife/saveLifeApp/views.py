from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, reverse
import mysql.connector as sql
from django.contrib import messages
from saveLife import settings

global donationType, donorNum, donorNid
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
        donationType = request.POST.get('donationType')
        if donationType == "Live Donation":
            return redirect("Donation")
        elif donationType == "After Death Donation":
            return redirect("afterDeathDonation")
        elif DonationType == "Money Donation":
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
        donorNid = request.POST.get('nid')
        donorBloodGroup = request.POST.get('bGroup')
        organ = request.POST.get('organ')
        uploadedFile = request.FILES["file"]
        fileSave = FileSystemStorage()
        fileSave.save(uploadedFile.name, uploadedFile)
        m = sql.connect(host="localhost", user="root", password="", database='save_life_project')
        cursor = m.cursor()
        c = "insert into donations Values('{}','{}','{}','{}','{}','{}','{}','{}')".format(donorName, donorMail,
                                                                                           donorAddress, donorNum,
                                                                                           donorNid, donorBloodGroup,
                                                                                           organ, uploadedFile.name)
        cursor.execute(c)
        m.commit()
    return render(request, "donation.html")


def after_death(request):
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
        donorNid = request.POST.get('nid')
        organ = request.POST.get('organ')
        uploadedFile = request.FILES["file"]
        uploadedFile1 = request.FILES["file2"]
        fileSave = FileSystemStorage()
        fileSave.save(uploadedFile.name, uploadedFile)
        fileSave.save(uploadedFile1.name, uploadedFile1)
        m = sql.connect(host="localhost", user="root", password="", database='save_life_project')
        cursor = m.cursor()
        c = "insert into after_life_donation Values('{}','{}','{}','{}','{}','{}')".format(donorName,
                                                                                           donorNum,
                                                                                           donorNid,
                                                                                           organ,
                                                                                           uploadedFile.name,
                                                                                           uploadedFile1.name)
        cursor.execute(c)
        m.commit()
        return redirect("donor")
    return render(request, "afterDeath.html")

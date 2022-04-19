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


def paymentP(request):
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
        patientId = request.POST.get("id")
        m = sql.connect(host="localhost", user="root", password="", database='savelifeproject')
        cursor = m.cursor()
        c = "insert into cash_pay Values('{}','{}','{}','{}')".format(name, address, number, patientId)
        cursor.execute(c)
        m.commit()
        return redirect("donor")
    return render(request, "CashPayment.html")


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
def fundRaise(request):
    """
    This function takes the fundraising request.
    For fundraising user upload files and those files take into the uploadedFile , uploadedFile2 and uploadedFile2 variable.
    All the given files save in temp/media.
    """
    if request.method == "POST":
        uploadedFile = request.FILES["file"]
        uploadedFile1 = request.FILES["file1"]
        uploadedFile2 = request.FILES["file2"]
        fileSystem = fileSystemStorage()
        fileSystem.save(uploaded_file.name, uploaded_file)
        m = sql.connect(host="localhost", user="root", password="", database='savelifeproject')
        cursor = m.cursor()
        c = "insert into fund_raising Values('{}','{}','{}')".format(uploadedFile.name, uploadedFile1.name,
                                                                     uploadedFile2.name)
        cursor.execute(c)
        m.commit()
    return render(request, "fundRaising.html")
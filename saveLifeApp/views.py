def search(request):
    """"
    This function will take input from user and it matches the with database,
    if it matches with the database it will show the results
    otherwise it will give an error massage and reload the page

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
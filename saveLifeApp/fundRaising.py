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
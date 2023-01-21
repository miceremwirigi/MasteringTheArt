import io
import pdfkit
from django.shortcuts import render, redirect

# Create your views here.

from .models import PersonalInfo
from .forms import PersonalInfoForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from docx import *
from docx.shared import Inches


def home(request):
    return render(request, "home.html")

# view to show members in the database


def listCustomers(request):
    members = PersonalInfo.objects.all()

    context = {
        'members': members,
    }
    return render(request, 'listcustomers.html', context)


# Form to add customer info to database
def createnewinfo(request):
    form = PersonalInfoForm()
    if request.method == "POST":
        form = PersonalInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("/"))

    context = {
        "form": form,
    }
    return render(request, "createnewinfo.html", context)

# Show details of all information of specific customers, e.g., name, ID, phone etc.


def customerInfo(request, pk):
    infos = PersonalInfo.objects.filter(idNumber=pk).values()[0]

    context = {
        "infos": infos,
    }
    print(infos)
    print(type(infos))
    for info, value in infos.items():
        print(info)
        print(value)
    return render(request, "customerinfo.html", context)


# generate and download specific CV document
# import modules to use with word document


def getDocument(request, pk):
    infos = PersonalInfo.objects.filter(idNumber=pk).values()[0]
    document = Document()
    print(infos)
    docx_title = infos.get('name') + "_CV.docx"
    pdf_title = "TEST_DOCUMENT. pdf"

    # __CV doc__ #
    h = document.add_heading()
    h.add_run(u"Personal Info: \n", 0)
    p = document.add_paragraph()
    p.paragraph_format.line_spacing = 2
    for info, value in infos.items():
        if info == "idNumber":
            info = "ID Number"
        elif info == "maritalStatus":
            info = "Marital Status"
        p.add_run(info). bold = True
        p.add_run(":  " + str(value) + "\n")
    document.add_page_break()

    # Prepare the document for download #
    f = io.BytesIO()
    document.save(f)
    length = f.tell()
    f.seek(0)

    '''
    #____ pdf format also____#
    options = {
        'page-size':'Letter',
        # 'format':'pdf',
        'encoding':'utf-8',
    }

    pdf = pdfkit.from_string(f.getvalue(),False, options)
    response = HttpResponse(pdf, content_type="application/pdf")
    response['Content-Disposition'] = "attachment; filename=" + pdf_title
    response["Content-Length"] = length
    '''

    # ____ word docx format ____#
    response = HttpResponse(f.getvalue(
    ), content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    response['Content-Disposition'] = "attachment; filename=" + docx_title
    response["Content-Length"] = length

    return response


# # to test how to work wuth docx
# def testDocument(request):
#     document = Document()
#     docx_title = "TEST_DOCUMENT.docx"
#     pdf_title = "TEST_DOCUMENT. pdf"

#     #__CV doc__ #
#     p = document.add_paragraph()
#     p.add_run("Test text1.")
#     p.add_run("Test text2.")
#     document.add_page_break()

#     # Prepare the document for download #
#     f = io.BytesIO()
#     print(f)
#     document.save(f)
#     length = f.tell()
#     f.seek(0)

#     '''
#     #____ pdf format also____#
#     options = {
#         'page-size':'Letter',
#         # 'format':'pdf',
#         'encoding':'utf-8',
#     }

#     pdf = pdfkit.from_string(f.getvalue(),False, options)
#     response = HttpResponse(pdf, content_type="application/pdf")
#     response['Content-Disposition'] = "attachment; filename=" + pdf_title
#     response["Content-Length"] = length
#     '''

#     # ____ word docx format ____#
#     response = HttpResponse(f.getvalue(), content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
#     response['Content-Disposition'] = "attachment; filename=" + docx_title
#     response["Content-Length"] = length


#     return response

# Show all clients whose data is available in the database

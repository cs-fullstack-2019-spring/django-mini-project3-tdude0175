from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse
from .forms import TeacherRecordForm , ClassRecordModel
# Create your views here.


# renders all entries for view
def index(request):
    teacherForm = TeacherRecordForm()
    classModel = ClassRecordModel.objects.all()
    context= \
        {
            'teacherForm':teacherForm,
            'classList': classModel
        }
    return render(request, 'teacherRecordApp/index.html',context)

# filters through objects via teacherName to manipulate them
def detailList(request,teacherID):
    teacherDetails = ClassRecordModel.objects.filter(teacherName=teacherID)
    return render(request,'teacherRecordApp/teacherEntries.html',{'teacher':teacherDetails})

# filters through objects via school
def schoolDetailList(request,schoolID):
    schoolDetails = ClassRecordModel.objects.filter(school=schoolID)
    return render(request,'teacherRecordApp/schoolList.html',{'school':schoolDetails})

# reworked presented details
def updateDetails(request,classID):
    teacherEntry = get_object_or_404(ClassRecordModel, pk = classID)
    entryForm = TeacherRecordForm(request.POST or None, instance=teacherEntry)
    if entryForm.is_valid():
        entryForm.save()
        return redirect('index')
    context =\
        {
            'form':entryForm
        }
    return render(request,'teacherRecordApp/updateDetails.html',context)

# remove an entry from the list
def deleteDetails(request,classID):
    teacherEntry = get_object_or_404(ClassRecordModel, pk = classID)
    if request.method == 'POST':
        teacherEntry.delete()
        return redirect('index')
    return render(request,'teacherRecordApp/DeleteEntry.html')

def newEntry(request):
    teacherForm = TeacherRecordForm(request.POST or None)
    classModel = ClassRecordModel.objects.all()
    if teacherForm.is_valid():
        teacherForm.save()
        return redirect('index')

    context= \
        {
            'teacherForm':teacherForm,
            'classList': classModel
        }
    return render(request,'teacherRecordApp/newEntry.html',context)
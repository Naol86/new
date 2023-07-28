from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Register_Patient,Doctors,Nurses,Drug_Stor
from .forms import DrugAdd
from django.db.models import Q

# Create your views here.

def Home(request):
    
    if request.GET.get('search') != None :
        search = request.GET.get('search')
    else:
        search = '#'
    
    patients = Register_Patient.objects.filter(
        Q(Full_Name__icontains = search) 
        )
    patient_count = patients.count()
    
    context = {'patients':patients,'patient_count':patient_count}
    
    return render (request,"home.html",context)

def RegisterPatient(request):
    if request.method == 'POST':
        First_Name = request.POST.get('First_Name')
        Middle_Name = request.POST.get('Middle_Name')
        Last_Name = request.POST.get('Last_Name')
        Father_Name = request.POST.get('Father_Name')
        Mother_Name = request.POST.get('Mother_Name')
        Sex = request.POST.get('Sex')
        Age = request.POST.get('Age')
        Address = request.POST.get('Address')
        Phone_number = request.POST.get('Phone_number')
        Emergency_Phone_number = request.POST.get('Emergency_Phone_number')
        Birth_Date = request.POST.get('Birth-Date')
        lis = [First_Name,Middle_Name,Last_Name,Father_Name,Mother_Name,Sex,Age,Address,Phone_number,Emergency_Phone_number,Birth_Date]
        try:
            patient = Register_Patient.objects.create(
                First_Name = First_Name,
                Middle_Name = Middle_Name,
                Last_Name = Last_Name,
                Father_Name = Father_Name,
                Mother_Name = Mother_Name,
                Sex= Sex,
                Address = Address,
                Phone_Number = Phone_number,
                Emergency_Phone_Number = Emergency_Phone_number,
                Birth_Day = Birth_Date,
                Age = Age,
            )
            patient.save()
            return redirect('register-patient')
        except:
            print(lis)
    return render(request,"register_patient.html")

def RegisterDoctor(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        Doctor_Field = request.POST['Doctor-Field']
        Room = request.POST['Room']
        
        doctor = Doctors.objects.create(
            Name = Name,
            Doctor_Field = Doctor_Field,
            Room = Room,
        )
        doctor.save()
        return redirect('register-doctor')
    return render(request,'register_doctor.html')

def Nurse(request):
    
    patients = Register_Patient.objects.filter(Nurse_Checked=False).first()
    doctors = Doctors.objects.all()

    if request.method == 'POST':
        doctor_name = request.POST.get('doctor')
        patient_name = request.POST.get('patient')
        status = request.POST.get('status')
        try:
            doctor = Doctors.objects.get(Name=doctor_name)
            patient = Register_Patient.objects.get(Full_Name=patient_name)
        except (Doctors.DoesNotExist, Register_Patient.DoesNotExist):
            # Handle the case when doctor or patient is not found
            return HttpResponse("Invalid doctor or patient name.")
        patient.Nurse_Checked = True
        new = Nurses.objects.create(
            patient = patient,
            status = status,
            doctor = doctor,
        )
        new.patient.Nurse_Checked=True
        new.save()
        return redirect('Nurse')
    context = {'patients': patients ,'doctors':doctors}
    return render(request, 'nurse.html', context)

def add_drug(request):
    drug_form = DrugAdd()
    if request.method == 'POST':
        drug_form = DrugAdd(request.POST)
        if drug_form.is_valid():
            drug_form.save()
            return redirect('add-drug')
    all_drug = Drug_Stor.objects.all()
    dictionary = {'form' : drug_form, 'all_drug' : all_drug}
    return render(request,'add_drug.html',dictionary)

def Doctor(request,pk):
    doctor = Doctors.objects.get(id=pk)
    patients = Nurses.objects.get(doctor=doctor)
    context = {'doctor': doctor, 'patients': patients}
    return render(request,'doctor.html',context)
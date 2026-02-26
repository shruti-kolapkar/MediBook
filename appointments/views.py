from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment, Doctor
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')


def doctors_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors.html', {
        'doctors': doctors
    })


@login_required
def book_appointment(request, id):
    doctor = get_object_or_404(Doctor, id=id)

    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')

        Appointment.objects.create(
            patient=request.user,
            doctor=doctor,
            date=date,
            time=time
        )
        return redirect('doctors')

    return render(request, 'book_appointment.html', {'doctor': doctor})


@login_required
def my_appointments(request):
    appointments = Appointment.objects.filter(patient=request.user)
    return render(request, 'my_appointments.html', {'appointments': appointments})
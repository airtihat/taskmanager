from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Donation
from django.db.models import Q
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
import io

# لوحة التبرعات مع الفلاتر
@login_required
def sadaqa_dashboard(request):
    donations = Donation.objects.all()

    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')
    recipient = request.GET.get('recipient')

    if from_date:
        donations = donations.filter(date__gte=from_date)
    if to_date:
        donations = donations.filter(date__lte=to_date)
    if recipient:
        donations = donations.filter(recipient__icontains=recipient)

    return render(request, 'sadaqa/dashboard.html', {'donations': donations})


# إضافة تبرع جديد
@login_required
def add_donation(request):
    if request.method == 'POST':
        Donation.objects.create(
            amount=request.POST['amount'],
            recipient=request.POST['recipient'],
            date=request.POST['date'],
            type=request.POST['type'],
            notes=request.POST.get('notes', '')
        )
    return redirect('sadaqa:dashboard')


# تصدير PDF
@login_required
def export_pdf(request):
    donations = Donation.objects.all()

    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')
    recipient = request.GET.get('recipient')

    if from_date:
        donations = donations.filter(date__gte=from_date)
    if to_date:
        donations = donations.filter(date__lte=to_date)
    if recipient:
        donations = donations.filter(recipient__icontains=recipient)

    html_string = render_to_string('sadaqa/pdf_template.html', {'donations': donations})
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html_string.encode("UTF-8")), result)

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("حدث خطأ أثناء إنشاء ملف PDF")

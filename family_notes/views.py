from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Note
from django.contrib.auth.decorators import login_required
from io import BytesIO
from django.shortcuts import render


@login_required

def export_notes_pdf(request):
    notes = Note.objects.all()
    template = get_template('family_notes/pdf_template.html')
    html = template.render({'notes': notes})

    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), dest=result)

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("خطأ في توليد ملف PDF", status=500)

@login_required
def note_list(request):
    notes = Note.objects.all()
    return render(request, 'family_notes/note_list.html', {'notes': notes})
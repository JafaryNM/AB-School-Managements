from django import template
from student.models import Results,Subject

register = template.Library()

@register.simple_tag
def get_subject_result(student_id,subject_id,exam_id):
    results=Results.objects.filter(student_id=student_id,subject_id=subject_id,exam_id=exam_id).first()
    if results:
        return results.mark
        return '-'

@register.simple_tag
def get_avarage_result(student_id,exam_id):
    subject_no=Subject.objects.all().count()
    totalmark = 0
    #results = Results.objects.filter(student_id=student_id, subject_id=subject_id, exam_id=exam_id).aggregate(sumt=Sum('mark'))['sumt']
    results=Results.objects.filter(student_id=student_id,exam_id=exam_id)
    for res in results:
        totalmark +=res.mark
        global  avarage
        avarage=round( (totalmark/subject_no), 2)

    return (avarage)





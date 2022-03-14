


from curses.ascii import HT
from multiprocessing import context
from re import I
from xml.sax import SAXNotSupportedException
from django.db.models.base import Model
from django.views.generic import ListView,UpdateView,CreateView,DeleteView, TemplateView,RedirectView,View
from .models import Darasa, Exam, Results, Student, Subject
from .forms import * #ViewResultsForm,ViewSingleSubjectResultForm, ResultsForm,AddResultsForm,InputResultsForm
from django.shortcuts import redirect, render,HttpResponse,HttpResponseRedirect
from django.urls import reverse
import datetime
#from .forms import ViewSubjectResultForm


# Create your views here.


#subjectcrud

class SubjectList(ListView):
    model=Subject
    template_name='subjects/subjects.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['subjects']=Subject.objects.all()
        return context
class CreateSubject(CreateView):
    model=Subject
    template_name='subjects/form.html'
    fields='__all__'
    context_object_name='form'
    success_url='/'
class UpdateSubject(UpdateView):
    model=Subject
    template_name='subjects/form.html'
    fields='__all__'
    context_object_name='form'
    success_url='/'

class DeleteSubject(DeleteView):
     model=Subject
     success_url='/'


#Exam crud

class ExamList(ListView):
    model=Exam
    template_name='exams/exams.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['exams']=Exam.objects.all()
        return context

class CreateExam(CreateView):
    model=Exam
    template_name='subjects/form.html'
    fields='__all__'
    context_object_name='form'
    success_url='/'
class UpdateSubject(UpdateView):
    model=Subject
    template_name='subjects/form.html'
    fields='__all__'
    context_object_name='form'
    success_url='/'

class DeleteSubject(DeleteView):
    model=Exam
    success_url='/'

#class crud

class DarasaList(ListView):
    model=Darasa
    template_name='darasa/darasa.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['darasa']=Darasa.objects.all()
        return context

class CreateDarasa(CreateView):
    model=Darasa
    template_name='darasa/form.html'
    fields='__all__'
    context_object_name='form'
    success_url='/'

class UpdateDarasa(UpdateView):
    model=Darasa
    template_name='darasa/form.html'
    fields='__all__'
    context_object_name='form'
    success_url='/'

class DeleteDarasa(DeleteView):
    model=Darasa
    success_url='/'

#Crud Students
class StudentList(ListView):
    model=Student
    template_name='students/students.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['students']=Student.objects.all()
        return context


class CreateStudent(CreateView):
    model=Student
    template_name='students/form.html'
    fields='__all__'
    context_object_name='form'
    success_url='/'


class UpdateStudent(UpdateView):
    model=Results
    template_name='results/form.html'
    field='__all__'
    context_object_name='form'
    success_url='/'

class DeleteStudent(DeleteView):
    model=Results
    success_url='/'

#display results
class ViewResults(CreateView):
    template_name = 'results/form.html'
    template_list= 'results/results.html'
    model = Results
    form_class = ViewSingleSubjectResultForm
    context_object_name = 'form'
    success_url = '/'

    def  post(self, request, *args, **kwargs):
        form=ViewSubjectResultForm
        if  form.is_valid:
            exam_id=request.POST.get('exam')
            exam=Exam.objects.get(id=exam_id)
            darasa_id=request.POST.get('darasa')
            darasa=Darasa.objects.get(id=darasa_id)
            students=Student.objects.filter(darasa_id=darasa_id)
            subjects=Subject.objects.all()

            return render(request, self.template_list,{'darasa': darasa, 'exam': exam,'students':students,'subjects':subjects})
        else:
            return render(request, self.template_name, {'form': form})

class ViewSingleResult(CreateView):
    #View Results
    template_name = 'results/form.html'
    template_list='results/singleresults.html'
    model=Results
    form_class = ViewSingleSubjectResultForm
    context_object_name = 'form'
    succes_url='/'

    def post(self, request, *args, **kwargs):
        form = ViewSingleSubjectResultForm
        if form.is_valid:
            exam_id = request.POST.get('exam')
            exam = Exam.objects.get(id=exam_id)
            subject_id = request.POST.get('subject')
            subject = Subject.objects.get(id=subject_id)
            darasa_id = request.POST.get('darasa')
            darasa = Darasa.objects.get(id=darasa_id)
            results=Results.objects.filter(darasa_id=darasa_id,exam_id=exam_id,subject_id=subject_id)
            return render(request, self.template_list,
                          {'subject': subject, 'darasa': darasa, 'results': results, 'exam': exam})
        else:
            pass
#display single subject Results
class AddSingleResults(CreateView):
    template_name = 'results/form.html'
    template_list = 'results/results.html'
    model = Results
    form_class = ViewResultsForm
    context_object_name = 'form'
    succes_url = '/'

    def post(self, request, *args, **kwargs):
        form = ViewResultsForm
        if form.is_valid:
            students=Student.objects.all()
            subject_no=Subject.objects.all().count()
            subjects=Subject.objects.all()
            exam_id = request.POST.get('exam')
            exam = Exam.objects.get(id=exam_id)
            return render(request, self.template_list,
                          { 'subject_no':subject_no , 'subjects': subjects, 'students':students,  'exam': exam})
        else:
            pass
#Adding Results
class   ResultInputMultipleStudentFormPage(View):
    model=Results
    context_object_name = 'form'
    form_class = InputMultipleResultsForm
    success_url = '/'
    template_name='results/inputmultiplesubjectresult.html'
    #template_name ='results/form.html'

    def get(self, *args,**kwargs):
        context = {}
        context['students']=Student.objects.filter(darasa_id=self.kwargs['darasaid']).order_by('-id')
        context['examob']=Exam.objects.get(id=self.kwargs['examid'])
        context['subob']=Subject.objects.get(id=self.kwargs['subjectid'])
        context['darasa']=Darasa.objects.get(id=self.kwargs['darasaid'])
        context['form']=self.form_class
        return render(self.request,self.template_name,context)
    
    # Taking data from form
    def post(self, request, *args, **kwargs):
        form=InputMultipleResultsForm(self.request)
    # Taking data from form
        if form.is_valid:
            
            exam_id = self.kwargs['examid']
            exam=Exam.objects.get(id=exam_id)
            subject_id=self.kwargs['subjectid']
            subject=Subject.objects.get(id=subject_id)
            darasa_id=self.kwargs['darasaid']
            darasa = Darasa.objects.get(id=darasa_id)
            mark=request.POST.getlist('mark')
            student_id=request.POST.getlist('student')
            
            
            for a in range(len(student_id)):
                
                student_obj=Student.objects.get(id=student_id[a]) 
                
                if not Results.objects.filter(exam_id=exam_id, subject_id=subject_id,darasa_id=darasa_id, student_id=student_id[a]).exists():
                    results=Results.objects.create(
                    exam_id=exam_id, 
                    subject_id=subject_id,
                    darasa_id=darasa_id,
                    student_id=student_obj.id,
                    mark=mark[a] 
                    )
            return redirect(reverse('singleresults',kwargs={'subjectid':subject_id,'darasaid':darasa_id,'examid':exam_id}))
                    
            
            
              
            
                
            
            #results=Results.objects.filter(darasa_id=darasa_id,exam_id=exam_id,subject_id=subject_id)
        else:
            pass

#display add results

### DISPLAY SINGLE RESULTS 

class ResultsSingleSubject(ListView):
    template_name='results/singleresults.html'
    model=Results
    
    #get values from url kwargs
    def get_context_data(self, **kwargs):
        
       context = super(ResultsSingleSubject, self).get_context_data(**kwargs)
       context['exam']=Exam.objects.get(id=self.kwargs['examid'])
       context['darasa']=Darasa.objects.get(id=self.kwargs['darasaid'])
       context['subject']=Subject.objects.get(id=self.kwargs['subjectid'])
       context['results']=Results.objects.filter(exam_id=self.kwargs['examid'], darasa_id=self.kwargs['darasaid'],subject_id=self.kwargs['subjectid'])
       return context
         
        
## UPDATE RESULTS 

class UpdateResults(CreateView):
    
    template_name='results/input'
        
    
        
    
    
    




class AddResults(CreateView):
    
    model=Results
    context_object_name='form'
    fields=['subject','exam','darasa']
    success_url='/'
    template_list='results/addsubjectresults.html'
    template_name ='results/form.html'
    def post(self, request, *args, **kwargs):
        form=AddResultsForm
    # Taking data from form
        if form.is_valid:
            students=Student.objects.all()
            exam_id = request.POST.get('exam')
            subject_id=request.POST.get('subject')
            darasa_id=request.POST.get('darasa')
            return redirect(reverse('input_multiple_student_result',kwargs={'subjectid':subject_id,'darasaid':darasa_id,'examid':exam_id}))
        else:
            return render(self.request,self.template_name,{'form':form})

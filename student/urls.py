
from django.urls import path
from .views  import  *


urlpatterns = [
  #Subjecst urls
  path("subjects/", SubjectList.as_view(), name='subjectslist'),
  path("subject/create", CreateSubject.as_view(), name='subjectscreate'),
  path("subject/<int:pk>/update/", UpdateSubject.as_view(), name='subjectupdate'),
  path("subject/subject/<int:pk>/delete", DeleteSubject.as_view(), name='subjectdelete'),

  #Exam urls
  path("exams/", ExamList.as_view(), name='examslist'),
  path("exam/create", CreateExam.as_view(), name='examscreate'),
  path("subject/<int:pk>/update/", UpdateSubject.as_view(), name='examupdate'),
  path("subject/<int:pk>/delete/", DeleteSubject.as_view(), name='examdelete'),

  # Classes urls

   path("class/", DarasaList.as_view(), name='darasalist'),
   path("darasa/create", CreateDarasa.as_view(), name='darasacreate'),
   path("darasa/<int:pk>/update/", UpdateDarasa.as_view(), name='darasaupdate'),
   path("darasa/<int:pk>/delete/", DeleteDarasa.as_view(), name='darasadelete'),

# Result urls
 path("viewallresults", ViewResults.as_view(), name='resultcreate'),
 path("singleresult",ViewSingleResult.as_view(), name='singleresult'),

 path("results/",  AddSingleResults.as_view(), name='viewresults'),
 path("",  AddResults.as_view(), name='addresults'),
 path("updateresult",  AddResults.as_view(), name='addresults'),

 
      

path("<int:subjectid>/<int:examid>/<int:darasaid>/student-form-input",  ResultInputMultipleStudentFormPage.as_view(), name='input_multiple_student_result'),
path("<int:subjectid>/<int:examid>/<int:darasaid>/subjectresults", ResultsSingleSubject.as_view(), name='singleresults'),
#path("",  GetResultFormPage.as_view(), name='addresults'),
#path("",  ResultInput.as_view(), name='addresults'),



#path("addresults",  ResultInput.as_view(), name='addresults'),
#path("",  ResultInput.as_view(), name='viewresults'),

    



    # Student urls
  path("students", StudentList.as_view(), name='studentslist'),
  path("students/create",CreateStudent.as_view(), name='studentscreate'),
  path("students/<int:pk>/update/", UpdateStudent.as_view(), name='studentupdate'),
  path("student/<int:pk>/delete/", DeleteStudent.as_view(), name='studentdelete'),


]
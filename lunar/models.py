from django.db import models
import datetime
from .usermanager import MyUserManager
from django.utils import timezone

from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

#College model
class Collage (models.Model):
    id = models.AutoField(primary_key=True)
    code = models.IntegerField()
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name



#Course model
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_code = models.IntegerField()
    course_name = models.CharField(max_length=200, null=True, blank=True)
    course_total = models.CharField(max_length=200, null=True, blank=True)
    collage_id = models.ForeignKey(Collage, on_delete=models.DO_NOTHING, default=1)

    def __str__(self):
        return self.course_name
        
#Teacher model

class Teacher(models.Model):
        
    _id = models.AutoField(primary_key=True,editable=False)
    title =  models.CharField(max_length=200, null=True, blank = True)
    surname = models.CharField(max_length=200, null=True, blank = True)
    firstname = models.CharField(max_length=200,null=True,blank=True)
    middlename = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(unique = True,null=True, blank = True)
    phone = models.IntegerField(null = True)
    college = models.CharField(max_length=200, null=True, blank = True)
    dept =  models.CharField(max_length=200, null=True, blank = True)
    course =  models.CharField(max_length=200, null=True, blank = True)
    #course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING, default=1)  # to be removed
   # subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, default=1) 

    building = models.CharField(max_length=200, null=True, blank = True)
    officenumber = models.CharField(max_length=200, null=True, blank = True)
    password = models.CharField(max_length=200,null=True,blank=True)
    profile =  models.ImageField(null=False, blank=False)
    Teacher_id = models.IntegerField(null = True)
   
    def __str__(self):
        return str(self.surname)


#hero model
class Hero(models.Model):       # defined
    surname = models.CharField(max_length=60,null=True)  #added
    first_name = models.CharField(max_length=200,null=True,blank=True)
    middle_name = models.CharField(max_length=200,null=True,blank=True)
    gender=models.CharField(max_length=200,null=True,blank=True)
    email=models.CharField(max_length=200,null=True,blank=True)
    phoneNumber=models.CharField(max_length=200,null=True,blank=True)
    student_id=models.CharField(max_length=200,null=True,blank=True)
    college=models.CharField(max_length=200,null=True,blank=True)
    #course= models.CharField(max_length=200,null=True,blank=True)
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING, default=1)
    #subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, default=1)
    year_of_enrollment=models.CharField(max_length=200,null=True,blank=True)
    password=models.CharField(max_length=200,null=True,blank=True)
    #student_id=models.CharField(max_length=200,null=True,blank=True)

    profile_photo=models.CharField(max_length=200,null=True,blank=True)   # not defined

    def __str__(self):
        return self.surname


#tech model temp
class Tech(models.Model):       # defined
    #_id = models.AutoField(primary_key=True,editable=True,max_length=200)  
    _id = models.AutoField(primary_key=True,editable=True)
    title1 =  models.CharField(max_length=200, null=True, blank = True)
    surname = models.CharField(max_length=200, null=True, blank = True)
    firstname = models.CharField(max_length=200,null=True,blank=True)
    middlename = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(unique = True,null=True, blank = True)
    phone = models.IntegerField(null = True)
    college = models.CharField(max_length=200, null=True, blank = True)
    dept =  models.CharField(max_length=200, null=True, blank = True)
    course =  models.CharField(max_length=200, null=True, blank = True)
    #course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING, default=1)  # to be removed
   #subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, default=1) 

    building = models.CharField(max_length=200, null=True, blank = True)
    officenumber = models.CharField(max_length=200, null=True, blank = True)
    password = models.CharField(max_length=200,null=True,blank=True)
    profile =  models.ImageField(null=True, blank=False)
    #Teacher_id = models.IntegerField(null = True)
    Teacher_id = models.CharField(null = True, max_length=200)

    #Teacherid = models.CharField(max_length=200, null=True, blank = True)

   
    def __str__(self):
        return str(self.surname)

#Subject model
class Subject(models.Model):

        Subject_name = models.CharField(max_length=200,null=True,blank=True)
        _id = models.AutoField(primary_key=True,editable=False)
        course_id = models.ForeignKey(Course, on_delete=models.CASCADE, default=1) #need to give defauult course
        Teacher_id = models.ForeignKey(Tech, on_delete=models.CASCADE)
        student_id = models.ForeignKey(Hero, on_delete=models.CASCADE)
        
    
        def __str__(self):
            return self.Subject_name

    
#Appointment model
class Appointment(models.Model):
    appointment_date = models.DateField(null = True)
    appointment_time = models.TimeField(null = True)
    reason = models.CharField(max_length=200, null=True, blank=True)
    appointment_id = models.CharField(max_length=200, null=True, blank=True)      # added per xsheet
    student_id = models.CharField(max_length=200, null=True, blank=True)

    #id = models.AutoField(primary_key=True)      
    #appointment_message = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    #status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.reason)

class Assignments(models.Model):
    course = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)   # added per xsheet
    attachment = models.FileField(null=True, blank=True)
    group = models.CharField(max_length=200, null=True, blank=True)             # added per xsheet
    assignment_id = models.CharField(max_length=200, null=True, blank=True)      # added per xsheet
    #student_id = models.CharField(max_length=200, null=True, blank=True)     # added per xsheet
    #student_idd = models.ForeignKey(Hero, on_delete=models.CASCADE)
    #course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

   
    type = models.CharField(max_length=200, null=True, blank=True)
    due = models.DateTimeField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.course)
    
class Calender(models.Model):
    date = models.DateField(null = True)
    time = models.TimeField(null = True)
    reason = models.CharField(max_length=200, null=True, blank=True)
    group = models.CharField(max_length=200, null=True, blank=True)             # added per xsheet
    notification = models.CharField(max_length=200, null=True, blank=True)      # added per xsheet
    teacher_id = models.CharField(max_length=200, null=True, blank=True)
          
    def __str__(self):
        return str(self.reason)

class Notice(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)   # added per xsheet
    attachment = models.FileField(null=True, blank=True)
    group = models.CharField(max_length=200, null=True, blank=True)             # added per xsheet
    notice_id = models.CharField(max_length=200, null=True, blank=True)      # added per xsheet
    
    def __str__(self):
         return str(self.title)

    
    

class Posts(models.Model):

    teacher = models.ForeignKey(Tech, on_delete = models.CASCADE, related_name="techy"
    )
    tittle = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    photo = models.FileField(null=False, blank=False)
    group = models.CharField(max_length=200, null=True, blank=True)             # added per xsheet
    doxtype = models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True,editable=False)

   
    def __str__(self):
        return str(self.teacher.Teacher_id)

      #  return f"{self.teacher.Teacher_id} - {self.title1}"


# assignment data table (teacher)
class Assignment_teacher(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)   # added per xsheet
    attachment = models.FileField(null=True, blank=True)
    group = models.CharField(max_length=200, null=True, blank=True)             # added per xsheet
    assignment_id = models.CharField(max_length=200, null=True, blank=True)      # added per xsheet
    teacher_id = models.CharField(max_length=200, null=True, blank=True)     # added per xsheet

    
    
    def __str__(self):
        return str(self.title)


class Classes_teacher(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)   # added per xsheet
    group = models.CharField(max_length=200, null=True, blank=True)             # added per xsheet
    classes_id = models.CharField(max_length=200, null=True, blank=True)      # added per xsheet
    teacher_id = models.CharField(max_length=200, null=True, blank=True)     # added per xsheet

    
    
    def __str__(self):
        return str(self.name)

class Announcement(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)   # added per xsheet
    photo = models.FileField(null=True, blank=True)
    group = models.CharField(max_length=200, null=True, blank=True)             # added per xsheet
    announcement_id = models.CharField(max_length=200, null=True, blank=True)      # added per xsheet


    
    def __str__(self):
        return str(self.title)

    
#Live session used in notification - tearch/subject FK to be added
class Session(models.Model):
    course_name = models.CharField(max_length=200,blank=True, null= True,default="DEFAULT VALUE")
    tutor = models.CharField(max_length=200,null=False,blank=True)
    course_code = models.IntegerField(default = 0) #models.ForeignKey(Course, on_delete=models.CASCADE, default=1) 
    venue = models.CharField(max_length=200,null=False,blank=True)
    time = models.TimeField(auto_now = True)
    phone_no = models.IntegerField()
    assistance_tutor = models.CharField(max_length=200,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    total_students =  models.IntegerField(default = 0)
    
    def __str__(self):
        return self.course_name



   
#Student model
class Student(models.Model):
    student_id =models.IntegerField()
    student_group = models.CharField(max_length=200,null=True,blank=True)
    student_name = models.CharField(max_length=200,null=True,blank=True)
    student_class_code = models.IntegerField(null=True, blank=True,default=0)
    student_total =  models.IntegerField(null=True,blank=True,default=0)
    _id = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.student_group

#Results model
class Results(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE, default=1)
    subject_assignment_marks = models.FloatField(default=0)
    id = models.AutoField(primary_key=True,editable=False)
    objects = models.Manager()

    def __str__(self):
        return self.subject_assignment_marks


 #Attendance model  
class Attendance(models.Model):
    Subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    Attendance_date = models.DateField()
    Student_id =models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    _id = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return str(self.Subject_id)



#Attendance Report model
class AttendanceReport(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    Attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.Attendance_id)

class Documents(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    name_doc= models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=200, null=True, blank=True)
    attachment = models.FileField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)
    course_name = models.CharField(max_length=200,blank=True, null= True)

    def __str__(self):
        return str(self.name)





class User(AbstractBaseUser):
    role_options = (
        ("student", "student"),
        ("teacher", "teacher"),
        ("admin", "admin"),
    )
    login_id = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=255)
    hint = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=role_options)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = MyUserManager()

    USERNAME_FIELD = 'login_id'

    def __str__(self):
        return f"{self.login_id}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
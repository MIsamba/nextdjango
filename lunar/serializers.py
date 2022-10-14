from .models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.utils.dateparse import parse_datetime
from django.contrib.humanize.templatetags import humanize
from .models import  Hero,Posts,Assignments,Documents,Course,Session,Student,Students,Teacher,Subject,Results,Attendance,AttendanceReport,Appointment,Calender,Notice,Assignment_teacher,Classes_teacher,Announcement


#User serializer

class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ['login_id','role']
   


#hero
class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'


class  PostsSerializer(serializers.ModelSerializer):
    #datehumanize = serializers.SerializerMethodField('dateHumanize')
    profile = serializers.CharField(read_only = True,source="teacher.profile")
    surname = serializers.CharField(read_only = True,source="teacher.surname")
    firstname = serializers.CharField(read_only = True,source="teacher.firstname")
    middlename = serializers.CharField(read_only = True,source="teacher.middlename")


    #def dateHumanize(self,obj):
        #formatted_time = humanize.naturaltime(obj.createdAt)
        #return str(formatted_time)
    
    
    class Meta:
        model = Posts
        fields = '__all__'
        extra_fields = ['profile,surname,firstname,middlename']



#Assignments serializer
class  AssignmentsSerializer(serializers.HyperlinkedModelSerializer):
    getcreatedat = serializers.SerializerMethodField('getCreatedAt')
    getdue = serializers.SerializerMethodField('getDue')

    def getCreatedAt(self,obj):
        formatted_time = parse_datetime(str(obj.createdAt)).strftime('%d-%m-%Y')
        return str(formatted_time)

    def getDue(self,obj):
        try:
            formatted_time = parse_datetime(str(obj.due)).strftime('%d-%m-%Y')
            return str(formatted_time)
        except:
            return "None"
    
    class Meta:
        model =  Assignments
        fields = '__all__'



'''
class DocumentListSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = DocumentList
        fields = '__all__'
'''
#Documents serializer
class  DocumentsSerializer(serializers.HyperlinkedModelSerializer):
  #  documents = DocumentListSerializer(many = True)


    class Meta:
        model = Documents
        fields = '__all__'


    #def get_avater(self, obj):
     # return obj.avater.url

"""
    def create(self, validated_data):
        hero = Hero.objects.create_hero(**validated_data)
        return hero

    class Meta:
        model = Hero
        fields = '__all__' 
        validators = [
            UniqueTogetherValidator(
                queryset=Hero.objects.all(),
                fields=['id', 'password']
            )
        ]


"""





#course serializer

class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = '__all__'


#Session serializer
class SessionSerializer(serializers.ModelSerializer):
    getdate = serializers.SerializerMethodField('getDate')

    def getDate(self,obj):
        formatted_time = parse_datetime(str(obj.date)).strftime('%d-%m-%Y')
        return str(formatted_time)
    
    class Meta:
        model = Session
        fields = '__all__'


#student serializer
class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'
#student serializer

class StudentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        fields = '__all__'

#class Student_courseSerializer(serializers.ModelSerializer):
 #   class Meta:
  #      model = Student_course
   #     fields = '__all__'

#calender
class CalenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Calender
        fields = '__all__'

         

#notice
class NoticeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'


        
#Teacher serializer
class TeacherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teacher
        exclude = ['password']



class Assignment_teacherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Assignment_teacher
        fields = '__all__'


class Classes_teacherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Classes_teacher
        fields = '__all__'

class AnnouncementSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Announcement
        fields = '__all__'




#Subject serializer
class SubjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subject
        fields = '__all__'

#Results serializer
class  ResultsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Results
        fields = '__all__'



#Attendance serializer
class AttendanceSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField('getDate')

    def getDate(self,obj):
        try:
            date = parse_datetime(obj.Attendance_date).strftime('%d-%m-%Y')
            return str(date)
        except:
            return "None"
    class Meta:
        model = Attendance
        fields = '__all__'

#AttendanceReport serializer
class AttendanceReportSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   AttendanceReport
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Attendance
        fields = '__all__'

#Appointment serializer
class  AppointmentSerializer(serializers.ModelSerializer):
    student_id = StudentSerializer()
    appointment_message = AttendanceSerializer()
    date = serializers.SerializerMethodField('getDate')

    def getDate(self,obj):
        try:
            date = parse_datetime(obj.appointment_date).strftime('%d-%m-%Y')
            return str(date)
        except:
            return "None"
    
    class Meta:
        model =   Appointment
        fields = '__all__'


class HeroSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Hero
        fields = '__all__'

class AssignmentSerializer(serializers.ModelSerializer):
    getcreatedat = serializers.SerializerMethodField('getCreatedAt')
    getdue = serializers.SerializerMethodField('getDue')

    def getCreatedAt(self,obj):
        formatted_time = parse_datetime(str(obj.createdAt)).strftime('%d-%m-%Y')
        return str(formatted_time)

    def getDue(self,obj):
        formatted_time = parse_datetime(str(obj.due)).strftime('%d-%m-%Y')
        return str(formatted_time)
    
    class Meta:
        model = Assignments
        fields = '__all__'
'''
class Course_AssignmentSerializer(serializers.ModelSerializer):
        getcreatedat = serializers.SerializerMethodField('getCreatedAt')
        getdue = serializers.SerializerMethodField('getDue')

        def getCreatedAt(self,obj):
            formatted_time = parse_datetime(str(obj.createdAt)).strftime('%d-%m-%Y')
            return str(formatted_time)

        def getDue(self,obj):
            formatted_time = parse_datetime(str(obj.due)).strftime('%d-%m-%Y')
            return str(formatted_time)

        class Meta:
            model = Course_Assignment
            fields = '__all__'

class Total_AssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Total_Assignment
        fields = '__all__'


'''
    
class DocumentSerializer(serializers.ModelSerializer):
    getcreatedat = serializers.SerializerMethodField('getCreatedAt')

    def getCreatedAt(self,obj):
        formatted_time = parse_datetime(str(obj.createdAt)).strftime('%d-%m-%Y')
        return str(formatted_time)

    class Meta:
        model = Documents
        fields = '__all__'
from django.urls import include, path
from rest_framework import routers
from . import views
from .views import UserRecordView


router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)
router.register(r'tech', views.TechViewSet)

router.register(r'posts',views.PostViewSet)
router.register(r'assignments',views.AssignmentViewSet)
router.register(r'documents',views.DocumentViewSet)
router.register(r'sessions',views.SessionViewSet)

#router.register(r'documentslist',views.DocumentListViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('user/', UserRecordView.as_view(), name='users'),
    path('heroes/',views.HeroViewSet),
    path('subject/',views.getSubject),
    path('session/<course>/',views.sessiondetails),
    path('assignment/',views.assignmentdetails),
    path('calender/<status>/', views.getCalender),  #added path
    path('notice/<status>/', views.getNotice),          #added path
    path('Assignment_teacher/<status>/', views.getAssignment_teacher),          #added path
    path('teacher/', views.getTeacher),          #added path
   
    path('Classes_teacher/<status>/', views.getClasses_teacher),          #added path
    
    path('Announcement/<status>/', views.getClasses_teacher),          #added path
    path('document/<course>/',views.documentdetails),
    path('document/<course>/<name>/',views.alldocumentdetails),
    path('filterassignment/<status>/',views.filterassignment),
    path('postview/',views.PostView),
    path('postview/<postname>/',views.PostDetailView),
    path('postview/<postname>/delete/',views.PostViewDelete),
    path('postview/<postname>/update/',views.PostViewUpdate),
    path('assignmentview/',views.AssignmentView),
    path('sessionview/',views.SessionView),
    path('sessionview/<int:id>/',views.SessionViewDelete),

    path('getuser/', views.LoadUserView.as_view()),
    path('tutor/', views.TutorView.as_view()),
    path('tutorupdate/', views.TutorUpdate),
    path('appointment/<status>/', views.getAppointment),

]
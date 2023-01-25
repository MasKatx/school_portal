from django.urls import path
from .views import (
    GetUserAvatarView,
    UpdateUserAvatarView,
    GetUserProfileView,
    UpdateUserProfileView,
    CreateTeachersAccountView,
    DeleteTeachersAccountView,
    UpdateTeachersAccountView,
    CreateStudentsAccountView,
    DeleteStudentAccountView,
    GetAllTeachersAccountProfile,
    GetAllTeachersAccount,
    ShowStudentAccountsView,
    GetAllTeacherAvatarByAdmin,
)

# GetUserProfileView,

urlpatterns = [
    path("user", GetUserProfileView.as_view()),
    path("user_update", UpdateUserProfileView.as_view()),
    path("user_avatar", GetUserAvatarView.as_view()),
    path("get_all_teacher_avt", GetAllTeacherAvatarByAdmin.as_view()),
    path("user_avatar_update/<int:pk>", UpdateUserAvatarView.as_view()),
    path("get_all_teacher", GetAllTeachersAccount.as_view()),
    path("get_all_teacher_account", GetAllTeachersAccountProfile.as_view()),
    path("create_teacher_account", CreateTeachersAccountView.as_view()),
    path("update_teacher_account/<int:pk>", UpdateTeachersAccountView.as_view()),
    path("delete_teacher_account/<int:pk>", DeleteTeachersAccountView.as_view()),
    path("create_student_account", CreateStudentsAccountView.as_view()),
<<<<<<< HEAD
    path("delete_student_account", DeleteStudentAccountView.as_view()),
=======
    path("showaccounts/<path:str>", ShowStudentAccountsView.as_view()),
>>>>>>> 7e527447173e72f7e8f16870656da4a3df027e98
    # path("csrf_cookie", GetCSRFToken.as_view()),
]

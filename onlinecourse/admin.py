from django.contrib import admin
# import any new models
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 4

# register QuestionInline class
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 4

# register ChoiceInline class    
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

# register models
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Submission)
# register Question and Choice models
admin.site.register(Question, QuestionAdmin) 
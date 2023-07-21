from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner
from .models import Question, Choice

# <HINT> Register QuestionInline and ChoiceInline classes here
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 2

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

# Question and Choice models
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text']
    inlines = [ChoiceInline]

# <HINT> Register Question and Choice models here

admin.site.register(Question, QuestionAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)

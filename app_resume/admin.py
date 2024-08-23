from django.contrib import admin
from app_resume.models import Resume , WorkExperience

# Register your models here.

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('user' , 'job_title' , 'field_type')
    list_editable = ('job_title' ,)
    search_fields = ('user__username' , 'job_title')



class  WorkExperienceaAdmin(admin.ModelAdmin):
    list_display = ('title' , 'company_name')
    list_filter = ('resume' , )
    

admin.site.register(Resume , ResumeAdmin)
admin.site.register(WorkExperience , WorkExperienceaAdmin)

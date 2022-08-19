from django.contrib import admin

from .models import jobs

@admin.register(jobs)
class jobsAdmin(admin.ModelAdmin):
    #displayed columns
    list_display = ('user', 'reason', 'start_date', 'end_date', 'description')
    
    #date ordering
    # date_hierarchy = "start_date"
    #order by
    ordering = ("user",)

    #right side filter
    list_filter = ('user','start_date','reason')
    #search bar
    search_fields = ("user",)
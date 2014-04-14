django-csvadmin
===============


Basic django admin class to allow exporting fields of a model to CSV.



Usage:
------

    from csvadmin.admin import CSVAdmin
    
    class MyModelAdmin(CSVAdmin):
        ...
        
    
or just:

    from csvadmin.admin import CSVAdmin
    
    admin.site.register(MyModel, CSVAdmin)

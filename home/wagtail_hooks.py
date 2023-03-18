from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from timetable.models import Event


class EventModelAdmin(ModelAdmin):
    model = Event
    menu_icon = "date"
    menu_label = "События"
    ordering = ["start_date"]
    list_display = ["title", "start_date", "active"]
    menu_item_name = "Событие"


modeladmin_register(EventModelAdmin)

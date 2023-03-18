from datetime import date, timedelta

from wagtail.models import Page

from timetable.models import Event


class HomePage(Page):

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        today = date.today()
        end_of_week = today + timedelta(days=7)
        all_events = Event.objects.filter(active=True).filter(start_date__range=[today, end_of_week])
        events_by_date = get_events_by_date(all_events)
        dates = [today + timedelta(days=x) for x in range(7)]
        context['dates'] = [{'date': d, 'events': events_by_date.get(d, [])} for d in dates]
        return context

    max_count = 1


def get_events_by_date(all_events):
    events = {}
    for event in all_events:
        start_date = event.start_date.date()
        if start_date in events:
            events[start_date].append(event)
        else:
            events[start_date] = [event]
    return events

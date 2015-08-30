from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .forms import EntryForm
from .models import Entry
import datetime
from django.utils import timezone


def home_page(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = EntryForm(request.POST)

            if form.is_valid():
                entry = form.save(commit=False)
                entry.enterdate = timezone.now
                entry.save()
        else:
            form = EntryForm()
        return render(request, 'app/homepage.html', {'form': form, 'CHOICES': Entry.CATEGORY_CHOICES})
    else:
        return render(request, 'app/refusepage.html', {})


def category_view(request, var_category, days='30'):
    if request.user.is_authenticated():
        entrys = Entry.objects.order_by('-datetime').filter(category=var_category)
        date = datetime.datetime.now().date()
        dicty = {}
        dates = []
        for x in range(1, int(days)+1):
            str_date = date.strftime('%Y-%m-%d')
            dicty[str_date] = []
            dates.append(str_date)
            date = date - datetime.timedelta(days=1)
        for entry in entrys:
            eDate = entry.datetime.date().strftime('%Y-%m-%d')
            if eDate in dicty.keys():
                dicty[eDate].append(entry)
        return render(request, 'app/categoryview.html',{'entrys': entrys, 'dicty': dicty, 'dates':dates})
    else:
        return render(request, 'app/refusepage.html', {})

def value_view(request, var_category, var_value, days='30'):
    if request.user.is_authenticated():
        entrys = Entry.objects.order_by('-datetime').filter(category=var_category).filter(value__icontains=var_value)
        date = datetime.datetime.now().date()
        dicty = {}
        dates = []
        for x in range(1, int(days)+1):
            str_date = date.strftime('%Y-%m-%d')
            dicty[str_date] = []
            dates.append(str_date)
            date = date - datetime.timedelta(days=1)
        for entry in entrys:
            eDate = entry.datetime.date().strftime('%Y-%m-%d')
            if eDate in dicty.keys():
                dicty[eDate].append(entry)
        return render(request, 'app/categoryview.html',
                      {'entrys': entrys, 'dicty': dicty, 'dates':dates})
    else:
        return render(request, 'app/refusepage.html', {})

def entry_list(request):
    if request.user.is_authenticated():
        entrys = Entry.objects.all().order_by('-enterdate')
        return render(request, 'app/entry_list.html', {'entrys':entrys})
    else:
        return render(request, 'app/refusepage.html', {})




def edit_page(request,pk):
    if request.user.is_authenticated():
        entry = get_object_or_404(Entry, pk=pk)
        if request.POST.get('delete'):
            entry.delete()
            return redirect('app.views.entry_list')
        if request.method == "POST":
            form = EntryForm(request.POST, instance=entry)
            if form.is_valid():
                entry = form.save(commit=False)
                entry.enterdate = timezone.now
                entry.save()
                return redirect('app.views.entry_list')
        else:
            form = EntryForm(instance=entry)
        return render(request, 'app/editpage.html', {'form': form})
    else:
        return render(request, 'app/refusepage.html', {})
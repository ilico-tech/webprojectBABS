from django.shortcuts import render,redirect
from .models import Voiture
from .forms import VoitureForm

from autoexpress.filters import VoitureFilter
from django .core .paginator import Paginator
from django.contrib.auth.decorators import login_required
from django .http import Http404
# Create your views here.
def LocationVoiture(request):
    voitures=Voiture.objects.all()
    myfilters = VoitureFilter(request.GET, queryset=voitures)
    voitures = myfilters.qs

    paginator = Paginator(voitures,10)
    page_number = request.GET.get('page')
    page_objet = paginator.get_page(page_number)



    voitures_number=voitures.count()



    context={'voitures':page_objet,'voitures_number':voitures_number,'myfilters':myfilters}
    return render(request,'voitures/location_voiture.html',context)







def DetailVoiture(request,id):
    voiture=Voiture.objects.get(id=id)

    context={'voiture':voiture,}



    return render(request,'voitures/detail_voiture.html',context)



def LouermaVoiture(request):
    if request.method == 'POST':
        form =VoitureForm(request.POST,request.FILES)
        if form.is_valid():

          #  form=form.save(commit=False)
          # form.user=request.user
            form.save()
        return redirect('voiture')

    else:
        form=VoitureForm()

    context={'form':form}
    return render(request,'voitures/louer_ma_voiture.html',context)



def ModifierVoiture(request,id):
    voiture=Voiture.objects.get(id=id)
    if voiture.user == request.user:
     if request.method == 'POST':
       form =VoitureForm(request.POST,request.FILES,instance=voiture)
       if form.is_valid():
        form.save()
       return redirect('voiture')

     else: form=VoitureForm(instance=voiture)



     context={'form':form,'voiture':voiture}


     return render(request,'voitures/Modifier_ma_voiture.html',context)












def SupprimerVoiture(request,id):
        voiture=Voiture.objects.get(id=id)
        if voiture.user == request.user:
         if request.method == 'POST':
           voiture.delete()

           return redirect('/')
         context={'voiture':voiture}

         return render(request,'voitures/supprimer_ma_voiture.html',context)











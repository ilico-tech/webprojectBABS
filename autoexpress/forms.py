from django import forms
from .models import Voiture

class VoitureForm(forms.ModelForm):

    class Meta:
         model=Voiture
         fields=('image','image1','image2','service','status','marque','categorie','emplacement','imageproprio','nom','telephone','email',
                 'prix','cartegrise','content' ,'annee','carburant','kilometrage','boitevitesse','nbrplaces')




         widgets={
             'image':forms.FileInput(attrs={'id':'image'

             }),
              'image1':forms.FileInput(attrs={'id':'image1'

             }),


              'image2' : forms.FileInput(attrs={'id':'image2'

             }),


              'service':forms.Select(attrs={'class':'form-control'

             }),

             'status':forms.Select(attrs={'class':'form-control'

             }),

             'marque':forms.TextInput(attrs={'class':'form-control'

                }),
            'categorie':forms.TextInput(attrs={'class':'form-control'

               }),
           'emplacement' :forms.TextInput(attrs={'class':'form-control',

                }),
            'imageproprio' : forms.FileInput(attrs={ 'class':'form-control',

                }),
            'telephone':forms.NumberInput(attrs={'class':'form-control'

                   }),
             'email':forms.EmailInput(attrs={'class':'form-control'

                   }),
            'prix':forms.TextInput(attrs={'class':'form-control'

                   }),
             'cartegrise':forms.FileInput(attrs={'class':'form-control'

             }),
             ' content':forms.TextInput(attrs={'class':'form-control'

                  }),
             'annee':forms.NumberInput(attrs={'class':'form-control'

                 }),
            ' carburant ':forms.TextInput(attrs={'class':'form-control'

                }),
             'kilometrage':forms.TextInput(attrs={'class':'form-control'

                  }),
           ' boitevitesse' :forms.TextInput(attrs={'class':'form-control'

                   }),
             'nbrplaces':forms.NumberInput(attrs={'class':'form-control'

                 }),

           'content': forms.Textarea(attrs={'class': 'form-control'

                                                   }),

          'nom': forms.TextInput(attrs={'class': 'form-control'

                                              })

         }










from django.forms import ModelForm, Textarea, ImageField, FileInput
from apps.pet.models import CadastroPet


class CadPet(ModelForm):
    class Meta:
        model = CadastroPet
        fields = '__all__'
        widgets = {

            'descricao': Textarea(attrs={'cols': 10, 'rows': 5, 'placeholder': 'Uma Breve Descrição sobre o Pet'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super(CadPet, self).__init__(*args, **kwargs)
    #     self.fields['imagem'].label = "Selecione a Foto do Pet"

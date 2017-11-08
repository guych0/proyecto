from django import forms
from .models import Vehiculos, Parqueo

class ParqueoForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Parqueo
        fields = ('nombre','fecha_inicial','fecha_salida','transportes')
def __init__ (self, *args, **kwargs):
        super(ParqueoForm, self).__init__(*args, **kwargs)
        self.fields["transportes"].widget = forms.widgets.CheckboxSelectMultiple()

        self.fields["transportes"].help_text = "Ingrese la placa del vehiculo"

        self.fields["transportes"].queryset = Vehiculos.objects.all()

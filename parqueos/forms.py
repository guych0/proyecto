from django import forms

from .models import Vehiculos, Parqueo

class ParqueoForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Parqueo
        fields = ('nombre','fecha_inicial','fecha_salida','transportes')
def __init__ (self, *args, **kwargs):
        super(ParqueoForm, self).__init__(*args, **kwargs)


        self.fields["Tipos"].widget = forms.widgets.CheckboxSelectMultiple()

        self.fields["Tipos"].help_text = "Ingrese la placa del vehiculo"

        self.fields["Tipos"].queryset = Vehiculos.objects.all()

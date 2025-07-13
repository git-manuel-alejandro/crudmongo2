from django import forms

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    descripcion = forms.CharField(widget=forms.Textarea, required=False)
    precio = forms.IntegerField()
    caracteristicas = forms.CharField(
        required=False,
        help_text="Separar por comas (ej: ligero, resistente, impermeable)"
    )

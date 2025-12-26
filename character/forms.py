from django import forms
from .models import Character


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Динамически фильтруем специализации по выбранному классу
        if 'character_class' in self.data:
            class_id = self.data.get('character_class')
            self.fields['specialization'].queryset = Specialization.objects.filter(
                character_class_id=class_id
            )
        elif self.instance.pk:
            self.fields['specialization'].queryset = self.instance.character_class.specializations.all()
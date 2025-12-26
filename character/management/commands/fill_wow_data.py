from django.core.management.base import BaseCommand
from character.models import CharacterClass, Race, Specialization
from character.constants import CLASS_CHOICES, RACE_CHOICES, CLASSES_DATA

class Command(BaseCommand):
    help = 'Заполняет базу данных WoW классами, расами и специализациями'
    
    def handle(self, *args, **options):
        # Создаем классы
        class_objects = {}
        for class_key, class_name in CLASS_CHOICES:
            obj, created = CharacterClass.objects.get_or_create(
                name=class_key
            )
            class_objects[class_key] = obj
            
        # Создаем расы
        race_factions = {
            # Альянс
            'human': 'alliance',
            'dwarf': 'alliance',
            'night_elf': 'alliance',
            'gnome': 'alliance',
            'draenei': 'alliance',
            'worgen': 'alliance',
            'void_elf': 'alliance',
            'lightforged_draenei': 'alliance',
            'dark_iron_dwarf': 'alliance',
            'kul_tiran': 'alliance',
            'mechagnome': 'alliance',
            # Орда
            'orc': 'horde',
            'undead': 'horde',
            'tauren': 'horde',
            'troll': 'horde',
            'blood_elf': 'horde',
            'goblin': 'horde',
            'nightborne': 'horde',
            'highmountain_tauren': 'horde',
            'maghar_orc': 'horde',
            'zandalari_troll': 'horde',
            'vulpera': 'horde',
            # Общие
            'pandaren_a': 'alliance',  # или horde в зависимости от выбора
            'dracthyr_a': 'alliance',  # или horde
            'earthen_a': 'alliance',   # или horde

            'pandaren': 'horde',  # или horde в зависимости от выбора
            'dracthyr': 'horde',  # или horde
            'earthen': 'horde',
        }
        
        for race_key, race_name in RACE_CHOICES:
            faction = race_factions.get(race_key, 'alliance')
            Race.objects.get_or_create(
                name=race_key,
                defaults={'faction': faction}
            )
        
        # Создаем специализации
        for class_data in CLASSES_DATA:
            character_class = class_objects.get(class_data['name'])
            if character_class:
                for spec in class_data['specs']:
                    Specialization.objects.get_or_create(
                        character_class=character_class,
                        name=spec['name'],
                        defaults={'role': spec['role']}
                    )
        
        self.stdout.write(self.style.SUCCESS('Данные WoW успешно загружены!'))

# python manage.py fill_wow_data

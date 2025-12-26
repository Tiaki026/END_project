
ROLE_CHOICES = [
    ('tank', 'Танк'),
    ('healer', 'Хилер'),
    ('melee', 'Ближний бой'),
    ('ranged', 'Дальний бой'),
]

CLASS_CHOICES = [
    ('warrior', 'Воин'),
    ('paladin', 'Паладин'),
    ('hunter', 'Охотник'),
    ('rogue', 'Разбойник'),
    ('priest', 'Жрец'),
    ('death_knight', 'Рыцарь смерти'),
    ('shaman', 'Шаман'),
    ('mage', 'Маг'),
    ('warlock', 'Чернокнижник'),
    ('monk', 'Монах'),
    ('druid', 'Друид'),
    ('demon_hunter', 'Охотник на демонов'),
    ('evoker', 'Пробудитель'),
]

CLASSES_DATA = [
    # Воин
    {'name': 'warrior', 'specs': [
        {'name': 'Оружие', 'role': 'melee'},
        {'name': 'Неистовство', 'role': 'melee'},
        {'name': 'Защита', 'role': 'tank'},
    ]},
    # Паладин
    {'name': 'paladin', 'specs': [
        {'name': 'Свет', 'role': 'healer'},
        {'name': 'Защита', 'role': 'tank'},
        {'name': 'Воздаяние', 'role': 'melee'},
    ]},
    # Охотник
    {'name': 'hunter', 'specs': [
        {'name': 'Повелитель зверей', 'role': 'ranged'},
        {'name': 'Стрельба', 'role': 'ranged'},
        {'name': 'Выживание', 'role': 'melee'},
    ]},
    # Разбойник
    {'name': 'rogue', 'specs': [
        {'name': 'Ликвидация', 'role': 'melee'},
        {'name': 'Головорез', 'role': 'melee'},
        {'name': 'Скрытность', 'role': 'melee'},
    ]},
    # Жрец
    {'name': 'priest', 'specs': [
        {'name': 'Послушание', 'role': 'healer'},
        {'name': 'Свет', 'role': 'healer'},
        {'name': 'Тьма', 'role': 'ranged'},
    ]},
    # Рыцарь смерти
    {'name': 'death_knight', 'specs': [
        {'name': 'Кровь', 'role': 'tank'},
        {'name': 'Лед', 'role': 'melee'},
        {'name': 'Нечестивость', 'role': 'melee'},
    ]},
    # Шаман
    {'name': 'shaman', 'specs': [
        {'name': 'Стихии', 'role': 'ranged'},
        {'name': 'Совершенствование', 'role': 'melee'},
        {'name': 'Исцеление', 'role': 'healer'},
    ]},
    # Маг
    {'name': 'mage', 'specs': [
        {'name': 'Тайная магия', 'role': 'ranged'},
        {'name': 'Огонь', 'role': 'ranged'},
        {'name': 'Лед', 'role': 'ranged'},
    ]},
    # Чернокнижник
    {'name': 'warlock', 'specs': [
        {'name': 'Колдовство', 'role': 'ranged'},
        {'name': 'Демонология', 'role': 'ranged'},
        {'name': 'Разрушение', 'role': 'ranged'},
    ]},
    # Монах
    {'name': 'monk', 'specs': [
        {'name': 'Пивовар', 'role': 'tank'},
        {'name': 'Ткач туманов', 'role': 'healer'},
        {'name': 'Тенебрас', 'role': 'melee'},
    ]},
    # Друид
    {'name': 'druid', 'specs': [
        {'name': 'Баланс', 'role': 'ranged'},
        {'name': 'Сила зверя', 'role': 'melee'},
        {'name': 'Страж', 'role': 'tank'},
        {'name': 'Исцеление', 'role': 'healer'},
    ]},
    # Охотник на демонов
    {'name': 'demon_hunter', 'specs': [
        {'name': 'Истребление', 'role': 'melee'},
        {'name': 'Месть', 'role': 'tank'},
    ]},
    # Пробудитель
    {'name': 'evoker', 'specs': [
        {'name': 'Разорение', 'role': 'ranged'},
        {'name': 'Сохранение', 'role': 'healer'},
    ]},
]

RACE_CHOICES = [
    # Альянс
    ('human', 'Человек'),
    ('dwarf', 'Дворф'),
    ('night_elf', 'Ночной эльф'),
    ('gnome', 'Гном'),
    ('draenei', 'Дреней'),
    ('worgen', 'Ворген'),
    ('void_elf', 'Эльф Бездны'),
    ('lightforged_draenei', 'Озаренный дреней'),
    ('dark_iron_dwarf', 'Дворф из клана Черного Железа'),
    ('kul_tiran', 'Култирасец'),
    ('mechagnome', 'Мехагном'),
    ('pandaren_a', 'Пандарен'),
    ('dracthyr_a', 'Драктир'),
    ('earthen_a', 'Земельники'),
    # Орда
    ('orc', 'Орк'),
    ('undead', 'Нежить'),
    ('tauren', 'Таурен'),
    ('troll', 'Тролль'),
    ('blood_elf', 'Эльф крови'),
    ('goblin', 'Гоблин'),
    ('nightborne', 'Ночнорожденный'),
    ('highmountain_tauren', 'Таурен Крутогорья'),
    ('maghar_orc', 'Магхарский орк'),
    ('zandalari_troll', 'Зандаларский тролль'),
    ('vulpera', 'Вульпера'),
    ('pandaren', 'Пандарен'),
    ('dracthyr', 'Драктир'),
    ('earthen', 'Земельники'),
]

FACTION_CHOICES = [
    ('alliance', 'Альянс'),
    ('horde', 'Орда'),
]

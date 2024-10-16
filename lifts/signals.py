from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Building, Elevator


@receiver(post_migrate)


def create_buildings(sender, **kwargs):
    buildings_data = [
        ("D36",),  # Добавь другие здания, если они нужны
    ]

    # Для каждого здания добавляем лифты
    for address in buildings_data:
        building, created = Building.objects.get_or_create(address=address[0])

        if created:
            elevators_data = [
                ("P1", "Лифт Р1 - 42422309"),
                ("P2", "Лифт Р2 - 42422311"),
                ("P3", "Лифт Р3 - 42422310"),
                ("P4", "Лифт Р4 - 42422312"),
                ("P5", "Лифт Р5 - 42422313"),
                ("P6", "Лифт Р6 - 42422314"),
                ("P7", "Лифт Р7 - 42422315"),
                ("P8", "Лифт Р8 - 42422316"),
                ("P9", "Лифт Р9 - 42422317"),
                ("P12", "Лифт Р12 - 42422320"),
                ("P13", "Лифт Р13 - 42422321"),
                ("P14", "Лифт Р14 - 42422322"),
                ("P15", "Лифт Р15 - 42422323"),
                ("P16", "Лифт Р16 - 42422324"),
                ("P17", "Лифт Р17 - 42422325"),
                ("P18", "Лифт Р18 - 42422326"),
                ("P19", "Лифт Р19 - 42422327"),
                ("SV1", "Лифт SV1 - 42422328"),
                ("SV2", "Лифт SV2 - 42422329"),
                ("SV3", "Лифт SV3 - 42422330"),
                ("SV4", "Лифт SV4 - 42422331"),
                ("SV5", "Лифт SV5 - 42422332"),
                ("SV6", "Лифт SV6 - 42422333"),
                ("SV7", "Лифт SV7 - 42422334"),
                ("SV8", "Лифт SV8 - 42422335"),
                # Добавь сюда все лифты для этого здания
            ]

            for elevator_code, elevator in elevators_data:
                Elevator.objects.get_or_create(
                    building=building,  # Привязываем к созданному зданию
                    elevator_name=elevator_code
                )

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from lifts.models import Building, Elevator

import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
dot_env = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path=dot_env)


class Command(BaseCommand):
    help = "Заполняет базу данных начальными данными"

    def handle(self, *args, **kwargs):
        # Создаем здания и лифты
        buildings_data = [
            {
                "address": "D36",
                "elevators": [
                    "P1",
                    "P2",
                    "P3",
                    "P4",
                    "P5",
                    "P6",
                    "P7",
                    "P8",
                    "P9",
                    "P12",
                    "P13",
                    "P14",
                    "P15",
                    "P16",
                    "P17",
                    "P18",
                    "P19",
                    "SV1",
                    "SV2",
                    "SV3",
                    "SV4",
                    "SV5",
                    "SV6",
                    "SV7",
                    "SV8",
                ],
            },
            {
                "address": "D36STR9",
                "elevators": [
                    "L_A9",
                    "L_B9",
                    "L_C9",
                    "L_D9",
                    "L_GENERAL9",
                    "L_KOHONIE9",
                    "L_GRUZ19",
                    "L_GRUZ29",
                    "L_PARK9",
                ],
            },
            {
                "address": "D36STR10",
                "elevators": [
                    "L_A10",
                    "L_B10",
                    "L_C10",
                    "L_GRUZ10",
                    "L_PARK10",
                ],
            },
            {
                "address": "D36STR11",
                "elevators": [
                    "L_A11",
                    "L_B11",
                    "L_C11",
                    "L_GRUZ11",
                    "L_PARK11",
                    "L_KUHONIE11",
                ],
            },
            {
                "address": "D36STR28",
                "elevators": [
                    "OTIS_MUSEI",
                    "STEKLYANIE_MUSEI",
                ],
            },
            {
                "address": "D36STR41",
                "elevators": [
                    "L1",
                    "L2",
                    "L3",
                    "L4",
                    "L5",
                    "L6",
                    "L7",
                    "L8",
                    "L9",
                    "L10",
                    "L11",
                    "L12",
                    "L13",
                    "L14",
                    "L15",
                ],
            },
            {
                "address": "MSTK",
                "elevators": [
                    "MSTK_L1",
                ],
            },
        ]

        for building_data in buildings_data:
            address = building_data["address"]
            elevators = building_data["elevators"]

            # Создаем здание
            building, created = Building.objects.get_or_create(address=address)

            # Создаем лифты и связываем их с зданием
            for elevator_name in elevators:
                elevator, created = Elevator.objects.get_or_create(
                    elevator=elevator_name
                )
                building.elevators.add(elevator)

        self.stdout.write(
            self.style.SUCCESS("База данных успешно заполнена начальными данными")
        )

        # Создаем администратора
        username = "niky"
        password = os.getenv("POSTGRES_PASSWORD")
        email = "niky@example.com"  # Вы можете изменить email на любой другой

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(
                self.style.SUCCESS(f"Администратор {username} успешно создан")
            )
        else:
            self.stdout.write(
                self.style.WARNING(f"Администратор {username} уже существует")
            )

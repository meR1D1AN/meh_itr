import os
from pathlib import Path

from django.core.management.base import BaseCommand
from dotenv import load_dotenv

from esc.models import Esc, EscChoices
from lifts.models import AddressChoices, Building, Elevator, ElevatorChoices
from users.models import User


BASE_DIR = Path(__file__).resolve().parent.parent
dot_env = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path=dot_env)


class Command(BaseCommand):
    help = "Заполняет базу данных начальными данными"

    def handle(self, *args, **kwargs):
        # Данные для заполнения зданий и лифтов
        buildings_data = [
            {
                "address": AddressChoices.D36,
                "elevators": [
                    ElevatorChoices.P1,
                    ElevatorChoices.P2,
                    ElevatorChoices.P3,
                    ElevatorChoices.P4,
                    ElevatorChoices.P5,
                    ElevatorChoices.P6,
                    ElevatorChoices.P7,
                    ElevatorChoices.P8,
                    ElevatorChoices.P9,
                    ElevatorChoices.P12,
                    ElevatorChoices.P13,
                    ElevatorChoices.P14,
                    ElevatorChoices.P15,
                    ElevatorChoices.P16,
                    ElevatorChoices.P17,
                    ElevatorChoices.P18,
                    ElevatorChoices.P19,
                    ElevatorChoices.SV1,
                    ElevatorChoices.SV2,
                    ElevatorChoices.SV3,
                    ElevatorChoices.SV4,
                    ElevatorChoices.SV5,
                    ElevatorChoices.SV6,
                    ElevatorChoices.SV7,
                    ElevatorChoices.SV8,
                ],
            },
            {
                "address": AddressChoices.D36STR9,
                "elevators": [
                    ElevatorChoices.L_A9,
                    ElevatorChoices.L_B9,
                    ElevatorChoices.L_C9,
                    ElevatorChoices.L_D9,
                    ElevatorChoices.L_GENERAL9,
                    ElevatorChoices.L_KUHONIE9,
                    ElevatorChoices.L_GRUZ19,
                    ElevatorChoices.L_GRUZ29,
                    ElevatorChoices.L_PARK9,
                ],
            },
            {
                "address": AddressChoices.D36STR10,
                "elevators": [
                    ElevatorChoices.L_A10,
                    ElevatorChoices.L_B10,
                    ElevatorChoices.L_C10,
                    ElevatorChoices.L_GRUZ10,
                    ElevatorChoices.L_PARK10,
                ],
            },
            {
                "address": AddressChoices.D36STR11,
                "elevators": [
                    ElevatorChoices.L_A11,
                    ElevatorChoices.L_B11,
                    ElevatorChoices.L_C11,
                    ElevatorChoices.L_GRUZ11,
                    ElevatorChoices.L_PARK11,
                    ElevatorChoices.L_KUHONIE11,
                ],
            },
            {
                "address": AddressChoices.D36STR28,
                "elevators": [
                    ElevatorChoices.OTIS_MUSEI,
                    ElevatorChoices.STEKLYANIE_MUSEI,
                ],
            },
            {
                "address": AddressChoices.D36STR41,
                "elevators": [
                    ElevatorChoices.L1,
                    ElevatorChoices.L2,
                    ElevatorChoices.L3,
                    ElevatorChoices.L4,
                    ElevatorChoices.L5,
                    ElevatorChoices.L6,
                    ElevatorChoices.L7,
                    ElevatorChoices.L8,
                    ElevatorChoices.L9,
                    ElevatorChoices.L10,
                    ElevatorChoices.L11,
                    ElevatorChoices.L12,
                    ElevatorChoices.L13,
                    ElevatorChoices.L14,
                    ElevatorChoices.L15,
                ],
            },
            {
                "address": AddressChoices.MSTK,
                "elevators": [
                    ElevatorChoices.MSTK_L1,
                    ElevatorChoices.MSTK_L2,
                ],
            },
        ]

        # Заполняем базу данных
        for building_data in buildings_data:
            address = building_data["address"]
            elevators = building_data["elevators"]

            # Создаем здание или получаем его
            building, created = Building.objects.get_or_create(address=address)

            # Создаем лифты и связываем их со зданием
            for elevator_name in elevators:
                elevator, created = Elevator.objects.get_or_create(elevator=elevator_name)
                building.elevators.add(elevator)

        self.stdout.write(self.style.SUCCESS("База данных успешно заполнена начальными данными"))

        esc_data = [
            EscChoices.E11,
            EscChoices.E12,
            EscChoices.E13,
            EscChoices.E14,
            EscChoices.E15,
            EscChoices.E16,
            EscChoices.E21,
            EscChoices.E22,
            EscChoices.E23,
            EscChoices.E24,
            EscChoices.E25,
            EscChoices.E26,
            EscChoices.E31,
            EscChoices.E32,
            EscChoices.E33,
            EscChoices.E34,
            EscChoices.E35,
            EscChoices.E36,
            EscChoices.E41,
            EscChoices.E42,
            EscChoices.E43,
            EscChoices.E44,
            EscChoices.E45,
            EscChoices.E46,
            EscChoices.E51,
            EscChoices.E52,
            EscChoices.E53,
            EscChoices.E54,
            EscChoices.E55,
            EscChoices.E56,
            EscChoices.E61,
            EscChoices.E62,
            EscChoices.E63,
            EscChoices.E64,
            EscChoices.E71,
            EscChoices.E72,
            EscChoices.E73,
            EscChoices.E74,
            EscChoices.E81,
            EscChoices.E82,
            EscChoices.E91,
            EscChoices.E92,
        ]

        # Заполнение данных для эскалаторов
        for esc_name in esc_data:
            Esc.objects.get_or_create(esc=esc_name)

        self.stdout.write(self.style.SUCCESS("Данные для эскалаторов успешно добавлены"))

        # Создаем администратора
        email = os.getenv("ADMIN_EMAIL")
        password = os.getenv("ADMIN_PASSWORD")
        first_name = "Никита"
        last_name = "Шидогубов"
        middle_name = "Александрович"
        phone = "+79958873107"

        if not User.objects.filter(email=email).exists():
            User.objects.create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                middle_name=middle_name,
                phone=phone,
                is_staff=True,
                is_superuser=True,
                is_itr=True,
            )
            self.stdout.write(self.style.SUCCESS(f"Администратор {email} успешно создан"))
        else:
            self.stdout.write(self.style.WARNING(f"Администратор {email} уже существует"))

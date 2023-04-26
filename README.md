 Объект тестирования: https://b2c.passport.rt.ru
 
 Ссылка на документ, содержащий  тест-кейсы, баг-репорты: https://docs.google.com/spreadsheets/d/15BzMI6Eu1SNsjZib3K8ezpPCCeE66QIiZVXTBKm2k-I/edit?usp=sharing
 
 Применялись техники позитивного и негативного тестирования 
 
 
Base_class.py - базовые классы,локаторы для тестов;

Settings.py - авторизационные данные для позитивных тестов;

Tests.py - автотесты;
 
 Запуск автотестов командой из корневой директории проекта:  python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests.py

Объект тестирования: https://b2c.passport.rt.ru 
Применялись техники позитивного и негативного тестирования 
  
Base_class.py - базовые классы,локаторы для тестов;

Settings.py - авторизационные данные для позитивных тестов;

Tests.py - автотесты;
 
 Запуск автотестов командой из корневой директории проекта:  python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests.py

Объект тестирования: https://b2c.passport.rt.ru 

https://docs.google.com/spreadsheets/d/1Ke162E-bPWovZwVnaJjOCic8NqwutOBjTT5k8tfCzDs/edit?usp=sharing  - пример тест кейсов и БР

Применялись техники позитивного и негативного тестирования 
  
Base_class.py - базовые классы,локаторы для тестов;

Settings.py - авторизационные данные для позитивных тестов;

Tests.py - автотесты;
 
 Запуск автотестов командой из корневой директории проекта:  python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests.py

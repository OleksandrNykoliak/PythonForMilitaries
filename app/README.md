


1. Створити віртуалку

   ```
    py -m venv venv
   ```
2. Активувати

   ```
   venv\Scripts\activate
   ```
3. встановлюєте всі бібліотеки з файлу requirements.txt

   ```
   pip install -r requirements.txt
   ```
4. ```
   uvicorn main:app --reload
   ```

Обовязково ранимо postgres в docker

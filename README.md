Описание:
Приложение для распространения сообщений представляет собой систему на основе Python, состоящую из четырех модулей, которые вместе образуют универсальное решение для распространения сообщений. Каждый модуль играет определенную роль в процессе отправки сообщений, делая систему эффективной и масштабируемой. Ниже приведен обзор каждого модуля:

Модуль хранения: 
Модуль хранения служит очередью для отправки сообщений. Он реализован с использованием SQLite, легкой и эффективной реляционной базы данных. Модуль эффективно сохраняет сообщения в очереди, обеспечивая целостность данных и надежное хранение.

Интерфейс API: 
Модуль интерфейса API действует как универсальный интерфейс для взаимодействия с системой распространения сообщений. Он построен с использованием FastAPI, современного веб-фреймворка для Python, и SQLAlchemy, мощного и гибкого ORM. Этот модуль позволяет пользователям отправлять сообщения в очередь. Интерфейс API обеспечивает бесперебойную связь между пользователями и системой.

Веб-интерфейс: 
Модуль веб-интерфейса предоставляет удобный сервис для отображения очереди сообщений и различной статистики, связанной с отправленными сообщениями. Он реализован в Streamlit, платформе приложений с открытым исходным кодом для создания интерактивных веб-приложений. Веб-интерфейс позволяет пользователям визуализировать состояние системы распространения сообщений, облегчая мониторинг и устранение неполадок.

servis_mailing: 
Модуль servis_mailing отвечает за отправку сообщений из очереди получателям. Он использует smtplib, стандартный библиотечный модуль для отправки электронных писем по протоколу Simple Mail Transfer Protocol (SMTP). Эта служба эффективно извлекает сообщения из очереди и обеспечивает их надежную доставку предполагаемым получателям.

Основные характеристики:

Эффективное хранение очереди сообщений с использованием SQLite.
Универсальный интерфейс API с FastAPI и SQLAlchemy для беспрепятственного взаимодействия с пользователем.
Удобный веб-интерфейс с подсветкой потока для удобного мониторинга и визуализации статистики.
Надежная доставка сообщений с использованием smtplib для отправки электронных писем.
Использование: Приложение для рассылки сообщений подходит для сценариев, где требуется эффективная рассылка сообщений, таких как уведомления, оповещения и кампании по электронной почте. Его можно легко интегрировать в существующие системы и приложения через его интерфейс API.

Вклад: 
Вклад в проект приветствуется. Будь то исправления ошибок, новые функции или усовершенствования существующих модулей, ваш вклад может помочь улучшить приложение для рассылки сообщений.

Лицензия: 
Приложение для рассылки сообщений имеет открытый исходный код и выпущено под MIT. Пожалуйста, обратитесь к файлу ЛИЦЕНЗИИ для получения более подробной информации.

Отказ от ответственности: 
Приложение для рассылки сообщений предоставляется как есть, без каких-либо гарантий. Разработчики не несут ответственности за какие-либо проблемы или потерю данных, которые могут возникнуть во время его использования.

Для получения дополнительной информации и для начала работы с приложением рассылки сообщений, пожалуйста, обратитесь к соответствующему описаниям в приложениях для каждого модуля


Как запустить приложенее :

1. Скачать приложение : git clone https://github.com/oldkoteika/user_notification.git
2. Откройте свой интерфейс командной строки (например, командную строку в Windows, терминал в macOS и Linux).

3. Перейдите в каталог, в котором вы хотите создать виртуальную среду, используя cd команду. 

    cd /path/to/your/project


4. Проверьте версию Python, установленную в вашей системе, набрав:
    python --version

5. Создайте виртуальную среду с помощью venv. Виртуальную среду обычно называют "venv".:

    python -m venv venv

В некоторых системах может потребоваться использовать python3 вместо python явного указания Python 3.

6. Активируйте виртуальную среду. Команда активации варьируется в зависимости от вашей операционной системы:

    В Windows:
    venv\Scripts\activate

    На macOS и Linux:
    source venv/bin/activate

    Вы увидите название виртуальной среды (например, (venv)) в начале командной строки, указывающее, что виртуальная среда теперь активна.

7. Установите необходимые пакеты внутри виртуальной среды с помощью pip. 
    pip install -r requirements.txt

8. в консоли устанавливаем  PORT_API переменную среды для всех операционных систем, вы можете использовать следующие команды:

    В Windows (командная строка):
    set PORT_API=1055

    В Windows (PowerShell):
    $env:PORT_API=1055

    На macOS / Linux:
    export PORT_API=1055

Обратите внимание, что приведенные выше команды установят для PORT_API переменной среды значение 1055. Вы можете заменить 1055 желаемый номер порта, который хотите использовать. После установки переменной среды она будет доступна в текущем сеансе командной строки. Если вы хотите сделать ее доступной в будущих сеансах, возможно, потребуется добавить ее в конфигурацию переменных среды вашей системы.

9. Запускаем API  приложение : python Api_integration\main.py 

10. Переходим в браузер и проверяем что приложение запущено : http://localhost:1055/docs#/

11. Открываем еще один терминал с созданой виртуальной средой, в корневой папке 

12. Определяем переменные окружения:

    Email - почта от чьего имени будет отправлятся почта

    SMTP_server - URL почтового сервера

    SMTP_PORT - Порт почтового сервера

     password - пароль от почты для логирования

    В Windows (командная строка):
    set Email=your_email@example.com
    set SMTP_server=smtp.example.com
    set SMTP_PORT=587
    set password=your_email_password

    В Windows (PowerShell):
    $env:Email="your_email@example.com"
    $env:SMTP_server="smtp.example.com"
    $env:SMTP_PORT="587"
    $env:password="your_email_password"

    На macOS / Linux:
    export Email=your_email@example.com
    export SMTP_server=smtp.example.com
    export SMTP_PORT=587
    export password=your_email_password

14. запускаем приложение рассылки сообщений из очереди : python servis_mailing/main.py

15. Запускаем WEB портал для отслеживания очереди и статистики в 3-ем терминале с виртуальной средой : streamlit run web_Interface/1_📨_Email.py --server.port 1056

16. Проверяем что приложение работает :

    Переходим в API и и отправляем тестовое сообщение себе на почту

    Переходим в почту и смотрим, в течении 1 минуты должно прийти сообщение

    Переходим в http://localhost:1056 (Admin  Admin)  и смотрим что сообщение обработано в очереди.

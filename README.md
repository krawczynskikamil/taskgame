# Api aplikacji do zarządzania zadaniami TaskGame

## Konfiguracja dockera

docker-compose up --build

## Adresy do zalogowania i wylogowania

http://localhost:8000/auth/login/

http://localhost:8000/auth/logout/

## Dodawanie Tasków

W "Recurrence" należy podać reguły występowania dat wg RFC 5545 poprzedzając ją "RRULE:" np.
   \
RRULE:FREQ=MONTHLY;BYMONTHDAY=1;INTERVAL=3;UNTIL=20230827T000000Z
   \<br />
Generowanie reguł na stronie
   \
https://freetools.textmagic.com/rrule-generator
   \

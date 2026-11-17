# 16. Go и backend (дополнение к исходному frontend-набору)

Применять для Go/HTTP/SQL-проектов при наличии соответствующего стека.

- Уважайте контракты: HTTP status, JSON schema, pagination, Request-ID, rate limit и authz. Ошибка клиента не должна выглядеть как success.
- Явно обрабатывайте `error`, используйте `errors.Is`/`errors.As` и контекст, не скрывайте причину через `panic`/`recover` без технической необходимости.
- Прокидывайте `context.Context` и учитывайте cancellation, deadlines, ресурсные лимиты.
- Для конкурентных операций проверяйте data races (`go test -race` где доступно), lock scope, идемпотентность и SQL-инварианты в реальном PostgreSQL.
- Unit: `go test ./...` по scope; integration: отдельная тестовая БД, миграции и реальные HTTP handlers; fuzz: `go test -fuzz` на парсерах/десериализации/нормализации с подходящим временем и seed.
- Подтверждайте, что `429` (rate limit) не является доказательством deduplication; проверяйте число строк и side effects в БД.
- Сохраняйте приватность логов и ограничивайте трассировку; не используйте production credentials.
- Тестовые fixture должны соответствовать всем security/audit инвариантам, а не обходить их при падении теста.

Критические сценарии (JWT, outbox, notifications, миграции) тестируйте с negative cases и ограниченными ожиданиями, избегая произвольных sleeps.

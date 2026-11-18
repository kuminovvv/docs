# Backend: проверка Go-сервисов

- Unit: `go test ./...` по scope; интеграция: отдельная тестовая БД, миграции и реальные HTTP handlers.
- При изменении конкурентного кода проверяйте гонки через `go test -race` там, где это возможно.
- Fuzz: `go test -fuzz` на парсерах, десериализации и нормализации с подходящим временем и сохранённым seed.
- Для JWT, outbox, notifications и миграций проверяйте negative cases, таймауты и реальные SQL-инварианты; избегайте произвольных `sleep`.
- Тестовые fixtures должны удовлетворять security/audit-инвариантам и не подменять их обходами.
- `SKIP`, `SETUP_FAILURE`, таймаут или недоступная PostgreSQL — не `PASS`.

Общие правила: [верификация](09-testing-and-verification.md), [E2E/property/differential](12-verification-techniques.md), [review и gates](13-review-and-gates.md).

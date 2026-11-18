# Go: ошибки, контекст и конкурентность

Применять для Go/HTTP/SQL-проектов при наличии соответствующего стека.

- Явно обрабатывайте `error`, используйте `errors.Is`/`errors.As` и контекст, не скрывайте причину через `panic`/`recover` без технической необходимости.
- Прокидывайте `context.Context` и учитывайте cancellation, deadlines, ресурсные лимиты.
- Для конкурентных операций проверяйте data races (`go test -race`, где доступно), lock scope, идемпотентность и SQL-инварианты в реальном PostgreSQL.

Смежные правила: [HTTP API](api-contracts.md), [данные](data-integrity.md), [тестирование](testing.md).

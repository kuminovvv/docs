# Backend — правила для Go, HTTP API и PostgreSQL

Применяйте **при соответствующем стеке и фактическом scope задачи**. Не считайте PostgreSQL, JWT, outbox или другие сервисы обязательными для любого backend.

| Документ | Содержание |
| --- | --- |
| [go.md](go.md) | Go: ошибки, context, конкурентность |
| [api-contracts.md](api-contracts.md) | HTTP API, статусы, JSON, авторизация |
| [data-integrity.md](data-integrity.md) | PostgreSQL, транзакции, идемпотентность, миграции |
| [testing.md](testing.md) | Go unit/integration/race/fuzz, негативные сценарии |
| [observability.md](observability.md) | Логи, Request-ID, privacy |

Общие правила применяются дополнительно: [выполнение задачи](02-task-workflow.md), [верификация](09-testing-and-verification.md), [безопасность](14-security-and-privacy.md), [review](13-review-and-gates.md).

Документы по backend не являются архитектурным шаблоном и не заменяют профиль реального проекта.

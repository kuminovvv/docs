# Навигация по правилам

Начните с [`../AGENTS.md`](../AGENTS.md). Затем откройте только нужные разделы.

## Общие правила для любого стека

| Документ | Область |
| --- | --- |
| [00-overview.md](00-overview.md) | Модель правил, приоритеты, статусы |
| [01-context-loading.md](01-context-loading.md) | Поиск релевантного контекста |
| [02-task-workflow.md](02-task-workflow.md) | План, критерии, фиксация результатов |
| [09-testing-and-verification.md](09-testing-and-verification.md) | Доказательства корректности |
| [10-git-and-delivery.md](10-git-and-delivery.md) | Git, коммиты, границы релиза |
| [12-verification-techniques.md](12-verification-techniques.md) | E2E, property, differential |
| [13-review-and-gates.md](13-review-and-gates.md) | Gate, review, CI, fail-closed |
| [14-security-and-privacy.md](14-security-and-privacy.md) | Безопасность и ПДн |
| [15-project-overrides.md](15-project-overrides.md) | Применение правил к проекту |

## Правила по направлениям

- **Frontend:** [frontend/README.md](frontend/README.md) — FSD, React, TypeScript, Next.js, performance, UI и ошибки.
- **Backend:** [backend/README.md](backend/README.md) — Go, API, БД, конкурентность, тестирование и логи.

**Шаблоны:** [профиль проекта](templates/project-profile.md), [отчёт о проверке](templates/verification-report.md).

Для frontend-задач сначала открывайте frontend-раздел и подходящие общие правила; для backend-задач — backend-раздел и общие правила. Не навязывайте документы одного стека другому. При изменении контракта между frontend и backend проверяйте обе стороны.

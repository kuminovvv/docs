# Навигация по правилам

Начните с [`../AGENTS.md`](../AGENTS.md). Затем откройте только нужные разделы:

| Файл | Область |
| --- | --- |
| [00-overview.md](00-overview.md) | Модель правил, приоритеты и статусы |
| [01-context-loading.md](01-context-loading.md) | Поиск релевантного контекста |
| [02-task-workflow.md](02-task-workflow.md) | План, критерии, фиксация результатов |
| [03-fsd.md](03-fsd.md) | Feature-Sliced Design (если применяется) |
| [04-components.md](04-components.md) | React-компоненты и типы |
| [05-typescript.md](05-typescript.md) | TypeScript-контракты |
| [06-nextjs.md](06-nextjs.md) | Next.js 16 / App Router |
| [07-performance.md](07-performance.md) | Профилирование и оптимизация |
| [08-error-handling.md](08-error-handling.md) | Ошибки и наблюдаемость |
| [09-testing-and-verification.md](09-testing-and-verification.md) | Доказательства корректности |
| [10-git-and-delivery.md](10-git-and-delivery.md) | Git, Conventional Commits, границы релиза |
| [11-ui-context-risks.md](11-ui-context-risks.md) | UI-паритет, состояния, черновики |
| [12-verification-techniques.md](12-verification-techniques.md) | E2E/property/differential |
| [13-review-and-gates.md](13-review-and-gates.md) | Gate, review, CI, fail-closed |
| [14-security-and-privacy.md](14-security-and-privacy.md) | Безопасность и ПДн |
| [15-project-overrides.md](15-project-overrides.md) | Применение и приоритет проектных правил |
| [16-go-and-backend.md](16-go-and-backend.md) | Go, API, PostgreSQL, гонки |

**Рабочие шаблоны:** [профиль проекта](templates/project-profile.md), [отчёт о проверке](templates/verification-report.md).

Для frontend-задачи начинайте с 04–06, для изменения UX — 11, для изменения API/БД — 14 и 16, для релизов — 09, 10 и 13. Для мелкой правки текста запуск приложения необязателен, но факт отсутствия проверки не маскируется.

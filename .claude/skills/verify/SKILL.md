---
name: verify
description: Verify changes in the actual target application with reproducible evidence, using project-specific commands and risk-based E2E/property/differential checks before committing.
---

# Verify skill — проектный шаблон

Перед применением выберите `docs/frontend/AGENTS.md` или `docs/backend/AGENTS.md` по scope задачи, затем прочитайте `docs/09-testing-and-verification.md`,
`docs/12-verification-techniques.md`, `docs/13-review-and-gates.md` и локальный `docs/project-profile.md` (если он есть).

1. Установите task acceptance criteria и точный scope; проверьте Git status/SHA и запрещённые пути.
2. Возьмите **реальные** команды из `package.json`, `go.mod`, Makefile, CI и project-profile. Не выдумывайте `npm test` или адрес dev-сервера.
3. Поднимите приложение/сервис и изолированные тестовые зависимости, если это безопасно и доступно; никогда не используйте production DB без отдельной авторизации.
4. Выполните быстрые детерминированные checks, затем один или больше необходимых E2E flows. Для миграций — differential; для инвариантов — property/fuzz.
5. Зафиксируйте command + exit code, environment, seed, artifacts, точный SHA; при снимках и trace удалите ПДн и secrets.
6. Если обязательная проверка невозможна, пометьте BLOCKED; при нестабильности — FLAKY; не объявляйте PASS.
7. Сравните diff и security/CI gates с защищённой baseline. Не меняйте тест ради прохождения проверки без отдельного ревью.
8. Перед коммитом выдайте отчёт по `docs/templates/verification-report.md`.

Этот файл — **процесс, а не автоматически исполняемый скрипт**. Для механической гарантии добавьте проектный harness и required CI checks.

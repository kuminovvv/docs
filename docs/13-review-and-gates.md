# 13. Review, gates и проверяемые доказательства

## Принципы

1. **Проверка относится к точному SHA**, а не к ветке, которая может измениться в процессе проверки.
2. Reviewer использует правила и baseline **из базовой/защищённой ветки**, а не изменённую проверяемым diff конфигурацию.
3. Владелец кода определяет инварианты и риск-критерии; агент помогает автоматизировать. Самопроверка автора — не независимое ревью.
4. Критические security/privacy, migration/data-integrity, required CI checks, auth tests должны **fail-closed**: нельзя автоматически разрешить commit/release после N блокировок.
5. `SKIP`, flaky, timeout и setup failure дают статус не-подтверждено; workflow не интерпретирует их как PASS.

## Diff-triggered review

Для каждого инцидентного правила храните: **trigger (по diff)** → **check** → **evidence** → **source incident**. Примеры:

| Триггер | Проверка |
| --- | --- |
| auth/session/JWT | replay, expiry, rotation, CSRF, 401/403, refresh |
| изменение API payload | backcompat, validation, unknown fields, consumer contract |
| migration/SQL | fresh/upgraded schema, rollback strategy, isolation, idempotency |
| UI interactive | E2E happy/negative, keyboard, read-only/auth parity |
| cache/SSR | stale/private data, direct refresh, cross-user leakage |
| retry/outbox/SSE | duplicate delivery, ordered state, recovery, reconnect |
| verifier/CI | baseline comparison, failure injection, skip/fail closed |
| network/SDK/vendor | data egress and privacy gate |

Выполняйте подходящие проверки; при высоком риске добавляйте baseline независимо от trigger. Изменение списка triggers само требует отдельного ревью.

## Порядок внедрения gate

`off` → `observe` (собрать false positives и стоимость) → `enforce` (закрепить в защищённой CI-конфигурации). Для опасных изменений новые gates могут потребовать ручного решения владельца до допуска, а не автоматического waiver.

## Эскалация

После **трёх содержательных раундов** попыток устранить один и тот же FAIL остановитесь, сохраните воспроизведение и передайте человеку. Три раунда — практика команды Claude Code, не гарантия и не основание пропускать тест.

## Инциденты и поддержка правил

Подтверждённые повторяющиеся нарушения превращайте в короткие diff-triggered проверки, регрессионные тесты и проектный lessons log. Периодически удаляйте устаревшие правила; проверяйте, что reviewer действительно ловит известные баги и не создаёт шум.

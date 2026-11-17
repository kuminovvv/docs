# 11. Риски UI-контекста

Перед изменением экрана определите конкретное расположение, viewport, состояние и аудиторию. Слова «сюда», «ниже», «рядом» без осмотра фактического UI не дают достаточной спецификации.

- Для read-only / auth-gated состояний проверяйте parity: click, drag-drop, keyboard shortcut, action button, retry должны вести в ожидаемые сценарии (в том числе sign-in gate).
- Если авторизация прерывает ввод, сохраните разрешённый объём черновика (text/media), с явным scope/TTL; восстановление тестируйте, не переносите приватные данные между аккаунтами.
- Для popover/tooltip/modal используйте существующие shared компоненты. Не заменяйте управляемый tooltip HTML `title`, если это ломает UX.
- Проверяйте keyboard, focus, accessibility, overlay, scroll locking, mobile keyboard и no-JS/slow-network states по релевантности.
- UI correctness лучше доказывается E2E с trace/screenshot/video и проверкой исходного ожидания, чем скриншотом без interaction.

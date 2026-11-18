# Backend: HTTP API и контракты

- Уважайте контракты: HTTP status, JSON schema, pagination, Request-ID, rate limit и authz.
- Ошибка клиента не должна выглядеть как success. Различайте transport failure, HTTP/API error, validation error, authorization error и unsupported state.
- Подтверждайте, что `429` (rate limit) не является доказательством deduplication; проверяйте число строк и side effects в БД, когда важна идемпотентность.
- AuthN/AuthZ выполняются на сервере: требования к RBAC, ownership, IDOR и CSRF изложены в [общем документе безопасности](14-security-and-privacy.md).

При изменении контрактов используйте [риск-ориентированные проверки](12-verification-techniques.md).

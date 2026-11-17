# 06. Next.js 16 / App Router

Применимо, только если проект действительно использует Next.js 16 с App Router.

## Границы сервера и клиента

- В App Router компоненты по умолчанию серверные, **если не находятся под клиентской границей**. Само размещение в `src/` не делает файл Server Component.
- `'use client'` размещайте в точке входа интерактивного поддерева, не размечайте им без необходимости каждый hook/helper. Но client-only модуль нельзя импортировать серверным образом без проверки.
- Данные через Server → Client границу должны быть сериализуемыми; callback из клиентского родителя в клиентского ребёнка разрешён. Название с `Action` не разрешает пересечь границу с произвольной функцией.
- Server Actions/Functions должны проверять **авторизацию на каждую мутацию** (роль, ownership, scope), валидировать вход и не считать скрытую кнопку защитой.

## Routing и API

- `page.tsx`/`layout.tsx` используют `default export`, если этого требует соглашение Next.js. Общее правило именованных экспортов на них не распространяется.
- Для динамических маршрутов в Next.js 16 `params` и, где применимо, `searchParams` — промисы: `const { slug } = await params`.
- Не смешивайте cache policy, auth/session data и публичные данные. Проверьте режим кеширования для каждого чувствительного ответа.
- Соблюдайте принятый в проекте error/loading/not-found UI и сохранение URL/state при навигации.

```tsx
export default async function Page({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const [channel, posts] = await Promise.all([fetchChannel(slug), fetchChannelPosts(slug)]);
  return <ChannelScreen channel={channel} posts={posts} />;
}
```

## Производительность

- Независимые серверные операции можно запускать через `Promise.all`, если они не требуют последовательности и не создают побочных эффектов.
- `React.cache()` полезен для request-scoped дедупликации серверных вычислений, но не заменяет работу с авторизацией и cache invalidation.
- `Suspense` — для оправданных streaming boundaries с осмысленным fallback.
- `next/dynamic(..., { ssr: false })` **используется внутри Client Component**, не напрямую в Server Component.
- Опции `next.config` и оптимизацию импортов сверяйте с текущей версией Next.js, не копируйте устаревшие `experimental`-флаги.

Источники: https://nextjs.org/docs/app/api-reference/directives/use-client ; https://nextjs.org/docs/app/api-reference/file-conventions/page ; https://nextjs.org/docs/app/guides/lazy-loading

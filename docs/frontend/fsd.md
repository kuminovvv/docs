# 03. Feature-Sliced Design (если проект использует FSD)

Направление зависимостей снизу вверх: `shared` → `entities` → `features` → `widgets` → `pages` → `app`. Внутри слайса слои определяются архитектурой конкретного проекта; модуль не импортирует зависимость с верхнего слоя. Между разными слайсами одного слоя обычные импорты запрещены (исключения — явно задокументированные архитектурные правила).

Для Next.js App Router файловые маршруты в `app/` или `src/app/` (по принятому расположению) должны оставаться тонкими composition-слоями; не предполагается одновременно два независимых app-root. Доменная композиция размещается в соответствующих слайсах, если это принято проектом.

```ts
// src/features/checkout/ui/CheckoutForm.tsx
import { Button } from '@/shared/ui';  // допустим импорт нижележащего слоя
import { Product } from '@/entities/product';

// Плохой пример: src/entities/product/ui/ProductCard.tsx
// import { CheckoutForm } from '@/features/checkout'; // верхний слой
```

- Публичная точка входа слайса — `index.ts`/`index.tsx`, если проект не выбрал другую политику.
- Не импортируйте внутренние файлы другого слайса deep-import'ом в обход API.
- Не создавайте фиктивные slices, layers или обёртки без полезной ответственности.

Источник: https://feature-sliced.design/docs/reference/layers

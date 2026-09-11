[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/iteration](../index.md) / IterationUsage

# Type Alias: IterationUsage

> **IterationUsage** = `object`

Defined in: [ui/src/api-shared/types/iteration.ts:86](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/iteration.ts#L86)

What an iteration still owns, as reported by `GET /api/iterations/[id]/usage`.
Drives the delete affordance (#473) — only an orphaned iteration is deletable.

## Properties

### curriculums

> **curriculums**: `number`

Defined in: [ui/src/api-shared/types/iteration.ts:88](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/iteration.ts#L88)

1 when a Gantt curriculum is linked, 0 otherwise.

***

### events

> **events**: `number`

Defined in: [ui/src/api-shared/types/iteration.ts:90](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/iteration.ts#L90)

Capped existence probe over the iteration's events (0 or 1).

***

### isCurrent

> **isCurrent**: `boolean`

Defined in: [ui/src/api-shared/types/iteration.ts:91](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/iteration.ts#L91)

***

### orphaned

> **orphaned**: `boolean`

Defined in: [ui/src/api-shared/types/iteration.ts:92](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/iteration.ts#L92)

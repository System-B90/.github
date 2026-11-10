[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/types/EventUtils](../index.md) / DIFF\_IGNORED\_KEYS

# Variable: DIFF\_IGNORED\_KEYS

> `const` **DIFF\_IGNORED\_KEYS**: `ReadonlySet`\<`string`\>

Defined in: [ui/src/components/schedule/types/EventUtils.ts:132](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/schedule/types/EventUtils.ts#L132)

Write bookkeeping, not content: `updatedAt` is re-stamped on every save, so
a copy re-saved with identical fields would otherwise read as changed and
flag a conflict.

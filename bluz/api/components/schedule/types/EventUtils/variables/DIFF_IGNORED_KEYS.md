[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/types/EventUtils](../index.md) / DIFF\_IGNORED\_KEYS

# Variable: DIFF\_IGNORED\_KEYS

> `const` **DIFF\_IGNORED\_KEYS**: `ReadonlySet`\<`string`\>

Defined in: [ui/src/components/schedule/types/EventUtils.ts:132](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/schedule/types/EventUtils.ts#L132)

Write bookkeeping, not content: `updatedAt` is re-stamped on every save, so
a copy re-saved with identical fields would otherwise read as changed and
flag a conflict.

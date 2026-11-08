[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/types/EventUtils](../index.md) / DIFF\_IGNORED\_KEYS

# Variable: DIFF\_IGNORED\_KEYS

> `const` **DIFF\_IGNORED\_KEYS**: `ReadonlySet`\<`string`\>

Defined in: [ui/src/components/schedule/types/EventUtils.ts:132](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/types/EventUtils.ts#L132)

Write bookkeeping, not content: `updatedAt` is re-stamped on every save, so
a copy re-saved with identical fields would otherwise read as changed and
flag a conflict.

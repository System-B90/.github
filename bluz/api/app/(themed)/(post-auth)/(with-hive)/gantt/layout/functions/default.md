[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [app/(themed)/(post-auth)/(with-hive)/gantt/layout](../index.md) / default

# Function: default()

> **default**(`__namedParameters`): `Promise`\<`Element`\>

Defined in: [ui/src/app/(themed)/(post-auth)/(with-hive)/gantt/layout.tsx:11](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/app/(themed)/(post-auth)/(with-hive)/gantt/layout.tsx#L11)

The gantt is staff-only: a Checker (read-only schedule viewer) is sent back
to the schedule. Not a data gate — every gantt API refuses a Checker on its
own (`requireStaffAuth`, `proxy.ts`) — just keeps it off a page it cannot use.

## Parameters

### \_\_namedParameters

`Readonly`\<\{ `children`: `React.ReactNode`; \}\>

## Returns

`Promise`\<`Element`\>

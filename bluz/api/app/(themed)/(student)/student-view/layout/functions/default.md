[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [app/(themed)/(student)/student-view/layout](../index.md) / default

# Function: default()

> **default**(`__namedParameters`): `Promise`\<`Element`\>

Defined in: [ui/src/app/(themed)/(student)/student-view/layout.tsx:16](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/app/(themed)/(student)/student-view/layout.tsx#L16)

The student view sits *outside* the `(post-auth)` group on purpose: that
group's layout mounts the staff shell (app bar, command palette, Hive
providers, settings dialog, onboarding) and bounces non-staff away from it.
This layout mounts none of that — a student session has no staff React tree
to inspect, and nothing on the page suggests one exists (#656).

Both staff and students may render this route: staff use it as the preview.

## Parameters

### \_\_namedParameters

`Readonly`\<\{ `children`: `React.ReactNode`; \}\>

## Returns

`Promise`\<`Element`\>

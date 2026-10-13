[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [app/(themed)/(student)/student-view/layout](../index.md) / default

# Function: default()

> **default**(`__namedParameters`): `Promise`\<`Element`\>

Defined in: [ui/src/app/(themed)/(student)/student-view/layout.tsx:19](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/app/(themed)/(student)/student-view/layout.tsx#L19)

The student view sits *outside* the `(post-auth)` group on purpose: that
group's layout mounts the staff shell (app bar, command palette, Hive
providers, settings dialog, onboarding) and bounces non-staff away from it.
This layout mounts none of that — a student session has no staff React tree
to inspect, and nothing on the page suggests one exists (#656).

Both staff and students may render this route: staff use it as the preview.
Students only get the pink toggle when the deployment enables it (#765).

## Parameters

### \_\_namedParameters

`Readonly`\<\{ `children`: `React.ReactNode`; \}\>

## Returns

`Promise`\<`Element`\>

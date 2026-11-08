[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [app/(themed)/(student)/student-view/layout](../index.md) / default

# Function: default()

> **default**(`__namedParameters`): `Promise`\<`Element`\>

Defined in: [ui/src/app/(themed)/(student)/student-view/layout.tsx:19](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/app/(themed)/(student)/student-view/layout.tsx#L19)

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

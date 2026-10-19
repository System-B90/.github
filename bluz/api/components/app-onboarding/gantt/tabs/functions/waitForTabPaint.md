[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/app-onboarding/gantt/tabs](../index.md) / waitForTabPaint

# Function: waitForTabPaint()

> **waitForTabPaint**(): `Promise`\<`void`\>

Defined in: [ui/src/components/app-onboarding/gantt/tabs.ts:23](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/app-onboarding/gantt/tabs.ts#L23)

Tab content mounts a couple of frames after the tab changes (the tab strip
defers the first mount so the switch animates), so a tour step that points
into a freshly-opened tab has to let those frames pass before its anchor can
possibly exist.

## Returns

`Promise`\<`void`\>

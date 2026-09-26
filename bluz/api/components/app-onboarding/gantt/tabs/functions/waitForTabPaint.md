[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/app-onboarding/gantt/tabs](../index.md) / waitForTabPaint

# Function: waitForTabPaint()

> **waitForTabPaint**(): `Promise`\<`void`\>

Defined in: [ui/src/components/app-onboarding/gantt/tabs.ts:22](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/app-onboarding/gantt/tabs.ts#L22)

Tab content mounts a couple of frames after the tab changes (the tab strip
defers the first mount so the switch animates), so a tour step that points
into a freshly-opened tab has to let those frames pass before its anchor can
possibly exist.

## Returns

`Promise`\<`void`\>

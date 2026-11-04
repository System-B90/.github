[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/curriculum-view/components/insights/dismiss](../index.md) / INSIGHTS\_DISMISS\_KEY

# Variable: INSIGHTS\_DISMISS\_KEY

> `const` **INSIGHTS\_DISMISS\_KEY**: `"bluz.gantt.insights.dismissedUntil"` = `"bluz.gantt.insights.dismissedUntil"`

Defined in: [ui/src/components/gantt/curriculum-view/components/insights/dismiss.ts:8](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/gantt/curriculum-view/components/insights/dismiss.ts#L8)

Session-scoped "dismiss for an hour" for the gantt insights card (#854).

Browser-only, no DB: one timestamp in `sessionStorage`. Another tab or a new
session shows the card again, which is fine for a QoL toggle.

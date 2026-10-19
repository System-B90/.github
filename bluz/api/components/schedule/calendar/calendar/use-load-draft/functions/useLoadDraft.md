[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/use-load-draft](../index.md) / useLoadDraft

# Function: useLoadDraft()

> **useLoadDraft**(): (`draftId`) => `Promise`\<\{ `eventCount`: `number`; `label`: `string`; \}\>

Defined in: [ui/src/components/schedule/calendar/calendar/use-load-draft.ts:18](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/schedule/calendar/calendar/use-load-draft.ts#L18)

Opens a shared draft for editing (#62). A draft is by definition not
deployed, so opening one enters offline mode: the server's events for the
draft's range become the baseline, the draft's events are shown in their
place and every edit stays local. Leaving offline mode then offers to
publish the difference, save it back to a draft, or discard it.

## Returns

Loads the draft; resolves to its label and event count.

(`draftId`) => `Promise`\<\{ `eventCount`: `number`; `label`: `string`; \}\>

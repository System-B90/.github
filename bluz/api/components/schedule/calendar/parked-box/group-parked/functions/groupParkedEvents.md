[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/parked-box/group-parked](../index.md) / groupParkedEvents

# Function: groupParkedEvents()

> **groupParkedEvents**(`events`, `rank`, `nameOf`): [`ParkedGroup`](../type-aliases/ParkedGroup.md)[]

Defined in: [ui/src/components/schedule/calendar/parked-box/group-parked.ts:20](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/schedule/calendar/parked-box/group-parked.ts#L20)

Groups parked events by subject (#981). Groups follow the subjects' order
in the gantt; subjects the gantt doesn't rank come after, by name, and
events without a subject come last. Inside a group, events keep the order
they had on the schedule.

## Parameters

### events

readonly [`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)[]

### rank

`ReadonlyMap`\<`number`, `number`\>

Subject id → position in the gantt.

### nameOf

(`subjectId`) => `string` \| `undefined`

Subject display name, when known.

## Returns

[`ParkedGroup`](../type-aliases/ParkedGroup.md)[]

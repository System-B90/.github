[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/parked-box/group-parked](../index.md) / groupParkedEvents

# Function: groupParkedEvents()

> **groupParkedEvents**(`events`, `rank`, `nameOf`): [`ParkedGroup`](../type-aliases/ParkedGroup.md)[]

Defined in: [ui/src/components/schedule/calendar/parked-box/group-parked.ts:20](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/schedule/calendar/parked-box/group-parked.ts#L20)

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

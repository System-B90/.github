[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/event-dialog/event-history/initiator-presentation](../index.md) / presentationFor

# Function: presentationFor()

> **presentationFor**(`initiator`): [`InitiatorPresentation`](../type-aliases/InitiatorPresentation.md)

Defined in: [ui/src/components/schedule/event-dialog/event-history/initiator-presentation.tsx:128](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/schedule/event-dialog/event-history/initiator-presentation.tsx#L128)

Icon + color for an initiator, falling back to a neutral "unknown" marker
so a value added server-side still renders.

## Parameters

### initiator

[`EventChangeInitiator`](../../../../../../api-shared/types/event-history/enumerations/EventChangeInitiator.md)

The recorded initiator of a change.

## Returns

[`InitiatorPresentation`](../type-aliases/InitiatorPresentation.md)

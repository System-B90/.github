[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/event-dialog/event-history/initiator-presentation](../index.md) / presentationFor

# Function: presentationFor()

> **presentationFor**(`initiator`): [`InitiatorPresentation`](../type-aliases/InitiatorPresentation.md)

Defined in: [ui/src/components/schedule/event-dialog/event-history/initiator-presentation.tsx:113](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/schedule/event-dialog/event-history/initiator-presentation.tsx#L113)

Icon + colour for an initiator, falling back to a neutral "unknown" marker
so a value added server-side still renders.

## Parameters

### initiator

[`EventChangeInitiator`](../../../../../../api-shared/types/event-history/enumerations/EventChangeInitiator.md)

The recorded initiator of a change.

## Returns

[`InitiatorPresentation`](../type-aliases/InitiatorPresentation.md)

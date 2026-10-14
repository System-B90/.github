[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/event-dialog/event-history/initiator-presentation](../index.md) / presentationFor

# Function: presentationFor()

> **presentationFor**(`initiator`): [`InitiatorPresentation`](../type-aliases/InitiatorPresentation.md)

Defined in: [ui/src/components/schedule/event-dialog/event-history/initiator-presentation.tsx:128](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/schedule/event-dialog/event-history/initiator-presentation.tsx#L128)

Icon + colour for an initiator, falling back to a neutral "unknown" marker
so a value added server-side still renders.

## Parameters

### initiator

[`EventChangeInitiator`](../../../../../../api-shared/types/event-history/enumerations/EventChangeInitiator.md)

The recorded initiator of a change.

## Returns

[`InitiatorPresentation`](../type-aliases/InitiatorPresentation.md)

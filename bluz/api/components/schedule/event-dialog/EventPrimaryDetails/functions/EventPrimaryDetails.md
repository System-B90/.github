[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-dialog/EventPrimaryDetails](../index.md) / EventPrimaryDetails

# Function: EventPrimaryDetails()

> **EventPrimaryDetails**(`__namedParameters`): `Element`

Defined in: [ui/src/components/schedule/event-dialog/EventPrimaryDetails.tsx:23](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/event-dialog/EventPrimaryDetails.tsx#L23)

## Parameters

### \_\_namedParameters

#### event

`Partial`\<[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)\>

#### isContentReady

`boolean`

False while the dialog opens: everything but the name field is a
skeleton of its own size, and the name stays live so typing right away
still lands in it (see EventDialog).

#### onUpdate

(`u`) => `void`

## Returns

`Element`

[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/week-template-cut](../index.md) / TemplateMatchTarget

# Type Alias: TemplateMatchTarget

> **TemplateMatchTarget** = `object`

Defined in: [ui/src/api-server/gantt/week-template-cut.ts:29](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-server/gantt/week-template-cut.ts#L29)

What the cut needs to know about a gantt event to match it (#997).

## Properties

### courseNames

> **courseNames**: `string`[]

Defined in: [ui/src/api-server/gantt/week-template-cut.ts:34](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-server/gantt/week-template-cut.ts#L34)

Its shuffles and courses (with their ancestors), by name.

***

### daily?

> `optional` **daily?**: `boolean`

Defined in: [ui/src/api-server/gantt/week-template-cut.ts:39](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-server/gantt/week-template-cut.ts#L39)

Recurs every day. One template placement then stands for every weekday
the template does not place it on itself.

***

### eventId

> **eventId**: `string`

Defined in: [ui/src/api-server/gantt/week-template-cut.ts:30](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-server/gantt/week-template-cut.ts#L30)

***

### names

> **names**: `string`[]

Defined in: [ui/src/api-server/gantt/week-template-cut.ts:32](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-server/gantt/week-template-cut.ts#L32)

Every name the event may carry: its gantt title and its cut name.

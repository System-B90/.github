[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/gantt/schema/event-recurrence-exceptions](../index.md) / ganttEventRecurrenceExceptionsSchema

# Variable: ganttEventRecurrenceExceptionsSchema

> `const` **ganttEventRecurrenceExceptionsSchema**: `PgTableWithColumns`\<\{ \}\>

Defined in: [ui/src/api-server/gantt/schema/event-recurrence-exceptions.ts:14](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/gantt/schema/event-recurrence-exceptions.ts#L14)

Drizzle database schema definition for the Gantt Event Recurrence Exceptions
table ("eRE"). A row means: within this curriculum, the recurring event no
longer echoes an occurrence onto this day — either the occurrence was
deleted outright, or it was materialized into its own standalone event.

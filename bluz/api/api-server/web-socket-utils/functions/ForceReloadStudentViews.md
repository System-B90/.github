[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/web-socket-utils](../index.md) / ForceReloadStudentViews

# Function: ForceReloadStudentViews()

> **ForceReloadStudentViews**(): `void`

Defined in: [ui/src/api-server/web-socket-utils.ts:245](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/api-server/web-socket-utils.ts#L245)

Staff "push update": every open student board reloads the whole page.

Payload-free like [NotifyStudentsOfCalendarChange](NotifyStudentsOfCalendarChange.md), and on the same
channel, so it inherits every guarantee that channel has. Unlike that ping
it is not tied to an iteration — it reloads the page, not the data.

## Returns

`void`

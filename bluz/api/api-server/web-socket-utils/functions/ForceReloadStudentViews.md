[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/web-socket-utils](../index.md) / ForceReloadStudentViews

# Function: ForceReloadStudentViews()

> **ForceReloadStudentViews**(): `void`

Defined in: [ui/src/api-server/web-socket-utils.ts:245](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/web-socket-utils.ts#L245)

Staff "push update": every open student board reloads the whole page.

Payload-free like [NotifyStudentsOfCalendarChange](NotifyStudentsOfCalendarChange.md), and on the same
channel, so it inherits every guarantee that channel has. Unlike that ping
it is not tied to an iteration — it reloads the page, not the data.

## Returns

`void`

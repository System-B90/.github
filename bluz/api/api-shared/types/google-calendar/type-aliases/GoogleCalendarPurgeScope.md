[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/google-calendar](../index.md) / GoogleCalendarPurgeScope

# Type Alias: GoogleCalendarPurgeScope

> **GoogleCalendarPurgeScope** = `"all"` \| `"orphaned"`

Defined in: [ui/src/api-shared/types/google-calendar.ts:123](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-shared/types/google-calendar.ts#L123)

`orphaned`: remove Bluz-tagged Google events whose Bluz event no longer
exists, belongs to another iteration than the calendar's, or no longer
falls within any linked user's sync scope.
`all`: remove every Bluz-tagged event from the calendar.
Events created by hand in Google are never touched either way.

[**TypeDoc API**](../../index.md)

***

[TypeDoc API](../../index.md) / [settings](../index.md) / MessageTypes

# Enumeration: MessageTypes

Defined in: [session-server/session-common.ts:31](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/session-server/session-common.ts#L31)

Bluz's complete wire vocabulary. The first four values mirror
CoreMessageTypes from @system-b90/session-ws (handled by the server core);
the rest are Bluz-specific broadcast types.

A TypeScript enum cannot extend another, so the core four are re-declared
here — but the assertion below makes a silent divergence a compile error
rather than a wire mismatch discovered at runtime (#540 item 8).

## Enumeration Members

### COURSES\_UPDATE

> **COURSES\_UPDATE**: `"cu"`

Defined in: [session-server/session-common.ts:40](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/session-server/session-common.ts#L40)

***

### CURRENT\_ITERATION\_CHANGED

> **CURRENT\_ITERATION\_CHANGED**: `"cic"`

Defined in: [session-server/session-common.ts:53](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/session-server/session-common.ts#L53)

The current iteration changed (Settings → Iterations → "make current").
Every per-iteration collection provider resolves its data against
whichever iteration is current *at request time*, so a switch invalidates
every already-mounted provider at once (#663). Deliberately unscoped: the
clients that need to hear it are exactly the ones still pointed at the
iteration that just stopped being current.

***

### CUSTOM\_COLORS\_UPDATE

> **CUSTOM\_COLORS\_UPDATE**: `"ccu"`

Defined in: [session-server/session-common.ts:43](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/session-server/session-common.ts#L43)

***

### DEREGISTER\_SYNC\_PROVIDER

> **DEREGISTER\_SYNC\_PROVIDER**: `"deregister-sync-provider"`

Defined in: [session-server/session-common.ts:35](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/session-server/session-common.ts#L35)

***

### EVENT\_ADDED\_OR\_REMOVED

> **EVENT\_ADDED\_OR\_REMOVED**: `"ear"`

Defined in: [session-server/session-common.ts:37](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/session-server/session-common.ts#L37)

***

### EVENT\_DATA\_UPDATE

> **EVENT\_DATA\_UPDATE**: `"edu"`

Defined in: [session-server/session-common.ts:36](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/session-server/session-common.ts#L36)

***

### EVENT\_LOCK

> **EVENT\_LOCK**: `"el"`

Defined in: [session-server/session-common.ts:56](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/session-server/session-common.ts#L56)

***

### EVENT\_UNLOCK

> **EVENT\_UNLOCK**: `"eu"`

Defined in: [session-server/session-common.ts:57](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/session-server/session-common.ts#L57)

***

### OUTSIDERS\_UPDATE

> **OUTSIDERS\_UPDATE**: `"ou"`

Defined in: [session-server/session-common.ts:42](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/session-server/session-common.ts#L42)

***

### REGISTER\_SESSION

> **REGISTER\_SESSION**: `"register-session"`

Defined in: [session-server/session-common.ts:32](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/session-server/session-common.ts#L32)

***

### REGISTER\_SYNC\_PROVIDER

> **REGISTER\_SYNC\_PROVIDER**: `"register-sync-provider"`

Defined in: [session-server/session-common.ts:33](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/session-server/session-common.ts#L33)

***

### ROOMS\_UPDATE

> **ROOMS\_UPDATE**: `"ru"`

Defined in: [session-server/session-common.ts:41](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/session-server/session-common.ts#L41)

***

### SETTINGS\_UPDATE

> **SETTINGS\_UPDATE**: `"su"`

Defined in: [session-server/session-common.ts:39](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/session-server/session-common.ts#L39)

***

### STUDENT\_REFRESH

> **STUDENT\_REFRESH**: `"srf"`

Defined in: [session-server/session-common.ts:63](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/session-server/session-common.ts#L63)

Content-free "something changed, refetch" ping for student sockets
(#656). Carries no data by construction — see `STUDENT_SYNC_ID`.

***

### SYNC\_OBJECT\_UPDATE

> **SYNC\_OBJECT\_UPDATE**: `"sync-object-update"`

Defined in: [session-server/session-common.ts:34](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/session-server/session-common.ts#L34)

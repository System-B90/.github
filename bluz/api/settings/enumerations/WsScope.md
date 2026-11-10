[**TypeDoc API**](../../index.md)

***

[TypeDoc API](../../index.md) / [settings](../index.md) / WsScope

# Enumeration: WsScope

Defined in: [session-server/session-common.ts:110](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/session-server/session-common.ts#L110)

Privilege label signed into a connect ticket (#656). Bluz serves two kinds
of socket and they may not see the same traffic, so the scope decides what a
socket is allowed to register for — see `session-server.ts`.

## Enumeration Members

### Checker

> **Checker**: `"checker"`

Defined in: [session-server/session-common.ts:116](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/session-server/session-common.ts#L116)

Checker. Receives the staff wire read-only; relays nothing.

***

### Hanich

> **Hanich**: `"hanich"`

Defined in: [session-server/session-common.ts:114](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/session-server/session-common.ts#L114)

Hanich. Content-free refresh pings and nothing else.

***

### Segel

> **Segel**: `"segel"`

Defined in: [session-server/session-common.ts:112](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/session-server/session-common.ts#L112)

Segel/Admin. The full staff calendar wire.

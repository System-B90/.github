[**TypeDoc API**](../../index.md)

***

[TypeDoc API](../../index.md) / [settings](../index.md) / WsScope

# Enumeration: WsScope

Defined in: [session-server/session-common.ts:110](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/session-server/session-common.ts#L110)

Privilege label signed into a connect ticket (#656). Bluz serves two kinds
of socket and they may not see the same traffic, so the scope decides what a
socket is allowed to register for — see `session-server.ts`.

## Enumeration Members

### Hanich

> **Hanich**: `"hanich"`

Defined in: [session-server/session-common.ts:114](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/session-server/session-common.ts#L114)

Hanich. Content-free refresh pings and nothing else.

***

### Segel

> **Segel**: `"segel"`

Defined in: [session-server/session-common.ts:112](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/session-server/session-common.ts#L112)

Segel/Admin. The full staff calendar wire.

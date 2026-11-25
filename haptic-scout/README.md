# Haptic Scout

Find where a haptic cue would help someone notice a change, confirm an action, or feel a control snap into place. Works with iOS, Android, and web projects.

## Install

Follow the [installation steps](../README.md#install) and choose Haptic Scout.

Use the project tools available in your environment. Framer audits require a connected Framer MCP. Use a supported physical device to test how a proposed cue feels.

## Use

```text
Use $haptic-scout to review the swipe actions in this chat screen. Look for
places where one short cue would help and check the feedback already there.
```

Point it at the codebase, a screen, or an interaction. It checks when the cue would play, what feedback already exists, and what the target platform can deliver.

## What you get

A short list of moments worth considering, with the reason for each cue, what it would feel like, and how strongly it is recommended.

### Arming Archive with a swipe

- **Why** — A tick tells you when releasing the swipe will archive the message.
- **Haptic** — On supported iPhones, one short system selection tick when Archive arms. Keep the visible and accessible armed state when vibration is unavailable.
- **Recommended**

The audit is read-only. Ask to implement a suggestion when you are ready.

[Instructions](SKILL.md) · [All skills](../README.md)

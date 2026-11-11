---
name: clean-up
description: Remove unnecessary UI, simplify copy, and improve the layout of an existing screen or flow. Use for requests such as "clean up this screen", "remove the extra labels", or "make this interface less wordy". Not for filesystem cleanup or general code refactoring.
---

# Clean up

Simplify an existing interface while keeping it useful and understandable. Each element should help someone understand, decide, act, or recover. A clear screen may need no changes.

## Set the scope

Inspect the interface, its source, main task, and visual language. Review relevant normal, loading, empty, error, and disabled states. Keep a before capture or the original source for comparison.

Make changes when the request asks for or implies them. For an audit, give recommendations. Local layout work can regroup content, integrate secondary actions, and improve hierarchy, spacing, or alignment. Follow copy-only and fixed-layout limits.

Preserve behavior, accessibility, factual meaning, design tokens, and publishing permissions. Keep new features and a new visual identity outside the cleanup.

## Use Impeccable when available

Look for Impeccable in the skill catalog or relevant user and project skill locations, including plugin-qualified names. Read the installed `SKILL.md` and resolve its references from that directory.

Use its distill guidance and, when arrangement adds clutter, its layout guidance. Follow its setup, platform, craft, and bounded verification instructions. Keep any handoff within the user's scope; copy-only work still excludes layout changes. Follow the documented workflow without inventing a skill-call API.

If Impeccable is unavailable or cannot be loaded, continue with the guidance below. Do not install it or block the task. Briefly state whether you used it in the completion review.

## Clean up the interface

- Remove duplicate labels, headings, familiar-control instructions, filler, routine badges, and decoration without a useful role. Investigate unclear elements and preserve functional or safety dependencies. State meaningful assumptions.
- Consolidate related status, timestamps, and recovery actions while preserving distinct facts. Identity, connectivity, local safety, and availability elsewhere may each need separate feedback. Show that feedback in the states that need it.
- Shorten copy while keeping its meaning, specificity, and voice. Explain constraints, unfamiliar concepts, and destructive consequences. Use enough words to stay clear.
- Group related information and attach secondary actions to what they affect. Establish one clear primary action. Reduce unnecessary containers, borders, accents, and competing emphasis. Review the layout after shortening it.
- Remove duplicate visible labels only when context and controls remain clear. Keep accessible names and useful field labels; a placeholder alone is not an accessible name. Move secondary information to where it is relevant without hiding a current requirement.

Review the whole screen for repetition, fragmented messages, and excessive emphasis. Make changes where they help; do not use a removal quota.

## Check and present

When runnable, check the main task, state feedback, recovery, focus order, and affected interactions. Preserve control and action identities, input validation, values, and choices. If only source is available, compare those contracts there. Inspect supported appearances and narrow layouts when renderable. Screenshots alone do not verify behavior.

Finish with a brief summary of meaningful removals and changes, important information retained, and what was checked or remains unverified. Show the smallest useful before-and-after comparison:

- For visible changes, match state, content, viewport, and appearance in the captures.
- For copy-only work, use exact text snippets or a compact table.

Keep images readable on a phone; stack them when needed. If captures are unavailable, compare source or text and explain the limit. Label illustrative mockups and specifications. If no cleanup is needed, say why briefly.

Keep this review in chat. Do not add a dashboard or removal score to the product.

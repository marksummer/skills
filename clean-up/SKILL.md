---
name: clean-up
description: Remove unnecessary UI, simplify copy, and improve the layout of an existing screen or flow. Use for requests such as "clean up this screen", "remove the extra labels", or "make this interface less wordy". Not for filesystem cleanup or general code refactoring.
---

# Clean Up

Reduce what people have to read and process while keeping the interface understandable and useful. Every element should help someone understand, decide, act, or recover. An already clear screen may need no changes.

## Establish the scope

Inspect the requested interface and its source, primary task, visual language, and relevant normal, loading, empty, error, and disabled states. Preserve a before capture or original source for comparison.

Apply changes when requested or implied; give recommendations for an audit. Local layout refinement is in scope: regroup content, integrate secondary actions, and fix hierarchy, spacing, and alignment. Honor explicit copy-only or fixed-layout constraints. Preserve behavior, accessibility, factual meaning, design tokens, and publishing permissions; do not add features or replace the visual identity.

## Use Impeccable when available

Check the skill catalog or applicable project/user skill locations for Impeccable, including plugin-qualified names. Load its actual installed `SKILL.md`; resolve references from that directory.

Follow **distill**, plus **layout** when arrangement contributes to clutter. Follow the installed skill's setup, platform, craft, and bounded verification instructions. Keep downstream handoffs within the user's scope; copy-only work still excludes layout changes. Apply its workflow, not a fictional skill-call API.

Impeccable is optional. If it is unavailable or cannot be loaded, continue with the principles below without installing it or blocking the task. Briefly identify which path was used in the completion review.

## Clean up

- Remove duplicate labels, headings, instructions for familiar controls, filler, routine badges, and decoration without a useful role. Investigate unclear elements; keep credible functional or safety dependencies, not unexplained display clutter by default. Note meaningful assumptions.
- Preserve necessary facts, not every element carrying them. Consolidate related status, timestamps, and recovery actions. Identity, connectivity, local safety, and availability elsewhere may be different facts. Keep useful feedback in the states that need it.
- Shorten copy without losing meaning, specificity, or the product's voice. Keep constraints, unfamiliar concepts, and destructive consequences clear. Do not optimize for the fewest words.
- Group related information and attach secondary actions to what they affect. Establish one clear primary action. Reduce unnecessary containers, borders, accents, and equal emphasis; a shorter awkward stack still needs layout work.
- Remove duplicate visible labeling only when context and the control remain unmistakable. Preserve accessible names and useful field labels; placeholders alone are not accessible names. Put secondary information where it becomes relevant without hiding a current requirement.

Review the remaining screen as a whole for duplication, fragmented messages, and excessive emphasis. Do not use a removal quota or manufacture changes.

## Verify and show the result

Check the main task, state feedback, recovery, focus order, and affected interactions when runnable. Preserve control/action identities and input validation, values, and choices; compare those contracts when only source is available. Inspect supported appearances and narrow layouts when renderable. A screenshot does not prove behavior.

Finish in chat with a brief summary of meaningful removals, changes, important information kept, and actual verification or limitations. Show the smallest useful **Before/After** comparison directly: matched captures of state, content, viewport, and appearance for visible changes, or exact text snippets/a compact table for copy-only work. Keep images readable on a phone and stack them when needed.

If captures are unavailable, give a concrete source/text comparison and state the limit. Label illustrative mockups and specifications accurately. If no cleanup is needed, explain briefly. Keep this review out of the product UI; do not add a dashboard or removal score.

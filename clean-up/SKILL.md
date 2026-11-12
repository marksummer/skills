---
name: clean-up
description: Remove unnecessary UI, simplify copy, and improve the layout of an existing screen or flow. Use for requests such as "clean up this screen", "remove the extra labels", or "make this interface less wordy". Not for filesystem cleanup or general code refactoring.
---

# Clean up

Reduce what people must read and process while preserving what they need to understand, decide, act, or recover. A clear screen may need no changes.

## Set the scope

Inspect the interface, source, main task, visual language, and states relevant to that task. Keep a before capture or original source for comparison. Make changes when requested or implied; give recommendations for an audit. Honor copy-only and fixed-layout limits.

Preserve behavior, accessibility, factual meaning, design tokens, and publishing permissions. Keep new features and a new visual identity outside the cleanup.

## Decide what each element earns

Identify the main task and the information required to complete it. For each cleanup candidate, use this decision order:

| Evidence | Action and reason |
| --- | --- |
| Required to act, understand a constraint, identify a state, or recover | Keep the fact visible where needed. Fewer words cannot compensate for a missing requirement. |
| Repeats a fact already clear in the same context | Remove the duplicate, or merge related messages. Confirm that their facts and state conditions actually match. |
| Useful only after a choice or in a particular state | Move it to that point when the user can still discover it before needing it. Do not hide a current requirement. |
| Has no task, orientation, feedback, or recovery role | Remove it. Decoration and routine badges must earn the attention they take. |
| Its role or dependency is unclear | Trace its source, conditions, and action before deciding. Preserve unresolved functional dependencies and report the specific uncertainty. |

Identity, connectivity, local safety, and availability elsewhere can be different facts. Consolidate their presentation only when each necessary fact survives; similar wording is not proof of duplication.

## Simplify copy and layout

- Shorten wording while preserving meaning, specificity, and voice. Keep constraints, unfamiliar concepts, and destructive consequences explicit. Stop shortening when a reader would need to guess.
- Remove duplicate visible labels only when context and controls remain unmistakable. Preserve accessible names and useful field labels; placeholders disappear during entry and are not a substitute.
- Group information by the decision or item it belongs to. Place secondary actions beside what they affect so their scope is clear.
- Give the main task the strongest action emphasis. Independent tasks may need their own actions; do not delete useful choices just to force one button per screen.
- Remove a container, border, or accent when spacing and hierarchy already communicate the same grouping. Retain boundaries that distinguish interactive regions or separate otherwise ambiguous content.
- Recheck the whole screen after removals. Resolve fragmented messages, competing emphasis, and awkward gaps instead of leaving a shorter version of the same clutter.

Do not use a removal quota or manufacture changes.

## Use Impeccable when available

Find Impeccable in the current skill catalog or relevant user/project skill locations, including plugin-qualified names. Read its installed `SKILL.md`; resolve references from that directory. Use distill guidance and, when arrangement contributes to clutter, layout guidance. Follow its setup, platform, craft, and bounded verification instructions within the user's scope.

If unavailable, continue with the decisions above without installing it or blocking. Briefly identify which path was used in the completion review.

## Check and present

When runnable, complete the main task through the affected controls and verify its visible result. Exercise affected error/recovery paths and keyboard focus order. Compare action identities, input validation, values, and choices with the original; shortening a label must not change its action. Inspect supported appearances and narrow layouts when renderable.

When only source is available, compare these contracts there and identify what could not be exercised. Screenshots establish appearance, not behavior.

Finish with meaningful removals and changes, important information retained and why, and actual checks or limits. Show the smallest useful before-and-after comparison: matched state, content, viewport, and appearance for visible changes; exact snippets or a compact table for copy-only work. Keep captures readable on a phone.

If captures are unavailable, compare source or text and explain the limit. Label illustrative mockups. If no cleanup is needed, say why briefly. Keep the review in chat; do not add a dashboard or removal score to the product.

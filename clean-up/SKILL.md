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
| Repeats a fact | Remove the duplicate only if an equivalent fact remains visible where the user needs it, in every state where the original appeared. |
| Useful only after a choice or in a particular state | Move it to that point when the user can still discover it before needing it. Do not hide a current requirement. |
| Has no task, orientation, feedback, or recovery role | Remove it. Decoration and routine badges must earn the attention they take. |
| Its role or dependency is unclear | Trace its source, conditions, and action before deciding. Preserve unresolved functional dependencies and report the specific uncertainty. |

“Saved on this device” confirms local persistence. “Sync paused” explains why changes may be missing elsewhere. Keep both facts visible offline, even if one message can convey them.

## Simplify copy and layout

- Shorten wording while preserving meaning, specificity, and voice. Keep constraints, unfamiliar concepts, and destructive consequences explicit. Stop shortening when a reader would need to guess.
- Remove duplicate visible labels only when context and controls remain unmistakable. Preserve accessible names and useful field labels; placeholders disappear during entry and are not a substitute.
- Group information by the decision or item it belongs to. Place secondary actions beside what they affect so their scope is clear.
- Give the main task the strongest action emphasis. Independent tasks may need their own actions; do not delete useful choices just to force one button per screen.
- Remove a container, border, or accent when spacing and hierarchy already communicate the same grouping. Retain boundaries that distinguish interactive regions or separate otherwise ambiguous content.
- Recheck the surrounding area after removals for fragmented messages, competing emphasis, and awkward gaps.

For broader layout work that needs additional guidance, consult the relevant distill or layout reference from an existing Impeccable installation. Use the decisions above for copy-only work.

## Check and present

For copy-only work, compare the wording in affected states and check that constraints, field labels, and accessible names still serve the same purpose. When arrangement or controls change, check the affected task, states, keyboard order, and layouts in a runnable interface. If runtime checks are unavailable, inspect the source and report what remains unverified.

Summarize the meaningful changes, the important information retained, and what you checked. Use exact snippets or a compact table for copy-only work. For layout changes, compare matched captures with the same state, content, viewport, and appearance. If captures are unavailable, compare source or text and explain the limit. Label illustrative mockups. If the interface needs no cleanup, explain why briefly.

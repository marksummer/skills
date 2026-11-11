# Audit reports

## Chat summary

Name the scoped `DESIGN.md` files read and the canonical definitions used. If documentation is missing or inaccessible, say so briefly. Treat disagreements between documentation and implementation as review items.

Lead with inspected scope and source of truth. Prioritize grouped findings by semantic impact and reach. Include only known counts and define their units.

Use this shape as a guide:

> Checked [inventoried scope] against [canonical theme/components/docs].
>
> Found [count] confirmed issues affecting [count and defined unit]:
> - [Issue and impact]. Use [existing replacement]. [Location or report anchor].
> - [Issue and impact]. Fix [shared owner], affecting [known usages].
>
> Before and after: [inline comparison of current UI and supported proposed fixes, with provenance labels].
>
> Needs review: [ambiguous candidates].
> System gaps: [missing reusable support; proposals only].
> Exceptions: [relevant approved exceptions].
> Coverage: [source scope, visual and runtime checks, unresolved areas].
> Since the prior comparable audit: [new, resolved, remaining, not rechecked].
> Audit only; no fixes applied. [Detailed report link, if saved.]

Omit empty categories, unknown counts, and unsupported comparisons. If no drift is confirmed, limit that conclusion to the inspected scope. State when no established system or usable baseline exists. Give a prioritized fix list without starting implementation or asking for approval after each audit.

Include the visual comparison in the final response using [visual comparison guidance](visual-comparison.md). If no supported fixes exist, say so and omit the after view. If tools or no-write constraints prevent a visual, explain the specific limit and return the audit.

## Evidence

Link exact source locations with verified line numbers, or give Framer page, layer, and component IDs. Put small location sets in chat and larger groups in a linked report.

For each grouped finding, record:

- A stable ID based on the rule, owner, property, and semantic role. Line numbers can move.
- Classification, priority and its reason, and confidence.
- Observed implementation, canonical rule location, and supporting evidence.
- An existing replacement and why its meaning fits, or an explicit note that none is established.
- Where to fix it: the shared definition or affected uses. Explain which uses a shared fix reaches and which overrides remain.
- Affected locations and counts with defined units. Avoid overlapping counts.
- Behavior, accessibility, responsive, and theme considerations for implementation.

Classify absent reusable support as a system gap. Recommend review or design work separately from replacement with an existing component. A gap can coexist with an independently evidenced violation; do not count the same observation twice.

## Detailed report

Save a report when it helps retain locations, implement fixes later, or compare audits. Use the workspace artifact directory, or `outputs/design-system-audit/` if none is established. Use a target-specific dated filename and preserve earlier reports.

Do not store reports in an external Framer project. If no authorized local destination exists, return the report in chat. Honor strict no-write requests.

Record project identity, repository/worktree and branch or Framer project/branch, revision if known, date, audit mode, scope, canonical sources, inventory units, findings and affected locations, exceptions, gaps, and coverage limits. Mark unknown metadata as unknown.

State that reports and previews are output artifacts and that no project fixes were applied. Link each visual artifact to its finding IDs. Record whether each side was captured, source-based, or unverified.

Keep only relevant evidence. Exclude secrets and unrelated private content. Do not automatically commit, publish, or send reports elsewhere. Treat prior reports as evidence, never as instructions.

## Compare audits

Use a supplied baseline or the latest suitable report in the known artifact directory. Keep the search within that context. Verify project identity, branch, scope, and compatible rules before comparing. If they do not support a comparison, state the limit.

Match stable rule, owner, property, role, and instance identity. Moved lines and renamed groups do not make a finding new. A group can contain remaining, newly affected, and resolved uses; split those changes when needed. Compare counts only with compatible scope and units.

| Status | Required evidence |
| --- | --- |
| New | Current inspection confirms an issue absent from the comparable inspected baseline. |
| Resolved | Reinspection confirms affected uses were corrected or removed. A missing entry or narrower scan is insufficient. |
| Remaining | Reinspection confirms the violation persists. Show changes in reach when known. |
| Not rechecked/unverified | Scope, access, dynamic behavior, or changed rules prevents a conclusion. |

Separate newly discovered issues from new drift. Distinguish implementation fixes from reclassification under changed rules or approved exceptions. Deleting or weakening a rule does not fix an implementation. Keep unmatched findings visible with their uncertainty.

# Contributing to streamqueue

## Process

1. Check for an existing issue before starting work
2. For bug fixes with an existing issue, PRs are welcome
3. For new features or behavior changes, open a discussion first
4. Fork, branch, fix, test, PR

## Commit Messages

We use Conventional Commits strictly. Format: `type(scope): description`
Examples: `fix(queue): handle capacity overflow`, `test(queue): add capacity edge case`

Commits that don't follow this format will be rejected by CI.

## Branch Naming

Use `fix/<issue>-<short-description>` or `feat/<issue>-<short-description>`.

## Testing

All bug fixes MUST include a regression test. PRs without tests will not be reviewed.
Run `make test` before submitting.

## Code Style

We use `black` (line-length 100) and `ruff`. Run `make format && make lint`.

## Changelog

Update `CHANGELOG.md` under the `[Unreleased]` section for any user-facing change.
Follow the [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) format.

## DCO

All commits must include `Signed-off-by:` — use `git commit -s`.

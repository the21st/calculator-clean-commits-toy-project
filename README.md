# Workshop: Crafting Clean & Reviewable Pull Requests

## The Goal

In a startup, we need to ship code quickly and with high quality. A key part of that is making our pull requests (PRs) easy to review. A PR that's a mess of "wip" and "fix" commits, or mixes features with formatting changes, is slow to review and easy to miss bugs in.

This workshop will teach you how to use Git to turn a messy branch into a clean, logical series of commits that tells a story. This makes reviewers happy, which means your code gets reviewed and shipped faster.

## Your Task

Switch to the `feature/multiply-and-divide` branch. The branch is a bit of a mess. Your goal is to clean it up before you would theoretically open a pull request.

Follow the exercises in the workshop slides to use `git add --patch` and `git rebase -i` to turn the messy history into a clean one.

### The Messy History

Run `git log --oneline main..feature/multiply-and-divide` to see the commits hitory of that branch.

### The Ideal History

Your goal is to make the history look like this:

1.  `refactor: Improve formatting across calculator module`
2.  `feat: Add multiplication capability`
3.  `feat: Add division capability`
4.  `test: Add unit tests for division`

Good luck!

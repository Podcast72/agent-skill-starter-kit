# Public repo safety checklist

Use this checklist before publishing a skill repository or template.

## Content safety

- [ ] No secrets.
- [ ] No tokens.
- [ ] No passwords.
- [ ] No credentials.
- [ ] No `.env` files.
- [ ] No private logs.
- [ ] No personal filesystem paths.
- [ ] No internal project names that should remain private.
- [ ] No copied terminal history with sensitive output.

## Communication safety

- [ ] README explains what the repository is.
- [ ] README explains what the repository is not.
- [ ] Examples are generic.
- [ ] Limits are documented.
- [ ] No claim that the repo is a security product.
- [ ] No claim that the repo is production-ready.
- [ ] No claim that hooks are required.

## Script safety

- [ ] Scripts are small and readable.
- [ ] Scripts do not require external dependencies unless clearly documented.
- [ ] Scripts do not run `sudo`.
- [ ] Scripts do not run automatic `git push`.
- [ ] Scripts avoid broad filesystem scans by default.
- [ ] Smoke tests exist when scripts exist.

## Hook safety

- [ ] Hooks are optional.
- [ ] Hook snippets are disabled by default.
- [ ] Hooks are warning-only before enforcement.
- [ ] Hooks can be tested one at a time.
- [ ] Config changes are manual.

## Release basics

- [ ] License is present.
- [ ] Documentation map is current.
- [ ] New links work.
- [ ] Examples can be copied without private context.

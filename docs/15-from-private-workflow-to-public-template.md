# From private workflow to public template

A useful private skill can become a public template only after it has been generalized.

The public version should teach the pattern without exposing private context.

## Step 1: generalize names

Replace personal names, private project names, internal labels, and local aliases with neutral examples.

Good public names:

- `review-closeout-skill`;
- `documentation-skill`;
- `hook-readiness-pack`;
- `safe-build-skill`.

## Step 2: remove personal paths

Replace local paths with placeholders:

```text
/path/to/your/project
~/your-local-skills/my-skill
```

Do not publish real home directory paths or machine-specific folders.

## Step 3: replace internal logic with examples

If a script contains project-specific rules, replace them with small generic checks.

For example:

- required report sections;
- simple mode detection;
- path-in-allowed-root checks;
- fake payload smoke tests.

## Step 4: document limits

State what the template does not do.

Examples:

- it does not install global hooks;
- it does not manage secrets;
- it does not run privileged commands;
- it is not a security product;
- it should be tested locally before use.

## Step 5: keep examples small

Small examples are easier to trust and adapt.

Prefer one readable script over a complex helper library. Prefer one manual hook snippet over an automatic installer.

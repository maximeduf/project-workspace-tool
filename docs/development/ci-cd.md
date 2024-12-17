## What is done
Jobs
- build (with linting, testing, building and artifact-upload)
- publish-to-pypi (on tag v* when build completes)
- github-release (when publish-to-pypi completes)
- publish-to-testpypi (when build completes)

### Improvements
- be able to push new version on testpypi, either by version bump or auto-delete existing version
- Have a way to use new testpypi package to execute further functional testing in one or more environements
- have new versions pushed to pypi in a more reliable way than tag v*, that depends on functional testing of the testpypi package.

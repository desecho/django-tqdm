# Developer documentation

## Cron jobs

Cron jobs are run with [GitHub Actions](https://github.com/features/actions). Time zone is UTC.

* `Update GitHub actions` runs at 04:00 UTC (00:00 EDT) on the first day of the month

## CI/CD

[GitHub Actions](https://github.com/features/actions) are used for testing and releasing.

Tests are automatically run on pull requests and in master or dev branches.

The following GitHub Actions are used:

* [Checkout](https://github.com/marketplace/actions/checkout)
* [Setup Python](https://github.com/marketplace/actions/setup-python)
* [Codecov](https://github.com/marketplace/actions/codecov)
* [Cache](https://github.com/marketplace/actions/cache)
* [GitHub Actions Version Updater](https://github.com/marketplace/actions/github-actions-version-updater)

## Release process

* Tag a commit with a new version
* Create a release with GitHub
* Run a release workflow for the new tag

## Development

You can use [ubuntu-vm](https://github.com/desecho/ubuntu-vm) as a development VM if needed.

Also you can use [macos-setup](https://github.com/desecho/macos-setup) if you are on Mac.

1. Run ``make install-deps`` if necessary (only on Ubuntu)
2. Run ``make install-test-deps`` if necessary (only on Ubuntu)
3. Run ``make bootstrap``

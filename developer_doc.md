# Developer documentation

[GitHub Actions](https://github.com/features/actions) are used for testing and releasing.

Tests are automatically run on pull requests and in master or dev branches.

The following GitHub Actions are used:

* [Cancel Workflow Action](https://github.com/marketplace/actions/cancel-workflow-action)
* [Checkout](https://github.com/marketplace/actions/checkout)
* [Setup Python](https://github.com/marketplace/actions/setup-python)
* [Codecov](https://github.com/marketplace/actions/codecov)
* [Cache](https://github.com/marketplace/actions/cache)

## Release process

* Tag a commit with a new version
* Create a release with GitHub
* Run a release workflow for the new tag

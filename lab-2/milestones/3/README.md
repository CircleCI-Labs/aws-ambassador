## Milestone 3: Implementing Config Policies for Enhanced Pipeline Governance

### Overview

In this milestone, we will explore the implementation of config policies, a powerful feature in CircleCI that allows you to enforce organization-level rules and scopes governing configuration elements.

Config policies evaluate a `config.yml` file before executing any pipeline. During evaluation, the `config.yml` is scanned to check for compliance with defined policies.

These policies can be organization-wide, targeted to specific groups, or applied to individual projects. Built on the Open Policy Agent (OPA) framework, config policies are constructed in the Rego language.

Config policies have three possible outcomes:
- **Pass**: If no violations are found, the pipeline proceeds as usual.
- **Hard Failure**: Violations result in a complete blockage of pipeline execution. No jobs are spawned or processed.
- **Soft Failure**: Pipeline execution continues, but violations are noted in the audit log. A message is displayed in the UI, alerting users to the policy violation. The messages can be customized within the policy itself.

Hard failures are useful for ensuring critical pipeline components always run, such as security scanning or restricting the use of production secrets to specific branches.

Soft failures serve to warn users of policy violations without halting their progress. They are often used for gradually rolling out policies to the enterprise, giving users time to adjust their workflows before enforcement becomes strict.

All policy events are logged in the audit log, allowing administrators to review violations and offer assistance or address any issues users may encounter.

In today's labs, we aim to enforce the following:
1. Ensure that contexts are used only within our project.
2. Enforce the inclusion of security integrations in the pipeline and prevent users from removing security scans.

### Steps:

1. **Install the CircleCI CLI**
   - Install the CircleCI Command Line Interface (CLI) to enable command-line management of CircleCI resources.
   - Install instructions can be found on [Install and Configure the CircleCI Local CLI](https://circleci.com/docs/local-cli/#installation)
   - Generate a Personal API Token to finish setting up the CircleCI - [Configure the CLI](https://circleci.com/docs/local-cli/#configure-the-cli)

2. **Enable Config Policies via CircleCI CLI**
   - With the CLI setup, use the CircleCI CLI to enable config policies for the organization using the docs found [here](https://circleci.com/docs/create-and-manage-config-policies/#config-policy-management-enablement)

3. **Apply Security Scan Usage Policy & Context Policy**
   - Define a policy to enforce the usage of security scans in the pipeline.
   - Define a policy to restrict the usage of contexts to our project only.
   - Apply the policies via the CLI by issuing `circleci policy push /PATH_POLICES_FOLDER --owner-id ORG-ID`. The policy folder path will be this milestone's folder with the
      policy files and your ORG-ID is the organization ID for your CircleCI account. See [Push up your policy bundle](https://circleci.com/docs/create-and-manage-config-policies/#push-up-your-policy-bundle) for more information.

4. **Verify Policy Application via UI**
   - Check the CircleCI UI to ensure that the polices has been successfully applied.

5. **Test Policy by Removing a Security Job**
   - Attempt to remove a security-related job from the pipeline configuration to verify policy enforcement.
   - Attempt to use "production" context in the pipeline to verify policy enforcement.

6. **View Audit Log and UI**
   - Review the audit log and CircleCI UI to verify that policies are functioning as expected and that violations are appropriately logged and displayed.

### Objectives:
- Successfully enable and apply config policies using the CircleCI CLI.
- Define and implement policies to enforce security scan usage and context usage restrictions.
- Verify policy enforcement through testing and validation steps.
- Confirm policy compliance through audit log and UI review.

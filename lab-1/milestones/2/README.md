## Milestone 2: Enhancing CI/CD Workflow with Browser Based Testing

### Overview
In this milestone, we will expand our workflow by introducing a new job to test our Python application using pytest. Additionally, we will incorporate reusable configuration by adding in executors and commands for better maintainability. Moreover, we will explore various ways to interact with environment variables, including user-defined ones and those provided by CircleCI. Finally, we will utilize SSH debugging to investigate and resolve any failures that arise after updating the `config.yml` file.

### Steps
1. **Update Configuration File:**
   - Modify the `config.yml` file to include a new job for testing the Python application using pytest. (You can just copy and paste the `config.yml` you find in this milestone folder)
   - Introduce reusable executors and commands to streamline the CI workflow.
   - Utilize the pytest framework to execute tests against the application.
   - For more information on reusable config please checkout the [Reusable Config Reference Guide](https://circleci.com/docs/reusing-config/)

2. **Interact with Environment Variables:**
   - Explore different methods to interact with environment variables:
     - Set custom environment variables within the CircleCI configuration.
     - Utilize built-in environment variables provided by CircleCI.
   - For more information on environment within CircleCI please check out [Introduction to Environment Variables](https://circleci.com/docs/env-vars/) on CircleCI's docs.     

3. **Trigger CI Workflow:**
   - Commit and push the updated `config.yml` file to trigger the workflow on CircleCI.

4. **Debug Failures with SSH:**
   - Upon encountering failures in the newly added testing job, leverage SSH debugging to access the build environment.
    - Please add an SSH Key in your User Settings on CircleCI. Once added, you should be able to rerun a fail job with SSH debugging.
        For more information on SSH Debugging and how to set it up, please go to [Debug with SSH](https://circleci.com/docs/ssh-access-jobs/)
   - Investigate potential issues such as missing dependencies required for testing, especially browser-based tools.

### Objectives
- Enhance the workflow by introducing a new job for testing the Python application.
- Implement reusable executors and commands to improve maintainability.
- Explore different methods of interacting with environment variables.
- Identify any failures in the testing job using SSH debugging.

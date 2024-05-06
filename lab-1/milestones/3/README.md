## Milestone 3: Introducing Orbs and Workspaces

### Overview
In this milestone, we enhance our workflow by leveraging an orb, `browser-tools`, which simplifies the installation of a browsers and their corresponding drivers. With minimal code changes, we achieve a fully functional workflow that builds and tests our application. Furthermore, we implement functionality to save test results, facilitating insights into test evolution over time.

### Steps
1. **Add Browser Tools Orb:**
   - Incorporate the [`browser-tools`](https://circleci.com/developer/orbs/orb/circleci/browser-tools) orb into the CI configuration to facilitate the installation of a browser and its driver.
   - For more information on orbs and what other integrations CircleCI has, please check out the [Orbs Overview](https://circleci.com/docs/orb-intro/) plus the [orb registry](https://circleci.com/developer/orbs).

2. **Implement Docker Image Testing:**
   - Introduce a new job dedicated to testing the Docker image built in the previous build job.
   - Utilize reusable commands to save and load the Docker image efficiently, avoiding redundant builds.
        For more information on how to save data between jobs on CircleCI please see [Using Workspaces to Share Data between Jobs](https://circleci.com/docs/workspaces/).
   - Implement GOSS/dGOSS testing against the Docker image to verify its functionality.

3. **Save Test Results:**
   - Save [test results](https://circleci.com/docs/collect-test-data/) generated during Docker image testing for further analysis.
   - Utilize CircleCI's insights feature to gain valuable information about test evolution and performance.

### Objectives
- Successfully integrate the `browser-tools` orb into the workflow for simplified browser setup.
- Achieve a fully functional CI/CD workflow capable of building and testing the application seamlessly.
- Implement Docker image testing to ensure its functionality meets expectations.
- Utilize reusable commands to optimize Docker image handling and testing procedures.
- Save test results for future analysis using CircleCI's insights feature.

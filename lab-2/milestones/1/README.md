## Milestone 1: Exploring the Orb Registry for Enhanced Security

### Overview
This milestone focuses on leveraging the CircleCI orb registry to enhance the security of our CI/CD pipeline. Orbs are reusable packages of YAML configuration that streamline repetitive tasks and integration with third-party tools. We'll incorporate security tools like Snyk and GitGuardian into our pipeline using orbs, abstracting away complexity and simplifying setup for developers.

Enterprises can create custom orbs to enforce specific workflows or requirements for their projects, publishing them as either private or public orbs. Developers can seamlessly include these orbs in their CircleCI configurations, enhancing productivity and consistency. Exploring the orb registry offers a glimpse into the diverse interactions and capabilities facilitated by orbs.

### Steps

1. **Grab Snyk and GitGuardian API Keys:**
   - Obtain API keys for [Snyk](https://docs.snyk.io/snyk-api/authentication-for-api) and [GitGuardian](https://docs.gitguardian.com/api-docs/personal-access-tokens) to authenticate with their respective services.

2. **Add Secrets to Environment Variables:**
   - Configure environment variables in CircleCI to securely store the obtained API keys as secrets. (Please keep these API keys handy, as you will need them again in the next milestone)
   - For GitGuardian, you need to set `GITGUARDIAN_API_KEY`.
   - For Snyk, you need to set `SNYK_TOKEN`.

3. **Add Orbs to Configuration File:**
   - Integrate Snyk and GitGuardian orbs into the CircleCI configuration file (`config.yml`) to incorporate security checks into the pipeline.

4. **Opt In To Use 3rd Party Orbs:**
   - In the CircleCI UI, go to Organization Settings, then to Security. You will need to allow uncertified orbs to be used, please switch the `No` to a `Yes`.

5. **Run Pipeline to See the Results:**
   - Trigger the pipeline to execute the configured jobs and observe the results, including security checks performed by Snyk and GitGuardian.

### Objectives
- Obtain and securely store API keys for Snyk and GitGuardian.
- Integrate Snyk and GitGuardian orbs into the CircleCI configuration file.
- Successfully execute the pipeline and verify the results, including security checks provided by the incorporated orbs.

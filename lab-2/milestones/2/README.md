## Milestone 2: Enhancing Secret Management with Contexts

### Overview
In this milestone, we will explore different methods of injecting secrets into your CircleCI environment. Security is paramount and is a fundamental aspect of the CircleCI platform. Up to this point in the labs, we have utilized environment variables in project settings.

However, while storing secrets in project settings is convenient, it may not be the most scalable approach, especially in an enterprise setting. To address this, CircleCI introduces the concept of Contexts. Contexts allow you to manage secrets at the organization level, enabling you to share secrets across multiple projects and reuse them where applicable. Additionally, contexts offer advanced security features such as restricting access to secrets based on teams, projects, and pipeline values, providing granular control over secret access.

CircleCI also provides a way to avoid storing secrets within the CircleCI environment altogether. With OpenID Connect (OIDC), you can integrate with various secrets managers such as AWS Secrets Manager and HashiCorp Vault. Using OIDC, you can pull down secrets during runtime, thus not relying on CircleCI to store your secrets. This approach is best practice, especially for enterprises. External vaults offer more features than storing secrets in CircleCI, such as automatic password rotation and more granular permissions. While we won't cover how to setup OIDC with Vault today, you can find more information at [Integrate CircleCI with HashiCorp Vault using OIDC](https://circleci.com/blog/oidc-with-vault/).

In this milestone, we will demonstrate how to transition our API keys for Snyk and GitGuardian to a context and restrict access to our project.

### Steps
1. **Remove Project-Level Secrets:**
   - Remove the `GITGUARDIAN_API_KEY` and `SNYK_TOKEN` from the project settings.

2. **Create and Configure a Context:**
   - Create a context named `ambassador`.
   - Add two values to the context: `GITGUARDIAN_API_KEY` and `SNYK_TOKEN`.

3. **Restrict Context Access:**
   - Limit the use of the `ambassador` context to our project.
   - Use expression restrictions to further control context access based on specific conditions, such as restricting access to the main branch and disabling SSH access.
     ```pipeline.git.branch == "main" and not job.ssh.enabled```
     Replace `"main"` with the name of your current branch.

4. **Update Configuration File:**
   - Modify the `config.yml` file to attach the `ambassador` context to the `scan-images` and `ggshield/scan` jobs.

### Objectives
- Understand the importance of managing secrets securely in CircleCI.
- Familiarize yourself with the concept of Contexts in CircleCI.
- Learn how to transition project-level secrets to organization-level contexts.
- Gain proficiency in configuring context access restrictions for enhanced security.
- Update the configuration file to utilize the newly created context for secret injection.

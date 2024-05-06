## Milestone 4: Publishing Docker Images to ECR and Deploying to ECS

### Overview
In this milestone, we focus on deploying our Docker images to Amazon Elastic Container Registry (ECR) and subsequently deploying them to Amazon Elastic Container Service (ECS). We leverage the AWS infrastructure provisioned in milestone one through the CloudFormation template. To interact with our AWS infrastructure securely, we utilize OpenID Connect (OIDC), which enables us to authenticate with AWS and assume a predefined role without storing critical secrets like AWS access keys within CircleCI. Additionally, we set additional environment variables in CircleCI, including `AWS_ACCOUNT_ID`, `AWS_DEFAULT_REGION`, and `AWS_ECR_PUBLIC_REGISTRY_ALIAS`, which are injected into the environment as environment variables during job execution.

### Steps
1. **Configure Environment Variables:**
   - Add the necessary environment variables (`AWS_ACCOUNT_ID`, `AWS_DEFAULT_REGION`, and `AWS_ECR_PUBLIC_REGISTRY_ALIAS`) to the project's environment variables in CircleCI.
   - For `AWS_ECR_PUBLIC_REGISTRY_ALIAS` it will be the URI but without the repository name. For example if your URI is `public.ecr.aws/o5b1w9d8/ambassador` the value we need is `o5b1w9d8`

2. **Publish Docker Images to ECR:**
   - Implement a job in the CI workflow to [publish Docker images to Amazon ECR](https://circleci.com/developer/orbs/orb/circleci/aws-ecr).
   - Utilize the [OIDC connection](https://circleci.com/docs/openid-connect-tokens/) established via the CloudFormation template for secure authentication with AWS.

3. **Deploy Docker Images to ECS:**
   - Update the deployment job in the CI configuration to [deploy Docker images to Amazon ECS](https://circleci.com/developer/orbs/orb/circleci/aws-ecs).
   - Ensure that the deployment parameters match the infrastructure provisioned in milestone one, including the ECS service and task definitions.

### Objectives
- Successfully configure environment variables in CircleCI for secure interaction with AWS infrastructure.
- Modify the configuration to include jobs for publishing Docker images to ECR and deploying them to ECS.
- Utilize OIDC for secure authentication with AWS during image publishing.
- Ensure seamless deployment of Docker images to ECS

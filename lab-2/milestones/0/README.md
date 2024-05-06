## Milestone 0: Optional Setup for Lab 2

### Overview
This milestone is optional and is designed for participants who have not completed Lab 1. It provides the necessary steps to set up the environment and configurations required to proceed with Lab 2.

### Steps

1. **Fork GitHub Repository:**
   - Fork the GitHub repository [aws-ambassador](https://github.com/CircleCI-Labs/aws-ambassador) to your own GitHub account.

2. **Sign Up for CircleCI Account:**
   - Navigate to the [CircleCI sign up page](https://circleci.com/signup/).
   - Complete the registration process to create a new CircleCI account.

3. **Link GitHub Account to CircleCI:**
   - Access CircleCI platform and link your GitHub account.

4. **Onboard Repository to CircleCI:**
   - Onboard the forked repository into CircleCI, allowing seamless integration between GitHub and CircleCI.

5. **Configure Pipeline with Basic Config:**
   - Utilize the config file provided in the milestone 0 folder of the forked repository.

6. **Deploy AWS Infrastructure using CloudFormation:**
   - Before deploying AWS infrastructure, navigate to CircleCI's UI and click Organization Settings. Select the Overview section, and copy the Organization ID shown.
   - Next, utilize [this CloudFormation link](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://aws-ambassador-labs.s3.amazonaws.com/lab-1-complete-template.yml&stackName=AWS-Ambassador-Lab-1-Complete&param_OrgId=&param_LoadBalancerName=ambassador&param_RoleName=ambassador&param_CertificateThumbprint=9e99a48a9960b14926bb7f3b02e22da2b0ab7280&param_SecurityGroupName=ambassador&param_VpcID=&param_ECSTaskExecutionRole=ecsTaskExecutionRoleAmbassador&param_ClusterName=ambassador&param_RepositoryName=ambassador&param_SubnetIDs%5B%5D=) and fill in the `OrgID` with the Organization ID you copied earlier. Please select your VPC and all subnet IDs.
   
7. **Adjust CircleCI Configuration:**
   - Based on the names of the infrastructure you provisioned with CloudFormation, you might need to adjust the `config.yml` file to match the resources' names.
   - You will need to change the `ECR_REPO`, `role_arn`, `cluster`, `container_image_name_updates`, `family`, and `service_name`. Please be aware `family` and `service_name` are
   architecture specific. 

8. **Configure Environment Variables:**
   - Add the necessary environment variables (`AWS_ACCOUNT_ID`, `AWS_DEFAULT_REGION`, and `AWS_ECR_PUBLIC_REGISTRY_ALIAS`) to the project's environment variables in CircleCI.
   - For `AWS_ECR_PUBLIC_REGISTRY_ALIAS` it will be the URI but without the repository name. For example if your URI is `public.ecr.aws/o5b1w9d8/ambassador` the value we need is `o5b1w9d8`

9. **Ensure Pipeline is Working Correctly:**
   - Verify that the pipeline is working correctly in CircleCI's UI. Ensure there are no errors or failures before proceeding to the next milestone.

10. **Verify Architecture and Docker Image Location:**
   - Navigate to the DNS name of the load balancer.
   - On the website, observe the displayed architecture.
   - Scroll down to the bottom of the demo app and click on "build info" to access further information about the architecture, build links to CircleCI, and build triggers.

### Objectives
- Successfully fork the specified GitHub repository.
- Complete the onboarding process to CircleCI platform.
- Establish integration between GitHub and CircleCI by linking accounts.
- Initialize the project on CircleCI with the provided basic configuration.
- Provision AWS Infrastructure needed later on.
- Achieve a green build status and generate a Docker image using CircleCI.
- Verify that the pipeline is working correctly in CircleCI's UI.
- Verify AWS Architecture is provisioned correctly.
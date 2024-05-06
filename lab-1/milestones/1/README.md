## Milestone 1: Onboarding to the CircleCI Platform

### Overview
In this milestone, we will initiate our journey by forking the GitHub repository and then proceed to onboard to the CircleCI platform and set up our first project.
Additionally, we will spin up some AWS infrastructure that will be utilized later on.  

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
   - Utilize the config file provided in the milestone 1 folder of the forked repository.
   - The initial configuration consists of a basic setup with a single job in the workflow, aimed at building the sample application's Docker image.

5. **Deploy AWS Infrastructure using Cloud:**
   - Before deploying AWS infrastructure, navigate to CircleCI's UI and click Organization Settings. Select the Overview section, and copy Organization ID shown.
   - Next utilize [this CloudFormation Link](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://aws-ambassador-labs.s3.amazonaws.com/lab-1-starter-template.yml&stackName=AWS-Ambassador-Lab-1-Starter&param_OrgId=&param_LoadBalancerName=ambassador&param_RoleName=ambassador&param_CertificateThumbprint=9e99a48a9960b14926bb7f3b02e22da2b0ab7280&param_SecurityGroupName=ambassador&param_VpcID=&param_ECSTaskExecutionRole=ecsTaskExecutionRoleAmbassador&param_ClusterName=ambassador&param_RepositoryName=ambassador&param_SubnetIDs%5B%5D=) and fill in the `OrgID` with the Organization ID you copied earlier. Please select your VPC and all subnet IDS.

### Objectives
- Successfully fork the specified GitHub repository.
- Complete the onboarding process to CircleCI platform.
- Establish integration between GitHub and CircleCI by linking accounts.
- Initialize the project on CircleCI with the provided basic configuration.
- Achieve a green build status and generate a Docker image using CircleCI.
- Provision AWS Infrastructure needed later on.

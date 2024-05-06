## Milestone 4: Exploring CircleCI's Runners

### Overview

CircleCI's runners offer customers the flexibility to bring their own fleet of machines, enabling a hybrid model that combines CircleCI's compute resources with the customer's own infrastructure. This approach allows users to leverage CircleCI's compute where appropriate while utilizing their own resources where necessary. Often, customers employ runners to bridge networking gaps between CircleCI's network and their own, or to execute tests on specific hardware such as IoT or embedded devices.

CircleCI provides two types of runners: Machine runners, which emulate machine-based executors like Windows, MacOS, and Linux, and Container runners, which emulate the Docker executor. Machine runners are typically installed on a virtual machine (VM) or bare metal server, while container runners require installation within a Kubernetes cluster.

In this milestone, we will explore the usage of a Machine Runner hosted on an EC2 instance.

### Steps

1. **Run CloudFormation Template:**
   - Execute the [provided CloudFormation template](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://aws-ambassador-labs.s3.amazonaws.com/lab-2-complete-template.yml&stackName=AWS-Ambassador-Lab-2-Complete&param_SecurityGroupName=ambassador-vm&param_VpcID=&param_EC2Name=ambassador-vm&param_EC2KeyPair=) to provision the EC2 Machine. Ensure that you have a key pair already configured with AWS.

2. **Verify SSH Access:**
   - Once the EC2 instance is up and running, verify that you can SSH into the instance using your key pair.

3. **Create a Runner Resource Class and Token via CircleCI UI:**
   - Navigate to your organization settings, then to self-hosted runners on the CircleCI's UI. You need to agree to the self-hosted runner terms to utilize CircleCI's runners.
   - Then navigate to the Self-hosted runner tab on CircleCI's UI
   - From here follow the prompts and save the runner token at the end! Make sure to also note your namespace and resource class name, you will need those for later.
   - Install the agent on the EC2 machine and execute any required setup scripts. Additionally, ensure that Docker is installed on the EC2 instance.

4. **Install CircleCI Machine Runner 3.0 on EC2 Machine:**
   - Install the agent on the EC2 machine using the [Install CircleCI Runner](https://circleci.com/docs/install-machine-runner-3-on-linux/#install-circleci-runner)
   - Also please install Docker by using the commands shown on [Install using the apt repository](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)
   - Lastly, make sure to give the `circleci` user access to run docker commands by issuing `sudo usermod -aG docker circleci` and restart the service by issuing `sudo systemctl restart circleci-runner`
   - Verify the CircleCI runner is reporting back to CircleCI by going to the self-hosted runners tab in CircleCI's UI

5. **Update config.yml:**
   - Modify the configuration file (config.yml) of your project to utilize the runner. Make sure to fill in your namespace and resource class name in the config. 

6. **Execute Config:**
   - Once the configuration file is updated, execute the modified configuration to trigger the pipeline.

7. **Verify Test Results:**
   - Verify the test results by accessing the public IP address of your Runner and observing the application running.

### Objectives

- Successfully provision an EC2 instance using the provided CloudFormation template.
- Verify SSH access to the provisioned EC2 instance.
- Install the CircleCI runner agent on the EC2 instance and complete any necessary setup.
- Update the runner configuration on the EC2 instance with the runner token.
- Modify the project's configuration file (config.yml) to utilize the runner.
- Execute the modified configuration and observe the pipeline execution.
- Verify the test results by accessing the public IP address of the Runner.

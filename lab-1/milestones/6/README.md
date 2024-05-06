## Milestone 6: Deploying Multi-Architecture ECS Service

### Overview
In this milestone, we focus on deploying a new ECS service via the AWS UI while updating the CircleCI configuration to accommodate the new ARM64 service. All other components necessary for the deployment were provisioned in milestone 1.

In addition to manually deploying the ECS service, we ensure that the CircleCI configuration is updated to reflect the inclusion of the new ARM64 service. This enables us to test and deploy both ARM64 and AMD64 architectures seamlessly with each run of our CI/CD workflow.

### Steps
1. **Deploy ECS Service via AWS UI:**
   - Navigate to the cluster provisioned in milestone 1 via the AWS UI.
   - Select "Services" and click "Create".
   - Configure the new service:
     - Select the family, choosing the task that ends in `-arm64`.
     - Enter the service name as `${clustername}-arm64`, replacing `${clustername}` with the name of your cluster.
     - Under the load balancing section, select "Application Load Balancer" and choose existing resources created in milestone one (load balancer, listener, target group).
   - Click "Create" to deploy the new ECS service.

2. **Update CircleCI Configuration:**
   - Modify the CircleCI configuration to incorporate the new ARM64 service information.
   - Ensure that the CircleCI workflow now includes steps for testing and deploying both ARM64 and AMD64 architectures.

3. **Verify Architecture and Docker Image Location:**
   - Navigate to the DNS name of the load balancer.
   - On the website, observe the architecture displayed.
   - Scroll down to the bottom of the demo app and click on "build info" to access further information about the architecture, build links to CircleCI, and build triggers.

### Objectives
- Deploy a new ECS service manually via the AWS UI, selecting the appropriate ARM64 task definition.
- Update the CircleCI configuration to accommodate the new ARM64 service, allowing for testing and deployment of both ARM64 and AMD64 architectures.
- Verify the architecture and Docker image location by accessing the DNS name of the load balancer and inspecting the website.
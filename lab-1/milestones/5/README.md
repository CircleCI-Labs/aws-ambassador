## Milestone 5: Exploring Multi-Architecture Images with Docker Manifests

### Overview
In this milestone, we delve into the realm of multi-architecture images, powered by Docker manifests. Docker manifests serve as a mechanism for amalgamating multiple architecture-specific images into a singular "meta" image, supporting diverse architectures seamlessly. With the emergence of ARM64 and the introduction of AWS Graviton offerings, customers now have the opportunity to capitalize on ARM64 for potential cost savings. However, a crucial question arises: how can customers effortlessly ensure their applications function seamlessly on ARM64?

Enter the concept of multi-architecture images. In this milestone, we embark on the journey of constructing such images, enabling us to harness the power of both AMD64 and ARM64 architectures.

### Steps
1. **Enable Docker Experimental Features:**
   - Configure Docker to enable experimental features, allowing interaction with Docker manifests.

2. **Publish Architecture-Specific Images to ECR:**
   - Publish individual architecture-specific images to our ECR instance, including both AMD64 and ARM64 versions.

3. **Construct Docker Manifest:**
   - Utilize Docker manifests to construct a unified image that references the architecture-specific images published to ECR.
   
4. **Redeploy ECS Instance with Multi-Architecture Support:**
   - Update the ECS deployment to leverage the newly created Docker manifest, ensuring compatibility across AMD64 and ARM64 architectures.

### Objectives
- Enable Docker experimental features to interact with Docker manifests effectively.
- Publish architecture-specific images for both AMD64 and ARM64 to the ECR instance.
- Construct a Docker manifest that references architecture-specific images, facilitating multi-architecture support.
- Redeploy the ECS instance, utilizing the newly created Docker manifest to ensure compatibility across diverse architectures.
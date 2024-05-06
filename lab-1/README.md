# AWS Ambassador - From Zero to Hero: Mastering CI/CD Pipelines with CircleCI 

Welcome to the first hands-on lab for the AWS Ambassador CircleCI program! This repository contains all the code needed to complete the lab titled "From Zero to Hero: Mastering CI/CD Pipelines with CircleCI." The focus of this lab is to familiarize users with the nuts and bolts of CircleCI, particularly the developer experience when onboarding a new project to CircleCI. Throughout the lab, participants will progress from setting up a brand new project on CircleCI to establishing a full production CI/CD pipeline.

## Prerequisites

To participate in this lab, you will need:

- CircleCI Account (You will be guided on how to sign up during the lab)
- AWS Account (Resources will be deployed in the lab via CloudFormation)
- GitHub Account (For forking this repository into your account)

## Milestones

In the repository, you will find the `milestones` folder, which contains each "version" of the CircleCI configuration needed to complete the lab. The first milestone contains the most basic configuration, while the last milestone contains the full production config. You can refer to the milestone folders as you progress through the lab to see what changes are needed to reach the next milestone.

To get started head to [milestone 1](./milestones/1/README.md)!

## Background

With the release of CircleCI's Arm executor, we can now build on multiple architectures via CircleCI's Cloud offering. Building on multiple architectures offers better performance/speed and ensures that your application will work on your platform.

While some examples show using Docker Buildx with QEMU, this can lead to issues with low-level languages appearing to work but failing when deployed on your platform. 

For this example, we will build a Python application, create Docker images for each architecture (arm64 and amd64), and construct a manifest to tie the Docker images together into a single tag. 


## CI/CD Setup

In this lab, we will utilize CircleCI's infrastructure to automate the build, test, and deployment processes for Docker images. We will primarily use the machine executor for both `amd64` and `arm64` architectures.

Our objectives for setting up CircleCI are as follows:

- **Triggering Builds:** Configure CircleCI to trigger builds on every commit to the `main` branch and every pull request on this repository.
- **Building the Flask Demo Container:** Build the Docker container for the Flask demo application.
- **Testing Flask Application:** Implement tests to ensure the Flask application functions correctly.
- **Testing the Container:** Validate the functionality of the Docker container.
- **Tagging and Pushing Images:** If tests pass successfully, tag the Docker images and push the architecture-specific images to Amazon Elastic Container Registry (ECR).
- **Creating Docker Manifests:** Create Docker manifests to enable users to pull down the image without needing to worry about architecture specifics.
- **Deploying New Images to ECS:** Deploy the new Docker images to Amazon Elastic Container Service (ECS).

Currently, the demo deploys a Flask-based website using Docker. The Flask server is load-balanced on multiple architectures, allowing users to observe architecture changes by refreshing the page.
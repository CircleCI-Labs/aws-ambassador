package org

import data.circleci.config
import future.keywords

policy_name["security_tool_enforcement"]

orbs := object.keys(config.orbs)
orbs_version := object.get(input, ["orbs"], {})

# Searches through all jobs looking for Snyk Orb Usage
snyk_jobs := {
    job_steps | walk(input, [path, value])
    path[_] == "steps"
    job_steps := value[_]
    job_steps["snyk/scan"]
}

# Searches through all jobs defined in the workflow looking for GitGuardian Job
gitguardian_workflows := {
    workflow | walk(input, [path, value])
    path[_] == "workflows"
    workflow = value["name"]
    startswith(workflow, "Scanning for Secrets with GitGuardian")
}

# Searches through all jobs defined in the workflow looking for Scan Image Job
scan_imge_workflows := {
    workflow | walk(input, [path, value])
    path[_] == "workflows"
    workflow = value["name"]
    startswith(workflow, "Scan << matrix.architecture >> Container Image")
}

snyk_version_is_present = reason {
    not "snyk/snyk@2.1.0" in orbs_version
    reason := "Orbs should include snyk/snyk@2.1.0"
}

ggshield_orb_is_present = reason {
    not "gitguardian/ggshield" in orbs
    reason := "Orbs should include gitguardian/ggshield"
}

scan_image_job_uses_snyk = reason {
    count(snyk_jobs) < 1
    reason := "Scan image job should use snyk/scan"
}

workflow_includes_gitguardian = reason {
    count(gitguardian_workflows) < 1
    reason := "Workflows should include a 'Scanning for Secrets with GitGuardian' job"
}

workflow_includes_scan_image = reason {
    count(scan_imge_workflows) < 1
    reason := "Workflows should include a 'Scan << matrix.architecture >> Container Image"
}

# Enable Rules
soft_fail["snyk_version_is_present"]
enable_rule["snyk_version_is_present"]

enable_hard["ggshield_orb_is_present"]
enable_hard["scan_image_job_uses_snyk"]
enable_hard["workflow_includes_gitguardian"]
enable_hard["workflow_includes_scan_image"]
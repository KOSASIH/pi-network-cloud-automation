from var import *
from google.cloud import governance_v1

client = governance_v1.PolicyControllerClient()
project_id = var.project

# Create a policy
policy_name = client.policy_path(project_id, 'my_policy')
policy = governance_v1.Policy(
    etag="\"012345678901234567890123456789\"",
    bindings=[
        governance_v1.Binding(
            role="roles/viewer",
            members=["user:jane@example.com"],
        ),
    ],
)
response = client.create_policy(policy_name, policy)
print("Policy created: ", response)

# Create a policy tag
tag_name = client.tag_path(project_id, 'my_tag')
tag = governance_v1.Tag(
    etag="\"012345678901234567890123456789\"",
    description="My tag description",
    display_name="My tag display name",
    resource_names=[
        "//cloudresourcemanager.googleapis.com/projects/my-project",
    ],
)
response = client.create_tag(tag_name, tag)
print("Tag created: ", response)

# Create a policy tag binding
policy_tag_binding_name = client.policy_tag_binding_path(project_id, 'my_policy', 'my_tag')
policy_tag_binding = governance_v1.PolicyTagBinding(
    etag="\"012345678901234567890123456789\"",
    policy=policy_name,
    tag=tag_name,
)
response = client.create_policy_tag_binding(policy_tag_binding_name, policy_tag_binding)
print("Policy tag binding created: ", response)

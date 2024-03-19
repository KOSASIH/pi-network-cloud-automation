import meraki

def delete_existing_port_forwarding_rules(api_key, network_id, public_port):
    """
    Deletes existing port forwarding rules for the same source port 22.
    """
    # Initialize the Meraki dashboard API
    dashboard = meraki.DashboardAPI(api_key)

    # Get the current port forwarding rules
    port_forwarding_rules = dashboard.appliance.getNetworkAppliancePortForwardingRules(networkId=network_id)

    # Check if there are any other port forwarding rules for the same source port 22
    for rule in port_forwarding_rules:
        if rule['publicPort'] == public_port:
            print(f"Deleting existing port forwarding rule for public port {public_port}")
            dashboard.appliance.deleteNetworkAppliancePortForwardingRule(networkId=network_id, portForwardingRuleId=rule['id'])

def pi_net_cloud_commander(api_key, network_id, vlan_id, public_port, local_port):
    """
    Commands the cloud for Pi Network operations with automated finesse.
    """
    # Delete any existing port forwarding rules for the same source port 22
    delete_existing_port_forwarding_rules(api_key, network_id, public_port)

    # Create a new port forwarding rule
    new_rule = {
        'comment': 'PiNetCloudCommander',
        'protocol': 'tcp',
        'publicPort': public_port,
        'localPort': local_port,
        'vlanId': vlan_id
    }

    # Add the new port forwarding rule
    dashboard.appliance.createNetworkAppliancePortForwardingRule(networkId=network_id, portForwardingRule=new_rule)
    print(f"Successfully added port forwarding rule for public port {public_port} and local port {local_port}")

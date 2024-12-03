import csv
import json

# Load the json data
with open('ce2_defaultOneTime_tn-SnV-2024-12-03T03-42-43_1.json') as config_file:
    data = json.load(config_file)

# Open a CSV file for writing
with open(f'Tenant_{data["fvTenant"]["attributes"]["name"]}.csv', 'w', newline='') as csv_file:
    # Define the header for the CSV
    header = [
       'vlan_id', 'vlan_name',
       'tenant', 'vrf', 'bdgw', 'bdmask'
       'bd_name', 'unicast',
       'appname', 'epgname',
       'PhysDom'
    ]

    # Create a CSV writer
    writer = csv.writer(csv_file)
    writer.writerow(header)

    # Loop through the children of fvTenant
    for child in data["fvTenant"]["children"]:
        if "fvBD" in child:
            # Extract tenant name
            tenant = data["fvTenant"]["attributes"]["name"]
            print(f"Tenant: {tenant}")

            # For Bridge Domain child
            for bd_child in child['fvBD']['children']:
                if 'fvRsCtx' in bd_child:
                    vrf = bd_child['fvRsCtx']['attributes']['tnFvCtxName']
                    print(f"VRF name: {vrf}")
                    writer.writerow([vrf])

                if 'fvSubnet' in bd_child:
                    try:
                      bdgw = bd_child['fvSubnet']['attributes']['ip'].split()[0]
                      bdmask = bd_child['fvSubnet']['attributes']['ip'].split()[1]
                      print(f"{bdgw},{bdmask}")
                    except KeyError as e:
                      bdmask == None

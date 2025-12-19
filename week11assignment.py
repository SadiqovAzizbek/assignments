def provision_server(clients_db, server_tiers, client_name, tier, months):
    if client_name not in clients_db:
        raise KeyError("Client unknown")
    if tier not in server_tiers:
        raise KeyError("Tier does not exist")
    if type(months) != int or months < 1:
        raise ValueError("Contract length invalid")
    monthly_cost = server_tiers[tier]["cost"]
    discount = server_tiers[tier]["discount"]
    total_cost = months * monthly_cost
    if months >= 12:
        total_cost -= discount
    if clients_db[client_name]["budget"] < total_cost:
        raise ValueError("Budget exceeded")
    clients_db[client_name]["budget"] -= total_cost
    return float(total_cost)

def run_provisioning(clients_db, server_tiers, request_list):
    contract_value = 0.0
    errors_logged = 0
    for client, tier, months in request_list:
        try:
            cost = provision_server(clients_db, server_tiers, client, tier, months)
            contract_value += cost
        except Exception as e:
            print(f"Provisioning Failed: {e}")
            errors_logged += 1
    return {
        "contract_value": contract_value,
        "errors_logged": errors_logged
    }

tiers = {
    "Basic": {"cost": 10.0, "discount": 10.0},
    "Pro":   {"cost": 50.0, "discount": 50.0}
}

clients = {
    "StartupCo": {"budget": 200.0},
    "MegaCorp":  {"budget": 1000.0}
}

requests = [
    ("StartupCo", "Basic", 12),
    ("StartupCo", "Pro", 5),    
    ("MegaCorp", "Ultra", 1),    
    ("GhostLLC", "Basic", 1),   
    ("MegaCorp", "Pro", 0.5)     
]

a = run_provisioning(clients, tiers, requests)
print(a)
from ape import accounts, project, networks


def main():
    acct = accounts.load("deployer_account")
    compass = "0xDcBd07EEC1D48aE0A14E61dD09BB5AA9c7ed391d"
    weth = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
    asset = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
    router = "0xF0d4c12A5768D806021F80a262B4d39d26C58b8D"
    pool = "0x87870Bca3F3fD6335C3F4ce8392D69350B4fA4E2"
    refund_wallet = "0x6dc0A87638CD75Cc700cCdB226c7ab6C054bc70b"
    entrance_fee = 40_000_000_000_000_000  # 100$
    service_fee_collector = "0xe693603C9441f0e645Af6A5898b76a60dbf757F4"
    service_fee = 500_000_000_000_000  # 0.05%
    priority_fee = int(0.01e9)
    base_fee = int(networks.active_provider.base_fee * 1.2 + priority_fee)
    vault = project.vault.deploy(
        compass, weth, asset, router, pool,  refund_wallet, entrance_fee,
        service_fee_collector, service_fee, max_fee=base_fee,
        max_priority_fee=priority_fee, sender=acct)

    print(vault)

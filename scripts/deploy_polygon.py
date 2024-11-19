from ape import accounts, project


def main():
    acct = accounts.load("deployer_account")
    compass = "0x26f5Da70095d69103ba8b2Ee264A20cD4B590EAb"
    weth = "0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270"
    asset = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"
    router = "0x0DCDED3545D565bA3B19E683431381007245d983"
    pool = "0x794a61358D6845594F94dc1DB02A252b5b4814aD"
    refund_wallet = "0x6dc0A87638CD75Cc700cCdB226c7ab6C054bc70b"
    entrance_fee = 320_000_000_000_000_000_000  # 100$
    service_fee_collector = "0xe693603C9441f0e645Af6A5898b76a60dbf757F4"
    service_fee = 500_000_000_000_000  # 0.05%
    vault = project.vault.deploy(
        compass, weth, asset, router, pool,  refund_wallet, entrance_fee,
        service_fee_collector, service_fee, sender=acct)

    print(vault)

# 0xeE8338Ee133B6705a7144a407eeB64Bf742B78f9
# 0xF6f6895CfF43172818c43310a3C22d43c453344a

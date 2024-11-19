from ape import accounts, project


def main():
    acct = accounts.load("deployer_account")
    compass = "0xEf2e3E09bCb5d1647D40E811D0396629549d16Ab"
    weth = "0xe91D153E0b41518A2Ce8Dd3D7944Fa863463a97d"
    asset = "0xDDAfbb505ad214D7b80b1f830fcCc89B60fb7A83"
    router = "0x0DCDED3545D565bA3B19E683431381007245d983"
    pool = "0xb50201558B00496A145fE76f7424749556E326D8"
    refund_wallet = "0x6dc0A87638CD75Cc700cCdB226c7ab6C054bc70b"
    entrance_fee = 100_000_000_000_000_000_000  # 100$
    service_fee_collector = "0xe693603C9441f0e645Af6A5898b76a60dbf757F4"
    service_fee = 500_000_000_000_000  # 0.05%
    vault = project.vault.deploy(
        compass, weth, asset, router, pool,  refund_wallet, entrance_fee,
        service_fee_collector, service_fee, sender=acct)

    print(vault)

# 0xaA79eD113b5f14565fB5A200Cfa28E1FbDb94EF5
# 0x2049e8Dcba698f2D6127E1f3e423D2278A1538d2

from ape import accounts, project


def main():
    acct = accounts.load("deployer_account")
    compass = "0x5a7A8fAf7f73063b4F175E4eF354B6426aF3bd52"
    weth = "0x4200000000000000000000000000000000000006"
    asset = "0x0b2C639c533813f4Aa9D7837CAf62653d097Ff85"
    router = "0x0DCDED3545D565bA3B19E683431381007245d983"
    pool = "0x794a61358D6845594F94dc1DB02A252b5b4814aD"
    refund_wallet = "0x6dc0A87638CD75Cc700cCdB226c7ab6C054bc70b"
    entrance_fee = 40_000_000_000_000_000  # 100$
    service_fee_collector = "0xe693603C9441f0e645Af6A5898b76a60dbf757F4"
    service_fee = 500_000_000_000_000  # 0.05%
    vault = project.vault.deploy(
        compass, weth, asset, router, pool,  refund_wallet, entrance_fee,
        service_fee_collector, service_fee, sender=acct)

    print(vault)

# 0xE105DA50a007246255cf91B42a82dd9FF5971243
# 0xaA79eD113b5f14565fB5A200Cfa28E1FbDb94EF5

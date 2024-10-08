from ape import accounts, project


def main():
    acct = accounts.load("deployer_account")
    compass = "0x82Ed642F4067D55cE884e2823951baDfEdC89e73"
    weth = "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1"
    asset = "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9"
    router = "0xF0d4c12A5768D806021F80a262B4d39d26C58b8D"
    pool = "0x794a61358D6845594F94dc1DB02A252b5b4814aD"
    refund_wallet = "0x6dc0A87638CD75Cc700cCdB226c7ab6C054bc70b"
    entrance_fee = 40_000_000_000_000_000  # 100$
    service_fee_collector = "0xe693603C9441f0e645Af6A5898b76a60dbf757F4"
    service_fee = 500_000_000_000_000  # 0.05%
    vault = project.vault.deploy(
        compass, weth, asset, router, pool,  refund_wallet, entrance_fee,
        service_fee_collector, service_fee, sender=acct)

    print(vault)

# 0xc742904b04193D36b1f93255f98dc9eD2CA4C2AA

from ape import accounts, project


def main():
    acct = accounts.load("deployer_account")
    compass = "0x042Ab4cd2897BA02a420146af8d95f161A4230F1"
    weth = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
    asset = "0x55d398326f99059ff775485246999027b3197955"
    router = "0xA72C85C258A81761433B4e8da60505Fe3Dd551CC"
    pool = "0x6807dc923806fE8Fd134338EABCA509979a7e0cB"
    refund_wallet = "0x6dc0A87638CD75Cc700cCdB226c7ab6C054bc70b"
    entrance_fee = 170_000_000_000_000_000  # 100$
    service_fee_collector = "0xe693603C9441f0e645Af6A5898b76a60dbf757F4"
    service_fee = 500_000_000_000_000  # 0.05%
    vault = project.vault.deploy(
        compass, weth, asset, router, pool,  refund_wallet, entrance_fee,
        service_fee_collector, service_fee, sender=acct)

    print(vault)

# 0xf5A21C45815b2801B00FdB5E7047BFDE97152040
# 0x849FB2fDE454627f7c1989e60937982FABA70EfB

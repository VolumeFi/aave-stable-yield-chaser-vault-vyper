from ape import accounts, project


def main():
    acct = accounts.load("deployer_account")
    compass = "0x7cd976c5029FDA0dF0124490d00D7fBa25a64E19"
    weth = "0x4200000000000000000000000000000000000006"
    asset = "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913"
    router = "0x4f37A9d177470499A2dD084621020b023fcffc1F"
    pool = "0xA238Dd80C259a72e81d7e4664a9801593F98d1c5"
    refund_wallet = "0x6dc0A87638CD75Cc700cCdB226c7ab6C054bc70b"
    entrance_fee = 40_000_000_000_000_000  # 100$
    service_fee_collector = "0xe693603C9441f0e645Af6A5898b76a60dbf757F4"
    service_fee = 500_000_000_000_000  # 0.05%
    vault = project.vault.deploy(
        compass, weth, asset, router, pool,  refund_wallet, entrance_fee,
        service_fee_collector, service_fee, sender=acct)

    print(vault)

# 0x88d48dAFf4F0da7DCD774D5B31A0a90A07283882
# 0x4495467f9cD04faF5fa65ed34AF335d4e2e7e129

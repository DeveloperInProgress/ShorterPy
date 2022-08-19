from pkgutil import pkgutil


def get_abi(contract_name: str):
    """
    Get the abi for a contract
    Args:
        contract_name: The name of the contract
    """
    return pkgutil.get_data(__name__, f"./abi/{contract_name}.json").decode("utf-8")

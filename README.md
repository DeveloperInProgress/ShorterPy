# ShorterPy
A Python SDK for Shorter

## Installation

From PyPi

```
pip install shorter-py
```

## Documentation

Complete documentation coming soon

## Example Usage

The following examples shows how to use this packages in different use cases

### Create an APIProvider

```
from shorterpy.api.apiProvider import ApiProvider, Network
from eth_account import Account

acc = Account.from_key(<PRIVATE_KEY_HERE>)
api = ApiProvider(
        <RINKEBY_RPC_URL>, 
        Network.RINKEBY,
        acc
    )

```

### Provider Usecase

#### Create a Pool Proposal

Creating a pool proposal requires you to call `createPoolProposal` function in `Committee` contract. This function requires you to pay 10000 IPISTR tokens.
First, approve `Committee` to use 10000 IPISTR from your account:

```
from shorterpy.contracts.erc20 import ERC20
from shorterpy.common.types import GasParams

#Create IPISTR Token contract object
ipistr = ERC20(api, Web3.toChecksumAddress('0x7b113F4e8b55f812eC52B83313f6354364204DB2'))

#Create GasParams object, containing details about gas to be uses
gas_params = GasParams(gas=1000000, max_fee_per_gas=Web3.toWei(2, 'gwei'), max_priority_fee_per_gas=Web3.toWei(2, 'gwei'))

#Send a transaction to approve Committee contract to use 10000 IPISTRs, the transaction will be signed automatically by the ApiProvider
tx_receipt = ipistr.approve(ADDRESSES[Network.RINKEBY.name]['ICommittee'], 10000*(10**18), gas_params)

```

Then, send a transaction to create pool proposal

```
from shorterpy.contracts.committee import Committee

#Create Committee contract object
committee = Committee(api)

#Create GasParams object, containing details about gas to be uses
gas_params = GasParams(gas=1000000, max_fee_per_gas=Web3.toWei(2, 'gwei'), max_priority_fee_per_gas=Web3.toWei(2, 'gwei'))

#Send a transaction to create pool proposal function: Committee.createPoolProposal(staked_token, leverage, duration_days, gas_params)
tx_receipt = committee.createPoolProposal(<STAKED_TOKEN_ADDRESS>, 5, 30, gas_params)
```

#### Deposit And Withdraw

Providers can deposit into a pool and withdraw from it, using the StrPool contract object.

A StrPool contract object can be created with the following syntax:

```
from shorterpy.contracts.strPool import StrPool

strPool = StrPool(api, <POOL_ADDRESS>)
```

The pool address paramater is required to connect it to the required StrPool

The deposit and withdrawal is made through the token related with the pool. So, it is necessary to approve the pool to use
the required amount of tokens to make a deposit. 

```
from shorterpy.contracts.erc20 import ERC20
from shorterpy.common.types import GasParams

#Create Token contract object
token = ERC20(api, Web3.toChecksumAddress(<TOKEN_ADDRESS>))

#Create GasParams object, containing details about gas to be uses
gas_params = GasParams(gas=1000000, max_fee_per_gas=Web3.toWei(2, 'gwei'), max_priority_fee_per_gas=Web3.toWei(2, 'gwei'))

#Send a transaction to approve Committee contract to use 10000 IPISTRs, the transaction will be signed automatically by the ApiProvider
tx_receipt = token.approve(<POOL_ADDRESS>, <AMOUNT_TO_DEPOSIT>, gas_params)
```

Then, the deposit can be made by calling `strPool.deposit()` function

```
#Create GasParams object, containing details about gas to be uses
gas_params = GasParams(gas=1000000, max_fee_per_gas=Web3.toWei(2, 'gwei'), max_priority_fee_per_gas=Web3.toWei(2, 'gwei'))

tx_receipt = strPool.deposit(<AMOUNT_TO_DEPOSIT>, gas_params)
```

Withdrawal can be made by calling `strPool.withdraw()` function

```
tx_receipt = strPool.withdraw(<PERCENTAGE_TO_WITHDRAW>, <AMOUNT_TO_WITDRAW>, gas_params)
```


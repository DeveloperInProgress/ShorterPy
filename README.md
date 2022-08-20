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
#Create IPISTR Token contract object
ipistr = ERC20(api, Web3.toChecksumAddress('0x7b113F4e8b55f812eC52B83313f6354364204DB2'))

#Create GasParams object, containing details about gas to be uses
gas_params = GasParams(gas=1000000, max_fee_per_gas=Web3.toWei(2, 'gwei'), max_priority_fee_per_gas=Web3.toWei(2, 'gwei'))

#Send a transaction to approve Committee contract to use 10000 IPISTRs, the transaction will be signed automatically by the ApiProvider
print(ipistr.approve(ADDRESSES[Network.RINKEBY.name]['ICommittee'], 10000*(10**18), gas_params))

```

Then, send a transaction to create pool proposal

```

```

```
from shorterpy.contracts.poolGuardian import PoolGuardian

pg = PoolGuardian(api)  #create a PoolGuardian contract object

```

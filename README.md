# ethstaker-deposit-cli

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Introduction](#introduction)
- [Tutorial for users](#tutorial-for-users)
  - [Build requirements](#build-requirements)
  - [For Linux or MacOS users](#for-linux-or-macos-users)
    - [File Permissions](#file-permissions)
    - [Option 1. Download binary executable file](#option-1-download-binary-executable-file)
      - [Step 1. Installation](#step-1-installation)
      - [Step 2. Create keys and `deposit_data-*.json`](#step-2-create-keys-and-deposit_data-json)
        - [`language` Argument](#language-argument)
        - [`--non_interactive` flag](#--non_interactive-flag)
        - [`--ignore_connectivity` flag](#--ignore_connectivity-flag)
        - [Commands](#commands)
        - [`new-mnemonic` Arguments](#new-mnemonic-arguments)
        - [`existing-mnemonic` Arguments](#existing-mnemonic-arguments)
        - [Successful message](#successful-message)
        - [`generate-bls-to-execution-change` Arguments](#generate-bls-to-execution-change-arguments)
        - [`generate-bls-to-execution-change-keystore` Arguments](#generate-bls-to-execution-change-keystore-arguments)
        - [`exit-transaction-keystore` Arguments](#exit-transaction-keystore-arguments)
        - [`exit-transaction-mnemonic` Arguments](#exit-transaction-mnemonic-arguments)
    - [Option 2. Build `deposit-cli` with native Python](#option-2-build-deposit-cli-with-native-python)
      - [Step 0. Python version checking](#step-0-python-version-checking)
      - [Step 1. Installation](#step-1-installation-1)
      - [Step 2. Create keys and `deposit_data-*.json`](#step-2-create-keys-and-deposit_data-json-1)
        - [Language Argument](#language-argument)
        - [Commands](#commands-1)
        - [Arguments](#arguments)
        - [Successful message](#successful-message-1)
    - [Option 3. Build `deposit-cli` with `virtualenv`](#option-3-build-deposit-cli-with-virtualenv)
      - [Step 0. Python version checking](#step-0-python-version-checking-1)
      - [Step 1. Installation](#step-1-installation-2)
      - [Step 2. Create keys and `deposit_data-*.json`](#step-2-create-keys-and-deposit_data-json-2)
        - [Language Argument](#language-argument-1)
        - [Commands](#commands-2)
        - [Arguments](#arguments-1)
    - [Option 4. Use published docker image](#option-4-use-published-docker-image)
      - [Step 1. Pull the official docker image](#step-1-pull-the-official-docker-image)
      - [Step 2. Create keys and `deposit_data-*.json`](#step-2-create-keys-and-deposit_data-json-3)
    - [Option 5. Use local docker image](#option-5-use-local-docker-image)
      - [Step 1. Build the docker image](#step-1-build-the-docker-image)
      - [Step 2. Create keys and `deposit_data-*.json`](#step-2-create-keys-and-deposit_data-json-4)
        - [Arguments](#arguments-2)
        - [Successful message](#successful-message-2)
  - [For Windows users](#for-windows-users)
    - [Option 1. Download binary executable file](#option-1-download-binary-executable-file-1)
      - [Step 1. Installation](#step-1-installation-3)
      - [Step 2. Create keys and `deposit_data-*.json`](#step-2-create-keys-and-deposit_data-json-5)
        - [Language Argument](#language-argument-2)
        - [Commands](#commands-3)
        - [Arguments](#arguments-3)
    - [Option 2. Build `deposit-cli` with native Python](#option-2-build-deposit-cli-with-native-python-1)
      - [Step 0. Python version checking](#step-0-python-version-checking-2)
      - [Step 1. Installation](#step-1-installation-4)
      - [Step 2. Create keys and `deposit_data-*.json`](#step-2-create-keys-and-deposit_data-json-6)
        - [Language Argument](#language-argument-3)
        - [Commands](#commands-4)
        - [Arguments](#arguments-4)
    - [Option 3. Build `deposit-cli` with `virtualenv`](#option-3-build-deposit-cli-with-virtualenv-1)
      - [Step 0. Python version checking](#step-0-python-version-checking-3)
      - [Step 1. Installation](#step-1-installation-5)
      - [Step 2. Create keys and `deposit_data-*.json`](#step-2-create-keys-and-deposit_data-json-7)
        - [Language Argument](#language-argument-4)
        - [Commands](#commands-5)
        - [Arguments](#arguments-5)
- [Development](#development)
  - [Install basic requirements](#install-basic-requirements)
  - [Install testing requirements](#install-testing-requirements)
  - [Run tests](#run-tests)
  - [Run the app](#run-the-app)
  - [Building Binaries](#building-binaries)
      - [Mac M1 Binaries](#mac-m1-binaries)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Introduction

`ethstaker-deposit-cli` is a tool for creating [EIP-2335 format](https://eips.ethereum.org/EIPS/eip-2335) BLS12-381 keystores and a corresponding `deposit_data*.json` file for [Ethereum Staking Launchpad](https://github.com/ethereum/staking-launchpad). One can also provide a keystore file to generate a `signed_exit_transaction*.json` file to be broadcast at a later date to exit a validator.

- **Warning: Please generate your keystores on your own safe, completely offline device.**
- **Warning: Please backup your mnemonic, keystores, and password securely.**

Please read [Launchpad Validator FAQs](https://launchpad.ethereum.org/faq#keys) before generating the keys.

You can find the audit report by Trail of Bits [here](https://github.com/trailofbits/publications/blob/master/reviews/ETH2DepositCLI.pdf).

## Tutorial for users

### Build requirements

- [Python **3.9+**](https://www.python.org/about/gettingstarted/)
- [pip3](https://pip.pypa.io/en/stable/installing/)

### For Linux or MacOS users

#### File Permissions

On Unix-based systems, keystores and the `deposit_data*.json` have `440`/`-r--r-----` file permissions (user & group read only). This improves security by limiting which users and processes that have access to these files. If you are getting `permission denied` errors when handling your keystores, consider changing which user/group owns the file (with `chown`) or, if need be, change the file permissions with `chmod`.

#### Option 1. Download binary executable file

##### Step 1. Installation

See [releases page](https://github.com/eth-educators/ethstaker-deposit-cli/releases) to download and decompress the corresponding binary files.

##### Step 2. Create keys and `deposit_data-*.json`

Run the following command to enter the interactive CLI and generate keys from a new mnemonic:

```sh
./deposit new-mnemonic
```

or run the following command to enter the interactive CLI and generate keys from an existing:

```sh
./deposit existing-mnemonic
```

###### `language` Argument

The Launchpad offers many language/internationalization options. If you wish to select one as a CLI argument, it must be passed in before one of the commands is chosen.

| Argument | Type | Description |
| -------- | -------- | -------- |
| `--language` | String. Options: `العربية`, `ελληνικά`, `English`, `Français`, `Bahasa melayu`, `Italiano`, `日本語`, `한국어`, `Português do Brasil`, `român`, `简体中文`. Default to `English` | The language you wish to use the CLI in. |

###### `--non_interactive` flag

**Warning: With this flag, there will be no confirmation step(s) to verify the input value(s). This will also ignore the connectivity check. Please use it carefully.**

| Argument | Type | Description |
| -------- | -------- | -------- |
| `--non_interactive` | Flag | Run CLI in non-interactive mode. |

###### `--ignore_connectivity` flag

**Warning: It is strongly recommended not to use this tool with internet access. Ignoring this check can further the risk of theft and compromise of your generated key material.**

| Argument | Type | Description |
| -------- | -------- | -------- |
| `--ignore_connectivity` | Flag | Skip internet connectivity check and warning. |

###### Commands

The CLI offers different commands depending on what you want to do with the tool.

| Command | Description |
| ------- | ----------- |
| `new-mnemonic` | (Recommended) This command is used to generate keystores with a new mnemonic. |
| `existing-mnemonic` | This command is used to re-generate or derive new keys from your existing mnemonic. Use this command, if (i) you have already generated keys with this CLI before, (ii) you want to reuse your mnemonic that you know is secure that you generated elsewhere (reusing your eth wallet mnemonic .etc), or (iii) you lost your keystores and need to recover your keys. |
| `generate-bls-to-execution-change` | This command is used to generate BLS to execution address change message. This is used to add a withdrawal address to a validator that does not currently have one. |
| `generate-bls-to-execution-change-keystore` | This command is used to sign a BLS to execution address change message with the provided validator key. This is used for a proposed solution to update withdrawal credentials for users who have lost their mnemonic. |
| `exit-transaction-keystore` | This command is used to create an exit transaction using a keystore file. |
| `exit-transaction-mnemonic` | This command is used to create an exit transaction using a mnemonic phrase. |

###### `new-mnemonic` Arguments

You can use `new-mnemonic --help` to see all arguments. Note that if there are missing arguments that the CLI needs, it will ask you for them.

| Argument | Type | Description |
| -------- | -------- | -------- |
| `--num_validators`  | Non-negative integer | The number of signing keys you want to generate. Note that the child key(s) are generated via the same master key. |
| `--mnemonic_language` | String. Options: `简体中文`, `繁體中文`, `český jazyk`, `English`, `Italiano`, `한국어`, `Português`, `Español`. Default to `English` | The language of the mnemonic word list |
| `--folder` | String. Pointing to `./validator_keys` by default | The folder path for the keystore(s) and deposit(s) |
| `--chain` | String. `mainnet` by default | The chain setting for the signing domain. |
| `--withdrawal_address` | String. Ethereum execution address in hexadecimal encoded form | If this field is set and valid, the given execution address will be used to create the withdrawal credentials. Otherwise, it will generate withdrawal credentials with the mnemonic-derived withdrawal public key in [ERC-2334 format](https://eips.ethereum.org/EIPS/eip-2334#eth2-specific-parameters). |
| `--pbkdf2` | Flag | Will use pbkdf2 key derivation instead of scrypt for generated keystore files as defined in EIP-2335. This can be a good alternative if you intend to work with a large number of keys. |

###### `existing-mnemonic` Arguments

You can use `existing-mnemonic --help` to see all arguments. Note that if there are missing arguments that the CLI needs, it will ask you for them.

| Argument | Type | Description |
| -------- | -------- | -------- |
| `--validator_start_index` | Non-negative integer | The index of the first validator's keys you wish to generate. If this is your first time generating keys with this mnemonic, use 0. If you have generated keys using this mnemonic before, use the next index from which you want to start generating keys from. As an example if you've generated 4 keys before (keys #0, #1, #2, #3), then enter 4 here.|
| `--num_validators`  | Non-negative integer | The number of new signing keys you want to generate. Note that the child key(s) are generated via the same master key. |
| `--folder` | String. Pointing to `./validator_keys` by default | The folder path for the keystore(s) and deposit(s) |
| `--chain` | String. `mainnet` by default | The chain setting for the signing domain. |
| `--withdrawal_address` | String. Ethereum execution address in hexadecimal encoded form | If this field is set and valid, the given execution address will be used to create the withdrawal credentials. Otherwise, it will generate withdrawal credentials with the mnemonic-derived withdrawal public key in [ERC-2334 format](https://eips.ethereum.org/EIPS/eip-2334#eth2-specific-parameters). |
| `--pbkdf2` | Flag | Will use pbkdf2 key derivation instead of scrypt for generated keystore files as defined in EIP-2335. This can be a good alternative if you intend to work with a large number of keys. |

###### Successful message

You will see the following messages after successfully generated the keystore(s) and the deposit(s):

```text
Creating your keys:               [####################################]  <N>/<N>
Creating your keystores:          [####################################]  <N>/<N>
Creating your depositdata:        [####################################]  <N>/<N>
Verifying your keystores:         [####################################]  <N>/<N>
Verifying your deposits:          [####################################]  <N>/<N>

Success!
Your keys can be found at: <YOUR_FOLDER_PATH>
```

###### `generate-bls-to-execution-change` Arguments

You can use `generate-bls-to-execution-change --help` to see all arguments. Note that if there are missing arguments that the CLI needs, it will ask you for them.

| Argument | Type | Description |
| -------- | -------- | -------- |
| `--bls_to_execution_changes_folder` | String. Pointing to `./bls_to_execution_changes` by default | The folder path for the `bls_to_execution_change-*` JSON file(s) |
| `--chain` | String. `mainnet` by default | The chain setting for the signing domain. |
| `--mnemonic` | String. mnemonic split by space.  | The mnemonic you used to create withdrawal credentials. |
| `--mnemonic_password` | Optional string. Empty by default. | The mnemonic password you used in your key generation. Note: It's not the keystore password. |
| `--validator_start_index` | Non-negative integer | The index position for the keys to start generating withdrawal credentials in [ERC-2334 format](https://eips.ethereum.org/EIPS/eip-2334#eth2-specific-parameters). |
| `--validator_indices` | String of integer(s) | A list of the chosen validator index number(s) as identified on the beacon chain. Split multiple items with whitespaces or commas. |
| `--bls_withdrawal_credentials_list` | String of hexstring(s). | A list of the old BLS withdrawal credentials of the given validator(s). It is for confirming you are using the correct keys. Split multiple items with whitespaces or commas. |
| `--withdrawal_address` | String. Ethereum execution address in hexadecimal encoded form | If this field is set and valid, the given execution address will be used to create the withdrawal credentials. Otherwise, it will generate withdrawal credentials with the mnemonic-derived withdrawal public key in [ERC-2334 format](https://eips.ethereum.org/EIPS/eip-2334#eth2-specific-parameters). |
| `--devnet_chain_setting` | String. JSON string `'{"network_name": "<NETWORK_NAME>", "genesis_fork_version": "<GENESIS_FORK_VERSION>", "exit_fork_version": "<EXIT_FORK_VERSION>", "genesis_validator_root": "<GENESIS_VALIDATOR_ROOT>"}'` | The custom chain setting of a devnet or testnet. Note that it will override your `--chain` choice. |

###### `generate-bls-to-execution-change-keystore` Arguments

You can use `generate-bls-to-execution-change-keystore --help` to see all arguments. Note that if there are missing arguments that the CLI needs, it will ask you for them.

| Argument | Type | Description |
| -------- | -------- | -------- |
| `--chain` | String. `mainnet` by default | The chain setting for the signing domain. |
| `--keystore` | File | The keystore file associating with the validator you wish to sign with. This keystore file should match the provided validator index. |
| `--keystore_password` | String | The password that is used to encrypt the provided keystore. Note: It's not your mnemonic password. |
| `--validator_index` | Integer | The validator index corresponding to the provided keystore. |
| `--withdrawal_address` | String. Ethereum execution address in hexadecimal encoded form that you wish to set as your withdrawal credentials. |
| `--output_folder` | String. Pointing to `./bls_to_execution_changes_keystore` by default | The folder path for the `signed_exit_transaction-*` JSON file |
| `--devnet_chain_setting` | String. JSON string `'{"network_name": "<NETWORK_NAME>", "genesis_fork_version": "<GENESIS_FORK_VERSION>", "exit_fork_version": "<EXIT_FORK_VERSION>", "genesis_validator_root": "<GENESIS_VALIDATOR_ROOT>"}'` | The custom chain setting of a devnet or testnet. Note that it will override your `--chain` choice. |

###### `exit-transaction-keystore` Arguments

You can use `exit-transaction-keystore --help` to see all arguments. Note that if there are missing arguments that the CLI needs, it will ask you for them.

| Argument | Type | Description |
| -------- | -------- | -------- |
| `--chain` | String. `mainnet` by default | The chain setting for the signing domain. |
| `--keystore` | File | The keystore file associating with the validator you wish to exit. |
| `--keystore_password` | String | The password that is used to encrypt the provided keystore. Note: It's not your mnemonic password. |
| `--validator_index` | Integer | The validator index corresponding to the provided keystore. |
| `--epoch` | Optional integer. 0 by default | The epoch of when the exit transaction will be valid. The transaction will always be valid by default. |
| `--output_folder` | String. Pointing to `./exit_transaction` by default | The folder path for the `signed_exit_transaction-*` JSON file |

###### `exit-transaction-mnemonic` Arguments

You can use `exit-transaction-mnemonic --help` to see all arguments. Note that if there are missing arguments that the CLI needs, it will ask you for them.

| Argument | Type | Description |
| -------- | -------- | -------- |
| `--chain` | String. `mainnet` by default | The chain setting for the signing domain. |
| `--mnemonic` | String. mnemonic split by space.  | The mnemonic you used during key generation. |
| `--mnemonic_password` | Optional string. Empty by default. | The mnemonic password you used in your key generation. Note: It's not the keystore password. |
| `--validator_start_index` | Non-negative integer | The index position for the keys to start generating keystores in [ERC-2334 format](https://eips.ethereum.org/EIPS/eip-2334#eth2-specific-parameters). |
| `--validator_indices` | String of integer(s) | A list of the chosen validator index number(s) as identified on the beacon chain. Split multiple items with whitespaces or commas. |
| `--epoch` | Optional integer. 0 by default | The epoch of when the exit transaction will be valid. The transaction will always be valid by default. |
| `--output_folder` | String. Pointing to `./exit_transaction` by default | The folder path for the `signed_exit_transaction-*` JSON file |

#### Option 2. Build `deposit-cli` with native Python

##### Step 0. Python version checking

Ensure you are using Python version >= Python3.9:

```sh
python3 -V
```

##### Step 1. Installation

Install the dependencies:

```sh
pip3 install -r requirements.txt
```

Or use the helper script:

```sh
./deposit.sh install
```

##### Step 2. Create keys and `deposit_data-*.json`

Run one of the following command to enter the interactive CLI:

```sh
./deposit.sh new-mnemonic
```

or

```sh
./deposit.sh existing-mnemonic
```

You can also run the tool with optional arguments:

```sh
./deposit.sh new-mnemonic --num_validators=<NUM_VALIDATORS> --mnemonic_language=english --chain=<CHAIN_NAME> --folder=<YOUR_FOLDER_PATH>
```

```sh
./deposit.sh existing-mnemonic --num_validators=<NUM_VALIDATORS> --validator_start_index=<START_INDEX> --chain=<CHAIN_NAME> --folder=<YOUR_FOLDER_PATH>
```

###### Language Argument

See [here](#language_argument) for `--language` arguments.
###### Commands

See [here](#commands)

###### Arguments

See [here](#new-mnemonic-arguments) for `new-mnemonic` arguments\
See [here](#existing-mnemonic-arguments) for `existing-mnemonic` arguments\
See [here](#generate-bls-to-execution-change-arguments) for `generate-bls-to-execution-change` arguments\
See [here](#generate-bls-to-execution-change-keystore-arguments) for `generate-bls-to-execution-change-keystore` arguments\
See [here](#exit-transaction-keystore-arguments) for `exit-transaction-keystore` arguments\
See [here](#exit-transaction-mnemonic-arguments) for `exit-transaction-mnemonic` arguments

###### Successful message
See [here](#successful-message)

#### Option 3. Build `deposit-cli` with `virtualenv`

##### Step 0. Python version checking

Ensure you are using Python version >= Python3.9:

```sh
python3 -V
```

##### Step 1. Installation

For the [virtualenv](https://virtualenv.pypa.io/en/latest/) users, you can create a new venv:

```sh
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
```

and install the dependencies:

```sh
pip3 install -r requirements.txt
```

##### Step 2. Create keys and `deposit_data-*.json`

Run one of the following command to enter the interactive CLI:

```sh
python3 -m ethstaker_deposit new-mnemonic
```

or

```sh
python3 -m ethstaker_deposit existing-mnemonic
```

You can also run the tool with optional arguments:

```sh
python3 -m ethstaker_deposit new-mnemonic --num_validators=<NUM_VALIDATORS> --mnemonic_language=english --chain=<CHAIN_NAME> --folder=<YOUR_FOLDER_PATH>
```

```sh
python3 -m ethstaker_deposit existing-mnemonic --num_validators=<NUM_VALIDATORS> --validator_start_index=<START_INDEX> --chain=<CHAIN_NAME> --folder=<YOUR_FOLDER_PATH>
```

###### Language Argument

See [here](#language_argument) for `--language` arguments.

###### Commands

See [here](#commands)

###### Arguments

See [here](#new-mnemonic-arguments) for `new-mnemonic` arguments\
See [here](#existing-mnemonic-arguments) for `existing-mnemonic` arguments\
See [here](#generate-bls-to-execution-change-arguments) for `generate-bls-to-execution-change` arguments\
See [here](#generate-bls-to-execution-change-keystore-arguments) for `generate-bls-to-execution-change-keystore` arguments\
See [here](#exit-transaction-keystore-arguments) for `exit-transaction-keystore` arguments\
See [here](#exit-transaction-mnemonic-arguments) for `exit-transaction-mnemonic` arguments

#### Option 4. Use published docker image

##### Step 1. Pull the official docker image

Run the following command to pull the latest docker image published on the Github repository:

```sh
docker pull ghcr.io/eth-educators/ethstaker-deposit-cli:latest
```

##### Step 2. Create keys and `deposit_data-*.json`

Run the following command to enter the interactive CLI:

```sh
docker run -it --rm -v $(pwd)/validator_keys:/app/validator_keys ghcr.io/eth-educators/ethstaker-deposit-cli:latest
```

You can also run the tool with optional arguments:

```sh
docker run -it --rm -v $(pwd)/validator_keys:/app/validator_keys ghcr.io/eth-educators/ethstaker-deposit-cli:latest new-mnemonic --num_validators=<NUM_VALIDATORS> --mnemonic_language=english
```

Example for 1 validator on the [Holesky testnet](https://holesky.launchpad.ethereum.org/) using english:

```sh
docker run -it --rm -v $(pwd)/validator_keys:/app/validator_keys ghcr.io/eth-educators/ethstaker-deposit-cli:latest new-mnemonic --num_validators=1 --mnemonic_language=english --chain=holesky
```

#### Option 5. Use local docker image

##### Step 1. Build the docker image

Run the following command to locally build the docker image:

```sh
make build_docker
```

##### Step 2. Create keys and `deposit_data-*.json`

Run the following command to enter the interactive CLI:

```sh
docker run -it --rm -v $(pwd)/validator_keys:/app/validator_keys eth-educators/ethstaker-deposit-cli
```

You can also run the tool with optional arguments:

```sh
docker run -it --rm -v $(pwd)/validator_keys:/app/validator_keys eth-educators/ethstaker-deposit-cli new-mnemonic --num_validators=<NUM_VALIDATORS> --mnemonic_language=english
```

Example for 1 validator on the [Holesky testnet](https://holesky.launchpad.ethereum.org/) using english:

```sh
docker run -it --rm -v $(pwd)/validator_keys:/app/validator_keys eth-educators/ethstaker-deposit-cli new-mnemonic --num_validators=1 --mnemonic_language=english --chain=holesky
```

###### Arguments
See [here](#arguments)

###### Successful message
See [here](#successful-message)

----

### For Windows users

#### Option 1. Download binary executable file

##### Step 1. Installation

See [releases page](https://github.com/eth-educators/ethstaker-deposit-cli/releases) to download and decompress the corresponding binary files.

##### Step 2. Create keys and `deposit_data-*.json`

Run one of the following command to enter the interactive CLI:

```sh
deposit.exe new-mnemonic
```

or

```sh
deposit.exe existing-mnemonic
```

You can also run the tool with optional arguments:

```sh
deposit.exe new-mnemonic --num_validators=<NUM_VALIDATORS> --mnemonic_language=english --chain=<CHAIN_NAME> --folder=<YOUR_FOLDER_PATH>
```

```sh
deposit.exe existing-mnemonic --num_validators=<NUM_VALIDATORS> --validator_start_index=<START_INDEX> --chain=<CHAIN_NAME> --folder=<YOUR_FOLDER_PATH>
```

###### Language Argument

See [here](#language_argument) for `--language` arguments.

###### Commands

See [here](#commands)

###### Arguments

See [here](#new-mnemonic-arguments) for `new-mnemonic` arguments\
See [here](#existing-mnemonic-arguments) for `existing-mnemonic` arguments\
See [here](#generate-bls-to-execution-change-arguments) for `generate-bls-to-execution-change` arguments\
See [here](#generate-bls-to-execution-change-keystore-arguments) for `generate-bls-to-execution-change-keystore` arguments\
See [here](#exit-transaction-keystore-arguments) for `exit-transaction-keystore` arguments\
See [here](#exit-transaction-mnemonic-arguments) for `exit-transaction-mnemonic` arguments

#### Option 2. Build `deposit-cli` with native Python

##### Step 0. Python version checking

Ensure you are using Python version >= Python12 (Assume that you've installed Python 3 as the main Python):

```sh
python -V
```

##### Step 1. Installation

Install the dependencies:

```sh
pip3 install -r requirements.txt
```

Or use the helper script:

```sh
sh deposit.sh install
```

##### Step 2. Create keys and `deposit_data-*.json`

Run one of the following command to enter the interactive CLI:

```sh
./deposit.sh new-mnemonic
```

or

```sh
./deposit.sh existing-mnemonic
```

You can also run the tool with optional arguments:

```sh
./deposit.sh new-mnemonic --num_validators=<NUM_VALIDATORS> --mnemonic_language=english --chain=<CHAIN_NAME> --folder=<YOUR_FOLDER_PATH>
```

```sh
./deposit.sh existing-mnemonic --num_validators=<NUM_VALIDATORS> --validator_start_index=<START_INDEX> --chain=<CHAIN_NAME> --folder=<YOUR_FOLDER_PATH>
```

###### Language Argument

See [here](#language_argument) for `--language` arguments.

###### Commands

See [here](#commands)

###### Arguments

See [here](#new-mnemonic-arguments) for `new-mnemonic` arguments\
See [here](#existing-mnemonic-arguments) for `existing-mnemonic` arguments\
See [here](#generate-bls-to-execution-change-arguments) for `generate-bls-to-execution-change` arguments\
See [here](#generate-bls-to-execution-change-keystore-arguments) for `generate-bls-to-execution-change-keystore` arguments\
See [here](#exit-transaction-keystore-arguments) for `exit-transaction-keystore` arguments\
See [here](#exit-transaction-mnemonic-arguments) for `exit-transaction-mnemonic` arguments

#### Option 3. Build `deposit-cli` with `virtualenv`

##### Step 0. Python version checking

Ensure you are using Python version >= Python3.9 (Assume that you've installed Python 3 as the main Python):

```cmd
python -V
```

##### Step 1. Installation

For the [virtualenv](https://virtualenv.pypa.io/en/latest/) users, you can create a new venv:

```cmd
pip3 install virtualenv
virtualenv venv
.\venv\Scripts\activate
```

and install the dependencies:

```cmd
pip3 install -r requirements.txt
```

##### Step 2. Create keys and `deposit_data-*.json`

Run one of the following command to enter the interactive CLI:

```cmd
python -m ethstaker_deposit new-mnemonic
```

or

```cmd
python -m ethstaker_deposit existing-mnemonic
```

You can also run the tool with optional arguments:

```cmd
python -m ethstaker_deposit new-mnemonic --num_validators=<NUM_VALIDATORS> --mnemonic_language=english --chain=<CHAIN_NAME> --folder=<YOUR_FOLDER_PATH>
```

```cmd
python -m ethstaker_deposit existing-mnemonic --num_validators=<NUM_VALIDATORS> --validator_start_index=<START_INDEX> --chain=<CHAIN_NAME> --folder=<YOUR_FOLDER_PATH>
```

###### Language Argument

See [here](#language_argument) for `--language` arguments.

###### Commands

See [here](#commands)

###### Arguments

See [here](#new-mnemonic-arguments) for `new-mnemonic` arguments\
See [here](#existing-mnemonic-arguments) for `existing-mnemonic` arguments\
See [here](#generate-bls-to-execution-change-arguments) for `generate-bls-to-execution-change` arguments\
See [here](#generate-bls-to-execution-change-keystore-arguments) for `generate-bls-to-execution-change-keystore` arguments\
See [here](#exit-transaction-keystore-arguments) for `exit-transaction-keystore` arguments\
See [here](#exit-transaction-mnemonic-arguments) for `exit-transaction-mnemonic` arguments

## Development

### Install basic requirements

```sh
python3 -m pip install -r requirements.txt
```

### Install testing requirements

```sh
python3 -m pip install -r requirements_test.txt
```

### Run tests

```sh
python3 -m pytest tests
```

### Run the app

```sh
python3 -m ethstaker_deposit [OPTIONS] COMMAND [ARGS]
```

### Building Binaries
**Developers Only**
##### Mac M1 Binaries

👋This is not the section you are looking for.👋
If you are trying to **build the binary** on macos with an M1 Mac and you are using pyenv to manage your python version. You'll probably need to reinstall a given python version using:
```
env PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install 3.10.3
```

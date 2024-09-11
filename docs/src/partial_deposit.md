# partial-deposit

{{#include ./snippet/warning_message.md}}

## Description
Creates a deposit file with an existing validator key. Can be used to initiate a validator or deposit to an existing validator.
If you wish to create a validator with 0x00 credentials, you must use the **[new-mnemonic](new_mnemonic.md)** or the **[existing-mnemonic](existing_mnemonic.md)** command.

## Optional Arguments

- **`--chain`**: The chain to use for generating the deposit data. Options are: 'mainnet', 'holesky', etc.

- **`--keystore`**: The keystore file associating with the validator you wish to deposit to.

- **`--keystore_password`**: The password that is used to encrypt the provided keystore. Note: It's not your mnemonic password. <span class="warning"></span>

- **`--amount`**: The amount you wish to deposit in ether. Must be at least 1 and can not have precision beyond 1 gwei. Defaults to 32 ether.

- **`--withdrawal_address`**: The withdrawal address of the existing validator or the desired withdrawal address.

- **`--output_folder`**: The folder path for the `deposit-*` JSON file.

## Output file
A successful call to this command will result in one [deposit data file](deposit_data_file.md) created.

## Example Usage

```sh
./deposit partial-deposit --keystore /path/to/keystore.json
```

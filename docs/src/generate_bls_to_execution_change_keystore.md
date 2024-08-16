# generate-bls-to-execution-change-keystore

<div class="warning">
This command is associated with the a proposed solution to update withdrawal credentials for those who are missing their mnemonic. At this point this has not been approved or implemented and there is no guarantee credentials will be modified in the future.
</div>

## Description
Signs a withdrawal credential update message using the provided keystore. This signature is one of the required proofs of ownership for validators who have lost or are missing their mnemonic and are unable to perform the BLS change needed to update their withdrawal credentials.

## Optional Arguments

- **`--chain`**: The chain to use for generating the deposit data. Options are: 'mainnet', 'holesky', etc.

- **`--keystore`**: The keystore file associating with the validator you wish to sign with. This keystore file should match the provided validator index.

- **`--keystore_password`**: The password that is used to encrypt the provided keystore. Note: It's not your mnemonic password. <span class="warning"></span>

- **`--validator_index`**: The validator index corresponding to the provided keystore.

- **`--withdrawal_address`**: Ethereum execution address in hexadecimal encoded form that you wish to set as your withdrawal credentials.

- **`--output_folder`**: The folder path for the `bls_to_execution_change_keystore_signature-*` JSON file.

- **`--devnet_chain_setting`**: The custom chain setting of a devnet or testnet. Note that it will override your `--chain` choice.

## Example Usage

```sh
./deposit generate-bls-to-execution-change
```

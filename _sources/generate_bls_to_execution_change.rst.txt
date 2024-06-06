Generate BLS to Execution Change
================================

``deposit generate-bls-to-execution-change``

This command generates a BLS to Execution change message.

Usage:
------

.. code-block:: bash

    deposit generate-bls-to-execution-change [OPTIONS]

Options:
--------

- `--validator_pubkey` - The validator's public key.
- `--withdrawal_credentials` - The new withdrawal credentials.
- `--chain` - Target chain (`mainnet`, `testnet`).

Example:
--------

.. code-block:: bash

    ./deposit generate-bls-to-execution-change --validator_pubkey 0x1234... --withdrawal_credentials 0xabcd... --chain mainnet

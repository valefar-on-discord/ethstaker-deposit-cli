Existing Mnemonic
=================

``deposit existing-mnemonic``

This command uses an existing mnemonic to generate validator keys.

Usage:
------

.. code-block:: bash

    deposit existing-mnemonic [OPTIONS]

Options:
--------

- `--mnemonic` - The existing mnemonic phrase.
- `--num_validators` - Number of validators to create keys for.
- `--folder` - Folder where the keystores and deposit data will be stored.
- `--chain` - Target chain (`mainnet`, `testnet`).

Example:
--------

.. code-block:: bash

    ./deposit existing-mnemonic --mnemonic "your mnemonic phrase" --num_validators 1 --folder /path/to/folder --chain mainnet

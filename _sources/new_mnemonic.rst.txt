New Mnemonic
============

``deposit new-mnemonic``

This command generates a new mnemonic and stores the validator keys.

Usage:
------

.. code-block:: bash

    deposit new-mnemonic [OPTIONS]

Options:
--------

- `--num_validators` - Number of validators to create keys for.
- `--folder` - Folder where the keystores and deposit data will be stored.
- `--chain` - Target chain (`mainnet`, `holesky`).

Example:
--------

.. code-block:: bash

    ./deposit new-mnemonic --num_validators 1 --folder /path/to/folder --chain mainnet

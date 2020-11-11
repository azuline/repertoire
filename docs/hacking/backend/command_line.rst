.. _backend_command_line:

Command Line
============

The ``cli`` package contains the implementation for the command line interface.
We use ``click`` to build the command line.

The ``commands`` module contains the root click group as well as functions
shared by commands.

.. note::

   As most of these commands are extremely thin wrappers, we do not have any
   tests for them. This may change in the future if the CLI commands become
   more complex.

.. automodule:: src.cli.commands
   :members:

   .. py:function:: src.cli.commands.commands

      The root click group that all commands derive from. This is the group
      invoked in ``__main__``.

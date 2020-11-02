.. _backend_command_line:

Command Line
============

The ``cli`` package contains the implementation for the command line interface.
We use ``click`` to build the command line.

The ``commands`` module contains the root click group as well as functions
shared by commands.

.. automodule:: src.cli.commands
   :members:

   .. py:function:: src.cli.commands.commands

      The root click group that all commands derive from. This is the group
      invoked in ``__main__``.

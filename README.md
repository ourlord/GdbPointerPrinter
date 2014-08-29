GdbPointerPrinter
============

Help to print contents for pointers in GDB. Especially deal with boost smart pointer.

This tool is still under development and construction.


How to install:
------------

In GDB, do below command at any time you want to use this tool:

    source <PATH-TO-THIS-SCRIPT>/PxPrinter.py

How to use:
-----------
    ppx <pointer_variable> [member]

First argument pointer_variable goes to the pointer we want to print. The second argument is optional. If you take that you will only print out that specific member for the object the pointer points to.

For example:

You have this in your source code:

    class A : public B
    {
      int param1;
      int param2;
      Obj obj1;
      Obj obj2;
    };
    A* a_ptr;

Then in GDB, do

    ppx a_ptr param1

This command will return the content of param1 for the a_ptr object.
If you don't type in any componenet, the command will just show you all components in the object.

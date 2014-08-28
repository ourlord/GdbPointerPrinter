GdbPointerPrinter
============

Help to print contents for pointers in GDB.
This tool is still under development and construction.


How to install:
------------

In GDB, do below command at any time you want to use this tool:

    source <PATH-TO-THIS-SCRIPT>/PxPrinter.py

How to use:
-----------
    ppx *<ptr> [member]

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

    ppx a_ptr [param1]

This command will return the content of param1 for the a_ptr object.
If you don't type in any componenet, the command will just show you all components in the object.

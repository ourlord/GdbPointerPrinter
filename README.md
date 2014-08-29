GdbPointerPrinter
============

Help to print contents for pointers in GDB. Especially deal with boost smart pointer.

This tool is still under development and construction.

Now there are two version of this command, one is the basic, another is the verbose. The verbose will iterate deep into the data structure and print out every thing inside or it into a indent format. Of course this will fill your screen...

Choose whether you like the basic one or the verbose one. Two version won't conflict with each other but for some reason, if you load them into Gdb, Gdb will mess them up. For example, you will see verbose output even you type in the basic command...


How to install:
------------

In GDB, do below command at any time you want to use this tool:

    source <PATH-TO-THIS-SCRIPT>/PxPrinter.py

Change *PxPrinter.py* to *PxPrinterVerbose.py* to use the verbose version.

How to use:
-----------
    ppx <pointer_variable> [member]

First argument *pointer_variable* goes to the pointer we want to print. The second argument is optional. If you take that you will only print out that specific member for the object the pointer points to.

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

This command will return the content of param1 for the *a_ptr* object.

If you don't type in any componenet, the command will just show you all components in the object.

To use the verbose output, just source the *PxPrinterVerbose.py* and use *ppv* instead of *ppx*.

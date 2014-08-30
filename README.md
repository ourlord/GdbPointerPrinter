GdbPointerPrinter
============

GdbPointerPrinter is a suite of Python scripts that aim to simplify the process of printing out the contents of pointers in GDB. In addition to standard pointers, GdbPointerPrinter also supports printing out the contents of smart pointers from the Boost Framework.

Currently, there are two commands that GdbPointerPrinter provides. Both commands offer the same basic functionality, but one prints verbose output. The verbose version will traverse a data structure, printing out its internal content using an indentation format.

**Note**: Currently, the two commands conflict. Therefore, it is recommended that you first try both commands individually and then decide which is most convenient for your particular use case.

Installation:
------------

Execute the following command to import the commands offered by GdbPointerPrinter into GDB:

    source <PATH-TO-THIS-SCRIPT>/PxPrinter.py

Change **PxPrinter.py** to **PxPrinterVerbose.py** if you prefer to use the verbose command.

Usage:
-----------

*Standard*

    ppx <pointer_variable> [member]
    
*Verbose*

    ppv <pointer_variable> [member]

Arguments:
-----------

The `<pointer_variable>` argument refers to the identifier of the pointer to be printed.

The `[member]` argument is optional. If provided, only the member specified will be printed.

Example:
-----------

Imagine you have the following in your soure code:

    class A : public B
    {
      int param1;
      int param2;
      Obj obj1;
      Obj obj2;
    };
    
    A* a_ptr;

To print out the value of `param1` in `a_ptr`, execute the following command within GDB:

    ppx a_ptr param1

If no member is specified (i.e. `ppx a_ptr`), all the contents of `a_ptr` will be printed. 

Alternatively, to show verbose output, execute the command:

    source PxPrinterVerbose.py 

and use `ppv` instead of `ppx`, like so:

    ppv a_ptr param1

**Note**: This tool is still under development and construction.

#
#   Author: Lincoln Xiong
#   Github account: ourlord
#   Contact: loli.lawliet@gmail.com
#   Project link:https://github.com/ourlord/GdbPointerPrinter/
#
#   Usage: Help to print pointer from address in GDB, especially when dealing with a
#   core-file(because you cannot run the process to do some dynamic stuffs).
#   
#   Example of using this command in GDB:
#
#   ppv <ptr_variable> [<member you concern about>]
#

import gdb

def printInner(v, c, level=0):
    # caculate indent
    indent = ''
    for i in range(0, level):
        indent += ' ' * 3 + '|'
    # check if the data tree hits the ground
    try:
        #gdb.write('===%s\n' % v.type.keys())
        v.type.keys()
    except:
        gdb.write( ('%s%s }\n' % (indent, v)).encode('utf-8') )
        return
    # if this pointer is a boost smart pointer, we only cares about the member px
    if 'px' in v.type.keys():
        v = v['px']
    # if this is a pointer, we dereference it
    if '*' in str(v.type.strip_typedefs()):
        if v == 0x0:
            if level != 0:
                gdb.write('%sNULL }\n' % indent)
                return
            else:
                gdb.write('NULL\n')
                return
        v = v.dereference()
    if c == None:
        # we don't want to dig too deep for the framework data structure
        if ('boost' in str(v.type.strip_typedefs())) or \
                ('std' in str(v.type.strip_typedefs())):
            gdb.write( ('%s%s }\n' % (indent, v)).encode('utf-8') )
        # iterate into the keys, print every member in the object
        for k in v.type.keys():
            # some member actually don't hit anything, we just ignore them
            try:
                v_ = v[k]
            except gdb.error:
                continue
            # use the encode in case there is any character issue
            #gdb.write( ( '%s = { %s }\n' % (k, v_) ).encode('utf-8') )
            gdb.write( ('%s%s ={\n' % (indent, k)).encode('utf-8') )
            printInner(v_, None, level+1)
    else:
        # we only care about member c at this time
        try:
            # use the encode in case there is any character issue
            #gdb.write( ( '%s = { %s }\n' % (c, v[c]) ).encode('utf-8') )
            #printHelper(v[c])
            gdb.write( ('%s%s ={\n' % (indent, c)).encode('utf-8') )
            printInner(v[c], None, level+1)
        except gdb.error, e:
            gdb.GdbError(e.message)
    gdb.write('%s}\n' % indent)

class PxPrinterVerbose(gdb.Command):
    """
    PxPrinterVerbos: a printer helps you to print out the content of a pointer in
    core-file especially. The command takes one optional argument, the component
    of that object you need to check.
    The verbose version gives you a verbose output.

        ppv <pointer_variable> [member class/paramter/method]
    """
    def __init__(self):
        super(PxPrinterVerbose, self).__init__(
                'ppv', gdb.COMMAND_DATA, gdb.COMPLETE_SYMBOL, False)
    def invoke(self, arg, from_tty):
        # deal with arguments
        space_location = arg.find(' ')
        # arguments not found
        if space_location == -1:
            (expr, component) = (arg, None)
        # arguments found
        else:
            (expr, component) = (arg[:space_location], arg[space_location+1:])
        # parse the name
        try:
            v = gdb.parse_and_eval(expr)
        except gdb.error, e:
            raise gdb.GdbError(e.message)
        printInner(v, component)

PxPrinterVerbose()

import gdb

def printInner(v, c):
    # this print just give the normal behavior of this script.
    # won't iterate into each member of the passin object
    if c == None:
        for k in v.type.keys():
            try:
                v_ = v[k]
            except gdb.error:
                continue
            gdb.write('%s = { %s }\n' % (k, v_))
    else:
        try:
            gdb.write('%s = { %s }\n' % (c, v[c]))
        except gdb.error, e:
            gdb.GdbError(e.message)

class PxPrinter(gdb.Command):
    """
    PxPrinter: a printer helps you to print out the content of a pointer invoke
    core-file especially. The command takes one optional argument, the component
    of that object you need to check.
        ppx *<pointer_variable>.px [member class/paramter/method]
    """
    def __init__(self):
        super(PxPrinter, self).__init__(
                'ppx', gdb.COMMAND_DATA, gdb.COMPLETE_SYMBOL, False)
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

PxPrinter()

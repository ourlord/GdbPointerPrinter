import gdb

# flag for using superb print
superb = False
# flag for using test print
test = False

def printInnerSuperb(v, c, level = 0):
    # advanced version of print, will iterate into each member until we hit the ground
    indent = ' ' * level * 4
    # reach the end of iteration, just write that value and return
    if v.type.keys() == None:
        if level == 0:
            gdb.write('%s\n' % (v,))
        else:
            gdb.write('%s%s\n' % (indent, v))
        return
    else:
        # if component takes None, we iterate every member
        if c == None:
            for k in v.type.keys():
                try:
                    v_ = v[k]
                except gdb.error:
                    gdb.write('%s%s\n' % (indent, k))
                    continue
                gdb.write('%s%s = {\n' % (indent, k))
                printInner(v_, None, level+1)
                gdb.write('%s}\n' % (indent,))
        # we only print out the specific member
        else:
            gdb.write('%s = {\n' % (c,))
            printInner(v[c], None, level+1)
            gdb.write('%s}\n' % (indent,))

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

def printInnerTest(v):
    # test print method helps develop this script
    gdb.write('%s\n' % (v.cast(v['px'].type.strip_typedefs()),))

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
        if test:
            printInnerTest(v)
        else:
            if superb:
                printInnerSuperb(v, component)
            else:
                printInner(v, component)

PxPrinter()

"""
Program: Peter’s Pizza Palace – Priority order-Placement Program v1.0.0 (.py)
Author: Cameron Coy (ccoy2@ivytech.edu)
Description:
"""
# import statements
from myGUI import *

# define main function
def main():
    """main program function description here"""
    # root gui window
    root = MyWindow('test', '600x400')
    
    main_frame = MyLabelFrame(root, 'test', row=0, col=0)
    a = MyButton(main_frame, 'test', row=0, col=0)
    # help(MyWindow)
    # main GUI loop
    root.mainloop()


# main loop
if __name__ == '__main__':
    main()


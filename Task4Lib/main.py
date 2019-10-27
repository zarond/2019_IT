import Task4Lib as lib
import numpy as np
#from mylib_dir.mylib import hello

def main():
    lib.Draw(0.1 + 2*np.random.rand(10,8))
    lib.ParetoTest()

if __name__ == "__main__":
    main()

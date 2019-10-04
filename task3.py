import numpy as np

def get_indices(N, n_batches, split_ratio):
    """Generates splits of indices from 0 to N-1 into uniformly distributed\
       batches. Each batch is defined by 3 indices [i, j, k] where\
       (j-i) = (1/split_ratio)*(k-j). The first batch starts with i = 0,\
       the last one ends with k = N - 1.
    Args:
        N (int): total counts
        n_batches (int): number of splits
        split_ratio (float): split ratio, defines position of j in [i, j, k].
    Returns:
        generator for batch indices [i, j, k]
        ---------------------------------------
        Assume inds(n)[i] = inds(n-1)[i] + a, where a = const and i = 0,1,2
        from this and the fact that K(n_batches) = N-1 we can find that a = (N - 1 - k0)/(n_batches-1)
        Next, find j0 = k0 /(split_ratio+1)
        Assuming that j1 = k0 we get that j1 = j0 + a = k0, where j0,a are already found before. 
        Finally, from that equation we get k0 = ((N-1)*(split_ratio+1))/(split_ratio*n_batches+1)
    """
    #inds = np.array([0, 0, 0])
    k0 = ((N-1)*(split_ratio+1))/(split_ratio*n_batches+1)
    j0 = k0 /(split_ratio+1)
    i0 = 0
    inds = np.array([i0, j0, k0])
    a = (N - 1 - k0)/(n_batches-1)
    inds -= a
    for i in range(n_batches):
        inds += a
        yield [int(round(inds[0])),int(round(inds[1])),int(round(inds[2]))]

def main():
    for inds in get_indices(100, 5, 0.25):
        print(inds)
    # expected result:
    # [0, 44, 55]
    # [11, 55, 66]
    # [22, 66, 77]
    # [33, 77, 88]
    # [44, 88, 99]

if __name__ == "__main__":
    main()

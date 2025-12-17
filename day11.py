import time
import networkx as nx

def advent11_1():
    file = open('input11.txt')
    to_devices = dict()
    lan = nx.DiGraph()
    for line in file:
        from_device, to_devs = line.strip('\n').split(':')
        lan.add_node(from_device)
        to_devices[from_device] = to_devs.split(' ')

    for from_d, to_d in to_devices.items():
        for d in to_d:
            if d != '':
                lan.add_edge(from_d, d)

    print('Nof paths(1):', len(list(nx.all_simple_paths(lan, source='you', target='out'))))


def advent11_2():
    file = open('input11.txt')
    to_devices = dict()
    lan = nx.DiGraph()
    for line in file:
        from_device, to_devs = line.strip('\n').split(':')
        lan.add_node(from_device)
        to_devices[from_device] = to_devs.split(' ')

    for from_d, to_d in to_devices.items():
        for d in to_d:
            if d != '':
                lan.add_edge(from_d, d)

    svr_pos = list(lan.nodes()).index('svr')
    dac_pos = list(lan.nodes()).index('dac')
    fft_pos = list(lan.nodes()).index('fft')
    out_pos = list(lan.nodes()).index('out')

    adj_mat = nx.adjacency_matrix(lan)
    pow_adj_mat = adj_mat

    nof_paths_svr2dac = 0
    nof_paths_svr2fft = 0
    nof_paths_dac2fft = 0
    nof_paths_fft2dac = 0
    nof_paths_dac2out = 0
    nof_paths_fft2out = 0
    break_time = False

    while True:
        k_len_paths = pow_adj_mat[svr_pos, dac_pos]
        nof_paths_svr2dac += k_len_paths
        if nof_paths_svr2dac > 0 and k_len_paths == 0:
            break_time = True
        else:
            break_time = False            
        k_len_paths = pow_adj_mat[svr_pos, fft_pos]
        nof_paths_svr2fft += k_len_paths
        if nof_paths_svr2fft > 0 and k_len_paths == 0:
            break_time = True
        else:
            break_time = False            
        k_len_paths = pow_adj_mat[dac_pos, fft_pos]
        nof_paths_dac2fft += k_len_paths
        if nof_paths_dac2fft > 0 and k_len_paths == 0:
            break_time = True
        else:
            break_time = False            
        k_len_paths = pow_adj_mat[fft_pos, dac_pos]
        nof_paths_fft2dac += k_len_paths
        if nof_paths_fft2dac > 0 and k_len_paths == 0:
            break_time = True
        else:
            break_time = False            
        k_len_paths = pow_adj_mat[dac_pos, out_pos]
        nof_paths_dac2out += k_len_paths
        if nof_paths_dac2out > 0 and k_len_paths == 0:
            break_time = True
        else:
            break_time = False            
        k_len_paths = pow_adj_mat[fft_pos, out_pos]
        nof_paths_fft2out += k_len_paths
        if nof_paths_fft2out > 0 and k_len_paths == 0:
            break_time = True
        else:
            break_time = False            
        pow_adj_mat *= adj_mat
        if break_time:
            break
        
    problematic_path_count = nof_paths_svr2dac*nof_paths_dac2fft*nof_paths_fft2out + nof_paths_svr2fft*nof_paths_fft2dac*nof_paths_dac2out
    print('Nof poblematic paths(2):', problematic_path_count)


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 11')
    advent11_1()
    advent11_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))

import torch
import timeit

a = torch.randn(10000, 10000)
b = torch.randn(10000, 10000)

c = torch.randn(10000, 10000).cuda()
d = torch.randn(10000, 10000).cuda()

def cpu_run():
    a1 = torch.matmul(a, b)
    return a1

def gpu_run():
    a2 = torch.matmul(c, d).cuda()
    return a2


cpu_time = timeit.timeit(cpu_run, number=10)
gpu_time = timeit.timeit(gpu_run, number=10)
print('warmup: CPU_Time: ', str(cpu_time) + 's GPU_Time: ' + str(gpu_time))
# 正式计算 10 次，取平均时间
cpu_time = timeit.timeit(cpu_run, number=10)
gpu_time = timeit.timeit(gpu_run, number=10)
print('run time: CPU_Time: ', str(cpu_time) + 's GPU_Time: ' + str(gpu_time))

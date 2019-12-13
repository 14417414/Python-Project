import tensorflow as tf
import timeit

# 创建在 CPU 上运算的 2 个矩阵
with tf.device('/cpu:0'):
    cpu_a = tf.random.normal([10000, 10000])
    cpu_b = tf.random.normal([10000, 10000])
    print(cpu_a.device, cpu_b.device)

# 创建使用 GPU 运算的 2 个矩阵
with tf.device('/gpu:0'):
    gpu_a = tf.random.normal([10000, 10000])
    gpu_b = tf.random.normal([10000, 10000])
    print(gpu_a.device, gpu_b.device)



def cpu_run():
    with tf.device('/cpu:0'):
        c = tf.matmul(cpu_a, cpu_b)
        return c
def gpu_run():
    with tf.device('/gpu:0'):
        c = tf.matmul(gpu_a, gpu_b)
        return c
        # 第一次计算需要热身，避免将初始化阶段时间结算在内

cpu_time = timeit.timeit(cpu_run, number=10)
gpu_time = timeit.timeit(gpu_run, number=10)
print('warmup: CPU_Time: ', str(cpu_time) + ' GPU_Time' + str(gpu_time))
# 正式计算 10 次，取平均时间
cpu_time = timeit.timeit(cpu_run, number=10)
gpu_time = timeit.timeit(gpu_run, number=10)
print('run time: CPU_Time: ', str(cpu_time) + ' GPU_Time' + str(gpu_time))

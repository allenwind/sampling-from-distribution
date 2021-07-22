# sampling-from-distribution

常见采样算法的实现：

- 线性同余法
- Box Muller方法（正太分布）
- 修正的Box Muller方法
- 基于中心极限定理的正太分布采样
- 逆变换采样
- 指数分布采样
- 拉普拉斯分布采样
- 接受-拒绝采样
- Metropolis Hastings
- Gibbs



## uniform-线性同余法

线性同余法的均匀分布采样，

![](asset/uniform-lcg-method.png)



## 正太分布采样

正太分布采样：

- Box Muller方法
- 修正的Box Muller方法
- 基于中心极限定理





## 接收-拒绝采样

以Laplace分布作为参考分布，采样正太分布，

![](asset/accept_reject_sampling_normal_laplace.png)



更新中~

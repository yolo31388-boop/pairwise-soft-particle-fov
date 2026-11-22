# pairwise-soft-particle-fov

## 领域

游戏、图形与多媒体

## 主题

软粒子 FOV 归一

## 说明

视空间深度、FOV 归一与比例淡出。

初始状态下 `render/soft_particle_fov.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。

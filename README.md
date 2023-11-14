https://github.com/wangzheng0822/algo

https://github.com/iostalks/Algorithms

method:
    fast/slow pointer
    double pointer
    double interval
    binary search
    stack
    queue
    hash
    binary tree
    dfs
    bfs
    heap
    greedy
    divide and conquer
    recursion
    back tracking
    dp（状态转移表法，状态转移方程法）

- 散列表：插入删除查找都是O(1), 是最常用的，但其缺点是不能有序遍历以及扩容缩容的性能损耗。适用于那些不需要有序遍历，数据更新不那么频繁的。
- 跳表：插入删除查找都是O(logn), 并且能顺序遍历。缺点是空间复杂度O(n)。适用于不那么在意内存空间的，其有序遍历和区间查找非常方便。
- 红黑树：插入删除查找都是O(logn), 中序遍历即是顺序遍历，稳定。缺点是难以实现，去查找不方便。其实跳表更佳，但红黑树已经用于很多地方了
# repeadoupy
删除/汇集某目录下的重复文件

## derep_all 方法
搜集齐文件后再遍历

## derep_each 方法
直接查找文件，看起来效率可能会高一点<br/>
但是也是递归的<br/>
walk还没弄明白……

## delete_rep_file 参数
False 把重复文件汇集到某处，若文件大小大于 move_file_max_size 则只记录位置<br/>
True 删除重复的文件

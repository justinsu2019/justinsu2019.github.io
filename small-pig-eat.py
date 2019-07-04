import numpy as np
import pandas as pd

main = True

recycle = ['可回收','废弃计算机','纸张','纸盒','瓶子','塑料盒','塑料袋','纸类','打印机','复印纸','包装盒','饮料瓶','塑料杯','保鲜袋','复印件','宣传单','纸巾盒','硬质塑料瓶','果冻杯','包装袋','传真机','包装纸','牛奶盒','软桶','快递包装袋','扫描仪','信封','塑料泡沫','电视机','水果网套','空调机','热饮杯','报纸','纸板箱','纸箱','PET塑料瓶','矿泉水瓶','冰激凌盒','点心盒','塑料瓶','酸奶杯','保鲜膜','硬塑料瓶','零食包装袋','饮料','利乐包装','杯盖','咖啡杯','快递袋','杂志']

harmful = ['纽扣电池','汞','废荧光灯管','过期药品','油漆','药品','废油漆','充电电池','手机电池','废节能灯','废农药','杀虫剂','残余液体','废水银温度计','废水银血压计','荧光棒','纸巾','不可生化降解牙签']

Shilaji = ['菜帮菜叶','剩菜','剩饭','肉类','鱼虾','蛋壳']

ganlaji = ['干垃圾','纺织品','灰土','土','灰尘','灰','织物','不确定是否可以回收废纸','砖瓦','陶瓷','木竹类废弃物中不可回收的部分','拖把','抹布','渣土','包装盒','干电池','贮存','木牙签','陶瓷碗碟','树枝等','植物硬壳','果壳','枯萎花草','花草','1号电池','7号电池','3号电池','4号电池','9号电池','5号电池','7号电池','3号电池','4号电池','9号电池','5号电池']


# for s in recycle:
'''
print(3 for i in recycle if '可' in i)

for s in recycle:
    if 'bu' in s:
        print('11')
'''


print(bool(s for s in recycle if 'bu' in s))

print(('111' in s for s in recycle) and "yes" or "not")

print("Little pig eats what? Ask him!: ")


while main==True:
        
    garbage = input("Please input what's in your hand?: ")

    output = ''
    
    for s in recycle:
        if garbage in s:
            output = '请放在可回收垃圾桶里'
    for d in harmful:
        if garbage in d:
            output = '吃死了。。。请放在有害垃圾桶里'
    for f in Shilaji:
        if garbage in f:
            output = '可以吃哦。。。请放在湿垃圾桶里'
    for g in ganlaji:
        if garbage in g:
            output = '我不吃哦！请放在干垃圾桶里'

    print(output)
    print('please re-enter with Chinese Characters, tips: input what the item made of: ')

    if garbage == 'exit':
        exit

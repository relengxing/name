#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
中文名字生成器 - 增强版
用于生成更多两字名字和提高大姓比例
"""

import random

# 百家姓（前100位，按人口比例排序）
# 前10大姓占比约40%，前20大姓占比约50%
SURNAMES = {
    # 超大姓（每个约占5-7%）- 权重10
    'super': ['王', '李', '张', '刘', '陈'],
    
    # 大姓（每个约占2-3%）- 权重5
    'major': ['杨', '黄', '赵', '周', '吴', '徐', '孙', '马', '朱', '胡'],
    
    # 常见姓（每个约占1-2%）- 权重3
    'common': [
        '郭', '何', '林', '高', '罗', '郑', '梁', '谢', '宋', '唐',
        '许', '韩', '冯', '邓', '曹', '彭', '曾', '肖', '田', '董'
    ],
    
    # 一般姓（每个约占0.5-1%）- 权重1
    'normal': [
        '袁', '潘', '于', '蒋', '蔡', '余', '杜', '叶', '程', '苏',
        '魏', '吕', '丁', '任', '沈', '姚', '卢', '姜', '崔', '钟',
        '谭', '陆', '汪', '范', '金', '石', '廖', '贾', '夏', '韦',
        '付', '方', '白', '邹', '孟', '熊', '秦', '邱', '江', '尹',
        '薛', '闫', '段', '雷', '侯', '龙', '史', '陶', '黎', '贺',
        '顾', '毛', '郝', '龚', '邵', '万', '钱', '严', '覃', '武',
        '戴', '莫', '孔', '向', '常'
    ]
}

# 单字名 - 按性别和年代分类
GIVEN_NAMES_SINGLE = {
    # 70-80年代常用字（男）
    'male_70s': [
        '伟', '强', '军', '勇', '杰', '涛', '磊', '超', '刚', '峰',
        '斌', '辉', '鹏', '波', '明', '亮', '勋', '凯', '建', '华',
        '国', '志', '平', '东', '文', '宇', '海', '力', '民', '春',
        '松', '林', '忠', '兴', '良', '发', '成', '康', '星', '光',
        '天', '达', '安', '彦', '朗', '清', '直', '刚', '勤', '克'
    ],
    
    # 70-80年代常用字（女）
    'female_70s': [
        '芳', '娜', '秀', '敏', '静', '丽', '霞', '艳', '莉', '红',
        '梅', '玲', '燕', '华', '琳', '雪', '婷', '洁', '萍', '凤',
        '兰', '英', '琴', '云', '珍', '玉', '秋', '荣', '翠', '月',
        '香', '珠', '素', '青', '惠', '贞', '爱', '妹', '纯', '真',
        '娟', '文', '君', '秀', '美', '丽', '芬', '芝', '桂', '莲'
    ],
    
    # 90-00年代常用字（男）
    'male_90s': [
        '浩', '宇', '轩', '杰', '豪', '博', '睿', '瑞', '峰', '磊',
        '涛', '鹏', '昊', '宸', '阳', '晨', '泽', '凯', '洋', '锋',
        '超', '龙', '俊', '飞', '鑫', '强', '亮', '晖', '伟', '刚',
        '辉', '斌', '威', '贤', '文', '武', '毅', '坚', '刚', '健',
        '力', '利', '胜', '雄', '勇', '猛', '谦', '廉', '正', '直'
    ],
    
    # 90-00年代常用字（女）
    'female_90s': [
        '欣', '怡', '婷', '雨', '雪', '梦', '琪', '嘉', '萱', '涵',
        '瑶', '薇', '雅', '静', '琳', '洁', '颖', '慧', '敏', '莹',
        '娜', '佳', '彤', '晴', '妍', '婷', '蕊', '璐', '倩', '丽',
        '茹', '美', '玉', '珊', '莎', '锦', '黛', '青', '倩', '婉',
        '柔', '竹', '霭', '凝', '晓', '欢', '霜', '飘', '育', '滢'
    ],
    
    # 10-20年代常用字（男）
    'male_10s': [
        '睿', '泽', '宇', '轩', '浩', '博', '晨', '阳', '宸', '昊',
        '梓', '子', '俊', '宇', '翔', '辰', '逸', '铭', '煜', '霖',
        '诺', '凯', '琦', '航', '鹏', '骏', '瑾', '熙', '墨', '枫',
        '朗', '伯', '言', '然', '安', '易', '亦', '思', '哲', '谦',
        '恒', '修', '贤', '德', '义', '礼', '智', '信', '仁', '和'
    ],
    
    # 10-20年代常用字（女）
    'female_10s': [
        '梓', '子', '雨', '思', '诗', '欣', '涵', '萱', '琪', '瑶',
        '馨', '妍', '婷', '怡', '嘉', '雅', '悦', '彤', '晴', '蕊',
        '宁', '心', '语', '莹', '涵', '薇', '菲', '珺', '瑾', '璇',
        '柔', '清', '芷', '若', '可', '依', '伊', '然', '安', '舒',
        '岚', '霏', '音', '韵', '姗', '娅', '纯', '真', '灵', '秀'
    ]
}

# 双字名常用字组合
GIVEN_NAMES_DOUBLE = {
    # 经典双字名（70-80年代）
    'classic': [
        '建国', '建军', '建华', '国强', '志强', '晓明', '秀英', '丽华',
        '淑芬', '春梅', '桂英', '桂兰', '玉兰', '玉梅', '桂珍', '秀兰',
        '海燕', '红梅', '桂香', '秀梅', '秀芳', '秀云', '秀荣', '玉珍',
        '建平', '海英', '桂芳', '桂荣', '玉华', '雪梅', '丽丽', '春华',
        '国华', '志刚', '志军', '国军', '建设', '建新', '建文', '建明',
        '红星', '红旗', '红军', '红卫', '国栋', '国良', '国平', '国庆',
        '淑珍', '淑华', '淑兰', '淑英', '春芳', '春燕', '春红', '春霞',
        '桂花', '桂芳', '桂芬', '桂云', '玉芳', '玉英', '玉芬', '玉霞'
    ],
    
    # 现代双字名（90-00年代）
    'modern': [
        '佳丽', '浩然', '雨萱', '思远', '紫涵', '雨轩', '思琪', '诗涵',
        '欣怡', '雨彤', '思雨', '雨桐', '思辰', '雨晨', '思颖', '思语',
        '雨泽', '思婷', '思羽', '雨桦', '思蕊', '雨薇', '浩宇', '俊杰',
        '天翊', '博文', '俊熙', '宇航', '煜祺', '智辉', '正豪', '昊然',
        '雅婷', '雅琪', '雅欣', '雅雯', '静怡', '静雯', '静萱', '静宜',
        '佳音', '佳怡', '佳欣', '佳琪', '欣然', '欣悦', '欣怡', '欣妍',
        '博涵', '博雅', '博文', '博宇', '浩博', '浩宇', '浩轩', '浩然',
        '俊哲', '俊豪', '俊逸', '俊雄', '俊彦', '俊才', '俊贤', '俊杰'
    ],
    
    # 当代双字名（10-20年代）
    'contemporary': [
        '子轩', '梓轩', '宇轩', '子涵', '梓涵', '子墨', '梓萱', '雨桐',
        '思涵', '梓豪', '皓轩', '子睿', '梓睿', '雨泽', '思睿', '语桐',
        '诗涵', '雨桐', '雨欣', '思彤', '梓彤', '子瑜', '雨琪', '思琪',
        '梓琪', '雨涵', '思涵', '诗语', '语馨', '子晴', '梓晴', '雨晴',
        '子安', '子恒', '子谦', '子贤', '子昂', '子宸', '子辰', '子诚',
        '梓安', '梓恒', '梓贤', '梓宸', '梓辰', '梓诚', '梓航', '梓朗',
        '诗雨', '诗琪', '诗涵', '诗颖', '诗婷', '诗瑶', '诗蕊', '诗嘉',
        '语嫣', '语彤', '语桐', '语涵', '语诗', '语馨', '语凝', '语芙',
        '若曦', '若涵', '若雪', '若诗', '若萱', '若彤', '若瑶', '若琳',
        '梦琪', '梦瑶', '梦涵', '梦萱', '梦蝶', '梦雪', '梦洁', '梦婷'
    ],
    
    # 文艺双字名
    'literary': [
        '清扬', '清欢', '清和', '清越', '清妍', '清雅', '清嘉', '清懿',
        '婉清', '婉约', '婉如', '婉仪', '婉柔', '婉妙', '婉娴', '婉然',
        '静姝', '静好', '静仪', '静曼', '静娴', '静婉', '静雅', '静宜',
        '雅琴', '雅韵', '雅致', '雅音', '雅诗', '雅歌', '雅正', '雅洁',
        '诗礼', '诗书', '诗画', '诗意', '诗情', '诗韵', '诗音', '诗文',
        '文君', '文静', '文雅', '文慧', '文馨', '文琪', '文嘉', '文淑',
        '书瑶', '书雅', '书慧', '书琴', '书韵', '书香', '书萱', '书涵',
        '安然', '安宁', '安乐', '安康', '安和', '安怡', '安静', '安悦'
    ]
}


def generate_two_char_names(count=3000):
    """生成两个字的名字（姓+单字）"""
    names = set()
    
    # 按权重生成姓氏列表（调整权重更接近真实人口比例）
    weighted_surnames = (
        SURNAMES['super'] * 20 +  # 超大姓权重20（王李张刘陈）
        SURNAMES['major'] * 8 +   # 大姓权重8
        SURNAMES['common'] * 3 +  # 常见姓权重3
        SURNAMES['normal'] * 1    # 一般姓权重1
    )
    
    # 合并所有单字名
    all_given_names = []
    for category in GIVEN_NAMES_SINGLE.values():
        all_given_names.extend(category)
    
    attempts = 0
    max_attempts = count * 3
    
    while len(names) < count and attempts < max_attempts:
        surname = random.choice(weighted_surnames)
        given_name = random.choice(all_given_names)
        full_name = surname + given_name
        
        if len(full_name) == 2:  # 确保是两个字
            names.add(full_name)
        
        attempts += 1
    
    return sorted(list(names))


def generate_three_char_names(count=3000):
    """生成三个字的名字（姓+双字）"""
    names = set()
    
    # 按权重生成姓氏列表（调整权重更接近真实人口比例）
    weighted_surnames = (
        SURNAMES['super'] * 20 +  # 超大姓权重20
        SURNAMES['major'] * 8 +   # 大姓权重8
        SURNAMES['common'] * 3 +  # 常见姓权重3
        SURNAMES['normal'] * 1    # 一般姓权重1
    )
    
    # 合并所有双字名
    all_double_names = []
    for category in GIVEN_NAMES_DOUBLE.values():
        all_double_names.extend(category)
    
    # 也支持单字组合成双字
    all_single_names = []
    for category in GIVEN_NAMES_SINGLE.values():
        all_single_names.extend(category)
    
    attempts = 0
    max_attempts = count * 3
    
    while len(names) < count and attempts < max_attempts:
        surname = random.choice(weighted_surnames)
        
        # 60% 使用预定义双字名，40% 使用随机组合
        if random.random() < 0.6 and all_double_names:
            given_name = random.choice(all_double_names)
        else:
            # 随机组合两个单字
            given_name = random.choice(all_single_names) + random.choice(all_single_names)
        
        full_name = surname + given_name
        
        if len(full_name) == 3:  # 确保是三个字
            names.add(full_name)
        
        attempts += 1
    
    return sorted(list(names))


def merge_with_existing(new_names, existing_file='names/chinese_names.txt'):
    """合并新生成的名字与现有名字库"""
    existing_names = set()
    
    # 读取现有名字
    try:
        with open(existing_file, 'r', encoding='utf-8') as f:
            existing_names = set(line.strip() for line in f if line.strip())
        print(f"✅ 已读取现有名字库：{len(existing_names)} 个名字")
    except FileNotFoundError:
        print("⚠️ 未找到现有名字库文件，将创建新文件")
    
    # 合并名字
    all_names = existing_names | set(new_names)
    
    return sorted(list(all_names))


def analyze_names(names):
    """分析名字库统计信息"""
    two_char = [n for n in names if len(n) == 2]
    three_char = [n for n in names if len(n) == 3]
    
    # 统计姓氏分布
    surname_count = {}
    for name in names:
        surname = name[0]
        surname_count[surname] = surname_count.get(surname, 0) + 1
    
    print("\n" + "="*50)
    print("📊 名字库统计信息")
    print("="*50)
    print(f"总名字数：{len(names)}")
    print(f"  - 两字名（姓+单字）：{len(two_char)} 个 ({len(two_char)/len(names)*100:.1f}%)")
    print(f"  - 三字名（姓+双字）：{len(three_char)} 个 ({len(three_char)/len(names)*100:.1f}%)")
    
    print("\n📈 前20大姓分布：")
    top_surnames = sorted(surname_count.items(), key=lambda x: x[1], reverse=True)[:20]
    for surname, count in top_surnames:
        percentage = count / len(names) * 100
        bar = '█' * int(percentage)
        print(f"  {surname}: {count:4d} ({percentage:5.2f}%) {bar}")
    
    print("="*50 + "\n")


def main():
    """主函数"""
    print("🚀 中文名字生成器 - 增强版")
    print("="*50)
    
    # 生成新名字（增加数量）
    print("\n1️⃣ 生成两字名...")
    two_char_names = generate_two_char_names(5000)  # 从3000增加到5000
    print(f"✅ 已生成 {len(two_char_names)} 个两字名")
    
    print("\n2️⃣ 生成三字名...")
    three_char_names = generate_three_char_names(5000)  # 从3000增加到5000
    print(f"✅ 已生成 {len(three_char_names)} 个三字名")
    
    # 合并新旧名字
    print("\n3️⃣ 处理名字...")
    all_new_names = two_char_names + three_char_names
    all_new_names = sorted(list(set(all_new_names)))  # 去重并排序
    print(f"✅ 去重后共 {len(all_new_names)} 个新名字")
    
    # 分析统计
    analyze_names(all_new_names)
    
    # 保存到文件
    output_file = 'names/chinese_names_enhanced.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        for name in all_new_names:  # 只保存新生成的名字，不合并旧的
            f.write(name + '\n')
    
    print(f"💾 已保存到：{output_file}")
    print(f"📝 共生成 {len(all_new_names)} 个新名字")
    print("\n✨ 完成！")
    print("💡 提示：程序会自动从两个文件中各取50%的名字")


if __name__ == '__main__':
    main()


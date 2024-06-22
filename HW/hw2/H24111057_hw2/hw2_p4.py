""" 
author: H24111057 姚博瀚
"""


#### 先計算最底部三角形的寬來決定"空格數"(space number)

# Obtain the height of each layer (layer means each triangle)
def calculate_height_for_each_layer(side_length_of_top_layer, groth_rate, number_of_layers):
    ''' 
    return: 
    (1) stored_list: list of each layers' height 
    (2) total_height: Total height of the tree (without the part of trunk) 
    '''
    tsl = side_length_of_top_layer
    gr = groth_rate
    l = number_of_layers
    
    ## 先將 ""每層三角形的高"" 視為一數列 : 規律 第n層的高度 = 首項 + 公差*(項數-1) - 1(因為頂部重疊) = an + d*(n-1) - 1 (where n != 1)
    # 定義:  # l 定義為項數n
            # tsl 定義為首項a1
            # gr 定義為公差d

    # 將每層三角形的高儲存
    stored_list = []
    # 將不斷迭代得到的nh加總會得到總高度total_height
    total_height = 0
    for i in range(1,l+1) :
        if i == 1 :
            nh = tsl + gr*(i-1)       # 最頂端的三角形其頂部並無重疊!
        else :
            nh = tsl + gr*(i-1) - 1   # 頂部重疊
        
        stored_list.append(nh)
        total_height += nh

    return stored_list, total_height

# Obtain the width of each rows in each layer (layer means each triangle)
def calculate_width_of_each_rows_in_each_layer(list_of_each_layers_height):
    ''' 
    input:
    list_of_each_layers_height: The list containing the height of each layers (Obtain from calculate_height_for_each_layer function)
    
    return:
    width_list_each_layers : The nested list containing the list of the width of each row in each layers
    eg. [[1, 3], [3, 5, 7], [3, 5, 7, 9, 11]]
    '''
    stored_list = list_of_each_layers_height
    ## 得到""每層三角形的高""可用於計算""當層三角形中每行的寬度""(i.e.公差為2, 項數=nh 的等差數列)
    width_list_each_layers = []
    # Loop through each layer (layer means a triangle)
    for j in stored_list :
        if j == stored_list[0] :         # 若為最頂部三角形:首項=1
            width_list = []
            for k in range(1,j+1) :
                width_each_row = 1 + 2*(k-1)
                width_list.append(width_each_row)
            # add the result of first layer into width_list_each_layers
            width_list_each_layers.append(width_list)

        else :                           # 反之,首項=3(因為頂部重疊)
            width_list = []
            for k in range(1,j+1) :
                width_each_row = 3 + 2*(k-1)
                width_list.append(width_each_row)
            # add the result of layer (second layer~) into width_list_each_layers
            width_list_each_layers.append(width_list)
    return width_list_each_layers


def print_tree(width_list_each_layers, trunk_width, trunk_height):
    width_of_tree = width_list_each_layers[-1][-1]
    
    ''' For the use of debugging
    print(f"width_of_tree: {width_of_tree}")
    '''
    
    # Print tree
    for layer in width_list_each_layers: 
        # first layer
        if layer[0] == 1:
            # First row to the row before last row
            for i in range(0, len(layer)-1):
                width_each_row = layer[i]
                if width_each_row == 1:
                    space = (width_of_tree - width_each_row) / 2
                    space = int(space)
                    row = ' ' * space + '#' + ' ' * space
                    print(row)
                else:
                    space = (width_of_tree - width_each_row) / 2
                    space = int(space)
                    row = ' ' * space + '#' + '@' * (width_each_row - 2) + '#' + ' ' * space
                    print(row)
                    
            # Last row of the fisrt layer
            width_each_row = layer[-1]
            space = (width_of_tree - width_each_row) / 2
            space = int(space)
            row = ' ' * space + '#' * width_each_row + ' ' * space
            print(row)
        # Second layer ~ last layer
        else:
            for i in range(0, len(layer)-1):
                width_each_row = layer[i]
                space = (width_of_tree - width_each_row) / 2
                space = int(space)
                row = ' ' * space + '#' + '@' * (width_each_row - 2) + '#' + ' ' * space
                print(row)
                
            # Last row of the layer
            width_each_row = layer[-1]
            space = (width_of_tree - width_each_row) / 2
            space = int(space)
            row = ' ' * space + '#' * width_each_row + ' ' * space
            print(row)
    
    # Print drunk
    i = 0
    space = (width_of_tree - trunk_width) / 2
    space = int(space)
    for i in range(trunk_height):
        row = ' ' * space + '|' * trunk_width + ' ' * space
        print(row)
            

while True:
    #### 判斷使用者輸入正確的參數,並記錄之
    layers = (input("Enter the number of layers (2 to 5) = "))         
    top_side_length = input("Enter the side lengths of the top layer = ")
    groth_rate = input("Enter the growth of each layer = ")             
    trunk_width = input("Enter the trunk width (odd number, 3 to 9) = ")
    trunk_height = input("Enter the trunk height (4 to 10) = ")

    if layers.isdigit() and top_side_length.isdigit() and groth_rate.isdigit() and trunk_width.isdigit() and trunk_height.isdigit() :
        l = int(layers)
        tsl = int(top_side_length)
        gr = int(groth_rate)
        tw = int(trunk_width)
        th = int(trunk_height)
        if (2<=l<=5) and (tw in range(3,10,2)) and (4<=th<=10) :
            list_of_each_layers_height, _ = calculate_height_for_each_layer(tsl, gr, l)
            ''' For the use of debugging
            print(f"list_of_each_layers_height: {list_of_each_layers_height}")
            '''
            
            width_list_each_layers = calculate_width_of_each_rows_in_each_layer(list_of_each_layers_height)
            ''' For the use of debugging
            print(f"width_list_each_layers: {width_list_each_layers}")
            '''
            print_tree(width_list_each_layers, tw, th)
            break
        else :
            print("Please enter valid numbers !")
    else :
        print("Please enter valid integers !")